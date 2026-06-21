#!/usr/bin/env python3
import html
import json
import re
import sys
import time
from collections import deque
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen


START_URL = "https://yandex.ru/dev/dialogs/alice/doc/ru/"
DOC_BASE_URL = "https://yandex.ru/dev/dialogs/alice/doc/"
ALLOWED_PREFIX = "/dev/dialogs/alice/doc/ru/"
OUT_DIR = Path("docs")
RAW_DIR = OUT_DIR / "raw"
RAW_MD_DIR = OUT_DIR / "raw-md"
AGENT_DOC = OUT_DIR / "alice-skills-agent-docs.md"
INDEX_DOC = OUT_DIR / "source-pages.md"


def normalize_url(url):
    parsed = urlparse(urljoin(DOC_BASE_URL, url))
    if parsed.netloc != "yandex.ru":
        return None
    if parsed.path.startswith("/dev/dialogs/alice/doc/ru/ru/"):
        parsed = parsed._replace(path=parsed.path.replace("/doc/ru/ru/", "/doc/ru/", 1))
    if not parsed.path.startswith(ALLOWED_PREFIX):
        return None
    path = parsed.path
    if path.endswith(".html"):
        path = path[:-5]
    if path.endswith("/index.html"):
        path = path[:-10]
    parsed = parsed._replace(path=path, query="", fragment="")
    return urlunparse(parsed)


def slug_for(url):
    path = urlparse(url).path
    rel = path.removeprefix(ALLOWED_PREFIX).strip("/")
    if not rel:
        return "index"
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", rel).strip("-")


def fetch(url):
    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 documentation crawler for local AI-agent notes",
            "Accept-Language": "ru,en;q=0.9",
        },
    )
    with urlopen(req, timeout=30) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def markdown_url_for(url):
    parsed = urlparse(url)
    if parsed.path.rstrip("/") == ALLOWED_PREFIX.rstrip("/"):
        path = ALLOWED_PREFIX + "index.md"
    else:
        path = parsed.path.rstrip("/") + ".md"
    return urlunparse(parsed._replace(path=path, query="", fragment=""))


def clean_markdown(md):
    md = re.sub(r"^---\n.*?\n---\n", "", md, flags=re.S)
    md = re.sub(r"(?s)<style scoped>.*?</style>\s*", "", md)
    md = re.sub(r"^\{%\s+include\s+notitle\s+\[neuroexpert-button\].*?%\}\s*$", "", md, flags=re.M)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def title_from_markdown(md, fallback):
    match = re.search(r"^#\s+(.+)$", md, re.M)
    if match:
        return match.group(1).strip()
    return fallback


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        attrs = dict(attrs)
        href = attrs.get("href")
        if href:
            self.links.append(href)


