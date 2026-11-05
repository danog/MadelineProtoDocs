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
from urllib.parse import urljoin

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "docs")
CONTENT = os.path.join(ROOT, "content")
STATIC = os.path.join(ROOT, "static")
EDIT_BASE = "https://github.com/danog/MadelineProtoDocs/edit/master/docs/"
SITE = "https://docs.madelineproto.xyz"
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
    PAGES.append({"rel": rel, "url": out["url"], "title": out["title"], "description": out.get("description", ""),
                  "weight": out.get("weight", 10**6), "body": strip_first_heading(body)})


# Every page, for the Markdown copies and llms.txt: rel (in docs/), url, title, description, weight, body.
PAGES = []


def md_url(url):
    """/docs/FILES.html -> /docs/FILES.md, next to the HTML page (so relative links keep working)."""
    return url[: -len(".html")] + ".md"


def markdown_page(page):
    head = f"# {page['title']}\n\n" + (f"> {page['description']}\n\n" if page["description"] else "")
    return head + page["body"].strip() + "\n"


def absolute_links(text, url):
    """Relative links of a page (Markdown and HTML) made absolute, for text read out of its page (llms-full.txt)."""
    base = SITE + url

    def fix(target):
        return target if re.match(r"[a-z][a-z0-9+.-]*:|#", target) else urljoin(base, target)

    text = re.sub(r"\]\(([^)\s]+)", lambda m: "](" + fix(m.group(1)), text)
    return re.sub(r'(href|src)="([^"]+)"', lambda m: f'{m.group(1)}="{fix(m.group(2))}"', text)


def write_markdown_and_llms():
    """The Markdown source of every page next to its HTML page, and llms.txt / llms-full.txt (llmstxt.org)."""
    for page in PAGES:
        dest = os.path.join(STATIC, md_url(page["url"]).lstrip("/"))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(markdown_page(page))

    home = next(p for p in PAGES if p["rel"] == "index.md")
    guides = sorted((p for p in PAGES if p["rel"].startswith("docs/")), key=lambda p: (p["weight"], p["title"]))
    refs = [p for p in PAGES if p["rel"] in (
        "API_docs/index.md", "API_docs/methods/index.md", "API_docs/constructors/index.md", "API_docs/types/index.md",
        "PHP/index.md",
    )]

    def entry(p):
        return f"- [{p['title']}]({SITE}{md_url(p['url'])})" + (f": {p['description']}" if p["description"] else "") + "\n"

    llms = (
        f"# MadelineProto\n\n> {home['description']}\n\n"
        f"MadelineProto's documentation. Every page is also available as Markdown: replace `.html` with `.md` in its "
        f"URL (e.g. {SITE}/docs/FILES.md for {SITE}/docs/FILES.html).\n\n"
        f"## Docs\n\n- [{home['title']}]({SITE}{md_url(home['url'])}): {home['description']}\n"
        + "".join(entry(p) for p in guides)
        + "\n## API reference\n\nThe Telegram API reference (every method, constructor and type) and the PHP API "
        "reference (every class of MadelineProto), as indexes linking to each page.\n\n"
        + "".join(entry(p) for p in refs)
        + f"\n## Optional\n\n- [Full text of the docs]({SITE}/llms-full.txt): every page of the Docs section above, "
        "in one file\n"
    )
    with open(os.path.join(STATIC, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms)
    full = "".join(
        f"\n\n---\n\nSource: {SITE}{p['url']}\n\n" + absolute_links(markdown_page(p), p["url"])
        for p in [home] + guides
    )
    with open(os.path.join(STATIC, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write(f"# MadelineProto\n\n> {home['description']}" + full)


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
        PAGES.append({"rel": rel + "/index.md", "url": fm["url"], "title": fm["title"], "description": "",
                      "weight": 10**6, "body": body})


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
    write_markdown_and_llms()
    print(f"Converted {count} pages")


if __name__ == "__main__":
    main()
