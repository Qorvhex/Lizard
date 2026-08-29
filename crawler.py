#!/usr/bin/env python3
"""
🦎 Qorvhex Lizard - High-Speed Documentation Crawler & Scraper
Author: Qorvhex Team
Telegram: https://t.me/Qorvhex_Channel
"""

import os
import sys
import time
import re
import argparse
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlparse, urldefrag
import requests
from bs4 import BeautifulSoup


class QorvhexLizard:
    def __init__(self, start_url: str, output_file: str = "documentation_full.txt",
                 max_workers: int = 10, restrict_to_path: bool = False, timeout: int = 10):
        self.start_url = start_url
        self.output_file = output_file
        self.max_workers = max_workers
        self.restrict_to_path = restrict_to_path
        self.timeout = timeout

        self.parsed_start = urlparse(start_url)
        self.base_domain = self.parsed_start.netloc
        self.base_path = self.parsed_start.path.rstrip('/')

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=max_workers, pool_maxsize=max_workers)
        self.session.mount('https://', adapter)
        self.session.mount('http://', adapter)

        self.visited_urls = set()
        self.visited_lock = threading.Lock()
        self.file_lock = threading.Lock()
        self.counter_lock = threading.Lock()
        self.page_counter = 0

        self.ignored_extensions = (
            '.png', '.jpg', '.jpeg', '.gif', '.svg', '.pdf',
            '.zip', '.tar', '.gz', '.mp4', '.json', '.xml',
            '.ico', '.webp', '.exe', '.dmg', '.pkg', '.woff', '.woff2', '.ttf'
        )

        self.junk_patterns = [
            "toc", "table-of-contents", "on-this-page", "sidebar", "breadcrumbs",
            "pagination", "feedback", "rating", "menu", "tablist", "tabs",
            "header-nav", "edit-page", "community-links"
        ]

        self.junk_line_exact = {
            "on this page", "in this article", "table of contents",
            "was this page helpful?", "yes", "no", "edit this page",
            "previous", "next", "graphql", "curl", "javascript", "python", "variables"
        }

    def is_valid_url(self, url: str) -> bool:
        """Validate if URL belongs to target domain, path constraint, and has a valid extension."""
        parsed = urlparse(url)
        if parsed.netloc != self.base_domain:
            return False

        if self.restrict_to_path and not parsed.path.startswith(self.base_path):
            return False

        if parsed.path.lower().endswith(self.ignored_extensions):
            return False

        return True

    def extract_clean_content(self, soup: BeautifulSoup) -> str:
        """Strip boilerplate headers, sidebars, navigation, code selectors, and UI noise."""
        for tag in soup(["script", "style", "nav", "footer", "header", "noscript",
                         "aside", "svg", "button", "form", "iframe"]):
            tag.extract()

        for element in soup.find_all(attrs={
            "class": lambda c: c and any(p in " ".join(c).lower() for p in self.junk_patterns)
        }):
            element.extract()

        for element in soup.find_all(attrs={
            "id": lambda i: i and any(p in i.lower() for p in self.junk_patterns)
        }):
            element.extract()

        for element in soup.find_all(attrs={"role": ["tablist", "tab", "navigation"]}):
            element.extract()

        main_content = (
            soup.find("main") or
            soup.find("article") or
            soup.find(class_=lambda c: c and any(w in c.lower() for w in ["content", "markdown", "document", "doc", "body"])) or
            soup.body
        )

        if not main_content:
            return ""

        raw_text = main_content.get_text(separator="\n", strip=True)
        lines = raw_text.splitlines()
        clean_lines = []

        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.lower() in self.junk_line_exact:
                continue
            clean_lines.append(stripped)

        return "\n\n".join(clean_lines)

    def process_page(self, url: str, file_handle) -> list:
        """Fetch, clean, and write document content to file, returning newly discovered links."""
        try:
            response = self.session.get(url, headers=self.headers, timeout=self.timeout)
            if response.status_code != 200 or 'text/html' not in response.headers.get('Content-Type', ''):
                return []

            soup = BeautifulSoup(response.text, "html.parser")

            raw_title = soup.title.string.strip() if soup.title else "Untitled"
            clean_title = re.sub(r'\s*\|.*$', '', raw_title).strip()

            content = self.extract_clean_content(soup)

            if content:
                with self.file_lock:
                    file_handle.write("=" * 80 + "\n")
                    file_handle.write(f"Title / عنوان: {clean_title}\n")
                    file_handle.write(f"URL / آدرس: {url}\n")
                    file_handle.write("=" * 80 + "\n\n")
                    file_handle.write(content + "\n\n\n")
                    file_handle.flush()

            with self.counter_lock:
                self.page_counter += 1
                print(f"[{self.page_counter}] 📄 Scraped: {url}")

            new_links = []
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link['href'])
                clean_url, _ = urldefrag(full_url)
                if self.is_valid_url(clean_url):
                    new_links.append(clean_url)

            return new_links

        except Exception as e:
            print(f"⚠️ Error loading {url}: {e}")
            return []

    def run(self):
        """Execute the crawling routine until all internal documentation links are exhausted."""
        print("=" * 60)
        print("🦎 QORVHEX LIZARD - DOCUMENTATION CRAWLER")
        print(f"🔗 Target URL: {self.start_url}")
        print(f"⚡ Max Workers: {self.max_workers}")
        print(f"📁 Output File: {self.output_file}")
        print(f"🔒 Path Restricted: {self.restrict_to_path}")
        print(f"📢 Telegram: https://t.me/Qorvhex_Channel")
        print("=" * 60 + "\n")

        clean_start_url, _ = urldefrag(self.start_url)
        to_visit = {clean_start_url}
        self.visited_urls.add(clean_start_url)

        start_time = time.time()

        with open(self.output_file, "w", encoding="utf-8") as f:
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                while to_visit:
                    futures = {executor.submit(self.process_page, url, f): url for url in to_visit}
                    to_visit = set()

                    for future in as_completed(futures):
                        discovered_links = future.result()

                        with self.visited_lock:
                            for link in discovered_links:
                                if link not in self.visited_urls:
                                    self.visited_urls.add(link)
                                    to_visit.add(link)

        elapsed = time.time() - start_time
        print("\n" + "=" * 60)
        print(f"🎉 Crawling finished in {elapsed:.2f} seconds!")
        print(f"📊 Total Pages Processed: {self.page_counter}")
        print(f"💾 Output saved to: {self.output_file}")
        print("=" * 60)

        # Trigger Colab file download if running in Google Colab environment
        try:
            import google.colab
            from google.colab import files
            print("📥 Preparing Google Colab auto-download...")
            files.download(self.output_file)
        except (ImportError, ModuleNotFoundError):
            pass


def main():
    parser = argparse.ArgumentParser(
        description="🦎 Qorvhex Lizard: Fast, multithreaded documentation crawler and text extractor."
    )
    parser.add_argument(
        "-u", "--url",
        default="https://docs.railway.com",
        help="Target base documentation URL (e.g. https://docs.railway.com)"
    )
    parser.add_argument(
        "-o", "--output",
        default="documentation_full.txt",
        help="Output text file path (default: documentation_full.txt)"
    )
    parser.add_argument(
        "-w", "--workers",
        type=int,
        default=10,
        help="Number of concurrent worker threads (default: 10, max recommended: 25)"
    )
    parser.add_argument(
        "--restrict-path",
        action="store_true",
        help="Restrict scraping only to subpaths starting with the initial URL path"
    )
    parser.add_argument(
        "-t", "--timeout",
        type=int,
        default=10,
        help="HTTP request timeout in seconds (default: 10)"
    )

    args = parser.parse_args()

    crawler = QorvhexLizard(
        start_url=args.url,
        output_file=args.output,
        max_workers=args.workers,
        restrict_to_path=args.restrict_path,
        timeout=args.timeout
    )
    crawler.run()


if __name__ == "__main__":
    main()