class TextParser(HTMLParser):
    block_tags = {
        "p",
        "div",
        "section",
        "article",
        "main",
        "li",
        "tr",
        "table",
        "thead",
        "tbody",
        "ul",
        "ol",
        "pre",
        "blockquote",
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.links = []
        self.skip = 0
        self.in_pre = 0
        self.current_href = None
        self.title = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "title":
            self._newline()
        if tag in {"h1", "h2", "h3", "h4"}:
            self._newline()
            self.parts.append("#" * int(tag[1]) + " ")
        elif tag == "br":
            self._newline()
        elif tag == "pre":
            self.in_pre += 1
            self._newline()
            self.parts.append("```")
            self._newline()
        elif tag == "code" and not self.in_pre:
            self.parts.append("`")
        elif tag == "li":
            self._newline()
            self.parts.append("- ")
        elif tag == "a":
            self.current_href = attrs.get("href")
        elif tag in self.block_tags:
            self._newline()

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag == "pre":
            self._newline()
            self.parts.append("```")
            self._newline()
            self.in_pre = max(0, self.in_pre - 1)
        elif tag == "code" and not self.in_pre:
            self.parts.append("`")
        elif tag == "a":
            self.current_href = None
        elif tag in self.block_tags or tag in {"h1", "h2", "h3", "h4"}:
            self._newline()

    def handle_data(self, data):
        if self.skip:
            return
        text = data if self.in_pre else re.sub(r"\s+", " ", data)
        if not text.strip():
            return
        stripped = text.strip()
        if not self.title and stripped:
            self.title = stripped
        self.parts.append(stripped if not self.in_pre else text.rstrip())
        if self.current_href and stripped:
            self.links.append((stripped, self.current_href))

    def _newline(self):
        if self.parts and self.parts[-1] != "\n":
            self.parts.append("\n")

    def markdown(self):
        text = "".join(self.parts)
        text = html.unescape(text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"^(Да Нет|Была ли статья полезна\\?|Следующая|Предыдущая)$", "", text, flags=re.M)
        return text.strip()


def parse_links(body):
    parser = LinkParser()
    parser.feed(body)
    return parser.links


def parse_text(body):
    parser = TextParser()
    parser.feed(body)
    md = parser.markdown()
    title_match = re.search(r"^#\s+(.+)$", md, re.M)
    title = title_match.group(1).strip() if title_match else (parser.title or "Untitled")
    return title, md


def crawl():
    seen = set()
    queue = deque([START_URL])
    pages = []

    while queue:
        url = normalize_url(queue.popleft())
        if not url or url in seen:
            continue
        seen.add(url)
        print(f"fetch {url}", file=sys.stderr)
        try:
            body = fetch(url)
        except Exception as exc:
            print(f"skip {url}: {exc}", file=sys.stderr)
            continue
        RAW_DIR.mkdir(parents=True, exist_ok=True)
        (RAW_DIR / f"{slug_for(url)}.html").write_text(body, encoding="utf-8")
        fallback_title, fallback_md = parse_text(body)
        if "# 404" in fallback_md[:100] or "Страница не найдена" in fallback_md[:500]:
            continue
        md_url = markdown_url_for(url)
        try:
            raw_md = fetch(md_url)
            RAW_MD_DIR.mkdir(parents=True, exist_ok=True)
            (RAW_MD_DIR / f"{slug_for(url)}.md").write_text(raw_md, encoding="utf-8")
            md = clean_markdown(raw_md)
            title = title_from_markdown(md, fallback_title)
        except Exception as exc:
            print(f"markdown fallback {md_url}: {exc}", file=sys.stderr)
            md = fallback_md
            title = fallback_title
        pages.append({"url": url, "title": title, "markdown": md})
        for href in parse_links(body):
            next_url = normalize_url(href)
            if next_url and next_url not in seen:
                queue.append(next_url)
        time.sleep(0.15)

    return pages


def make_agent_doc(pages):
    by_url = {p["url"]: p for p in pages}
    sections = []
    sections.append("# Документация по навыкам Алисы для ИИ-агентов\n")
    sections.append(
        "Источник: официальная документация Яндекс Диалогов для навыков Алисы. "
        "Этот файл является локальной, агент-ориентированной выжимкой и навигационной картой. "
        "За точными схемами JSON и свежими ограничениями сверяйтесь с исходными страницами.\n"
    )
    sections.append("## Как агенту работать с этой документацией\n")
    sections.append(
        "- Сначала определить тип навыка, пользовательский сценарий, поверхность запуска и требования модерации.\n"
        "- Затем спроектировать сценарий диалога: интенты, состояния, реплики, ошибки распознавания и выход из навыка.\n"
        "- Перед кодом проверить формат webhook-запроса и ответа, ограничения на текст, кнопки, карточки и изображения.\n"
        "- После реализации пройти тестирование, публикацию, аналитику и мониторинг ошибок.\n"
    )
    sections.append("## Карта источников\n")
    for page in pages:
        sections.append(f"- [{page['title']}]({page['url']})\n")

    important = [
        "quickstart",
        "requirements",
        "activation-and-exit",
        "design",
        "before-start",
        "development",
        "request",
        "response",
        "publish",
        "testing",
        "appmetrica",
        "monitoring",
        "faq",
    ]
    sections.append("\n## Агентская сводка по ключевым темам\n")
    for page in pages:
        slug = slug_for(page["url"])
        if any(key in slug for key in important) or page["url"] == START_URL:
            excerpt = page["markdown"]
            excerpt = re.sub(r"\n{2,}", "\n\n", excerpt)
            excerpt = excerpt[:3500].rstrip()
            sections.append(f"\n### {page['title']}\n\nИсточник: {page['url']}\n\n{excerpt}\n")

    sections.append("\n## Полный текст скачанных страниц\n")
    for page in pages:
        sections.append(f"\n---\n\n## {page['title']}\n\nИсточник: {page['url']}\n\n{page['markdown']}\n")
    return "".join(sections).strip() + "\n"


def main():
    pages = crawl()
    pages.sort(key=lambda p: (urlparse(p["url"]).path.count("/"), p["url"]))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    AGENT_DOC.write_text(make_agent_doc(pages), encoding="utf-8")
    INDEX_DOC.write_text(
        "# Скачанные страницы\n\n"
        + "\n".join(f"- [{p['title']}]({p['url']})" for p in pages)
        + "\n",
        encoding="utf-8",
    )
    (OUT_DIR / "crawl-result.json").write_text(
        json.dumps(
            [{"url": p["url"], "title": p["title"], "chars": len(p["markdown"])} for p in pages],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"pages={len(pages)}")
    print(AGENT_DOC)


if __name__ == "__main__":
    main()
