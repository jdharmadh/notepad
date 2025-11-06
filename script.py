import os, re, shutil

posts_dir = "_posts"
assets_dir = "notepad/assets/images"
os.makedirs(assets_dir, exist_ok=True)

for fname in os.listdir(posts_dir):
    if fname.endswith(".md"):
        path = os.path.join(posts_dir, fname)
        text = open(path).read()

        # Fix image links
        matches = re.findall(r'!\[\[(.*?)\]\]', text)
        for img in matches:
            src = os.path.join(posts_dir, img)
            dst = os.path.join(assets_dir, os.path.basename(img))
            if os.path.exists(src):
                shutil.move(src, dst)
            text = text.replace(f"![[{img}]]", f"![{img}](/assets/images/{os.path.basename(img)})")

        # Convert inline math: $...$ → \(...\)
        # Avoid touching already-converted or escaped dollar signs
        text = re.sub(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', r'\\(\1\\)', text)

        open(path, "w").write(text)
