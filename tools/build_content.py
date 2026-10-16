"""Turn the generated docs/ tree into Hugo content for the Hextra theme.

The docs generators (tools/build_docs.php and tools/phpdoc.php in the
MadelineProto repo) emit Jekyll-style markdown; this script maps it to Hugo
while keeping every URL unchanged.

Usage: python3 tools/build_content.py
"""
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "docs")
CONTENT = os.path.join(ROOT, "content")
STATIC = os.path.join(ROOT, "static")
EDIT_BASE = "https://github.com/danog/MadelineProtoDocs/edit/master/docs/"
SECTIONS = ("docs", "API_docs", "PHP")

# Leaf pages in these sections are hidden from the sidebar: their index pages
# already link to every entry, and Hextra renders the whole tree on each page.
HIDDEN_LEAVES = ("API_docs/methods/", "API_docs/constructors/", "API_docs/types/")
PHP_MAX_SIDEBAR_DEPTH = 3  # PHP/danog/MadelineProto/X.md


def parse_scalar(v):
    v = v.strip()
    if v.startswith('"') and v.endswith('"'):
        escapes = {"n": "\n", "t": "\t"}
        return re.sub(r"\\(.)", lambda m: escapes.get(m.group(1), m.group(1)), v[1:-1])
    if v.startswith("'") and v.endswith("'"):
        return v[1:-1].replace("''", "'")
    return v


def split_front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            k, v = line.split(":", 1)
            fm[k.strip()] = parse_scalar(v)
    return fm, text[m.end():]


def strip_first_heading(body):
    """Hextra renders the title itself, drop the generated one."""
    return re.sub(r"\A\s*#{1,2} [^\n]*\n", "", body, count=1)


def dump(fm):
    return "---\n" + "".join(f"{k}: {json.dumps(v)}\n" for k, v in fm.items()) + "---\n"


def url_for(rel):
    stem = rel[:-3]
    return "/" + (stem[: -len("index")] + "index.html" if stem.endswith("index") else stem + ".html")


def convert(rel):
    with open(os.path.join(SRC, rel), encoding="utf-8") as f:
        fm, body = split_front_matter(f.read())
    out = {"title": fm.get("title", os.path.basename(rel)[:-3])}
    parts = rel.split("/")
    is_index = parts[-1] == "index.md"

    if parts[0] == "PHP" and not is_index:
        out["linkTitle"] = out["title"].split(":", 1)[0].split("\\")[-1].strip("` ")
    if fm.get("description"):
        out["description"] = fm["description"]
    if str(fm.get("nav_order", "")).isdigit():
        out["weight"] = int(fm["nav_order"])
    elif rel == "API_docs/index.md":
        out["weight"] = 1000
    if fm.get("redirect_from"):
        out["aliases"] = [fm["redirect_from"]]
    out["url"] = url_for(rel)
    out["editURL"] = EDIT_BASE + rel

    hidden = (
        (len(parts) == 1 and not is_index)  # legacy root-level method pages
        or (rel.startswith(HIDDEN_LEAVES) and not is_index)
        or (parts[0] == "PHP" and len(parts) - 1 > PHP_MAX_SIDEBAR_DEPTH)
    )
    if hidden:
        out["sidebar"] = {"exclude": True}
    if rel == "index.md":
        out["type"] = "docs"
        out["cascade"] = {"type": "docs"}

    # Guides sit at the root of the sidebar, like in Just the Docs, while
    # keeping their /docs/X.html URLs.
    dest_rel = rel[len("docs/"):] if parts[0] == "docs" else rel
    if is_index:
        dest_rel = dest_rel[: -len("index.md")] + "_index.md"
    elif os.path.isdir(os.path.join(SRC, rel[:-3])) and not os.path.exists(os.path.join(SRC, rel[:-3], "index.md")):
        # Hugo can't have both X.md and X/, e.g. the EventHandler class page
        # and the EventHandler namespace: make the page the section page.
        dest_rel = dest_rel[:-3] + "/_index.md"
    dest = os.path.join(CONTENT, dest_rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(dump(out) + strip_first_heading(body))


def add_missing_section_indexes():
    for root, dirs, files in os.walk(CONTENT):
        if root == CONTENT or "_index.md" in files:
            continue
        rel = os.path.relpath(root, CONTENT)
        links = sorted(f[:-3] for f in files if f.endswith(".md")) + sorted(d + "/index" for d in dirs)
        body = "".join(f"* [{link.replace('/index', '')}]({link}.html)\n" for link in links)
        fm = {"title": os.path.basename(root), "url": f"/{rel}/index.html"}
        if rel.startswith("PHP") and rel.count("/") + 1 > PHP_MAX_SIDEBAR_DEPTH:
            fm["sidebar"] = {"exclude": True}
        with open(os.path.join(root, "_index.md"), "w", encoding="utf-8") as f:
            f.write(dump(fm) + body)


def copy_static():
    for name in os.listdir(SRC):
        src = os.path.join(SRC, name)
        if name in SECTIONS or name.endswith(".md"):
            continue
        dst = os.path.join(STATIC, name)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
    # Browsers look for these at the root.
    for name in os.listdir(os.path.join(SRC, "favicons")):
        shutil.copy2(os.path.join(SRC, "favicons", name), os.path.join(STATIC, name))


def main():
    shutil.rmtree(CONTENT, ignore_errors=True)
    shutil.rmtree(STATIC, ignore_errors=True)
    os.makedirs(STATIC)
    count = 0
    for root, dirs, files in os.walk(SRC):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in files:
            if name.endswith(".md"):
                convert(os.path.relpath(os.path.join(root, name), SRC))
                count += 1
    add_missing_section_indexes()
    copy_static()
    print(f"Converted {count} pages")


if __name__ == "__main__":
    main()
