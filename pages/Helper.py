import csv
import random
from urllib.parse import urlparse

from playwright.sync_api import Page


class Helper:
    def __init__(self, page: Page):
        self.page = page

    def pause(self, ms: int) -> None:
        self.page.wait_for_timeout(ms)

    def get_link_on_csv(self, row_num: int, header: str, csv_path: str = "./test-data/linkFile.csv") -> str:
        with open(csv_path, newline="", encoding="utf-8") as csv_file:
            rows = list(csv.DictReader(csv_file))

        if row_num < 0 or row_num >= len(rows):
            raise IndexError(f"Row index out of range: {row_num}")

        if header not in rows[row_num]:
            raise KeyError(f"Header not found: {header}")

        value = rows[row_num][header]
        if value is None:
            raise ValueError(f"Empty value at row {row_num} for header {header}")

        return value

    def get_random_number(self, min_num: int = 1, max_num: int = 5) -> int:
        return random.randint(min_num, max_num)

    def build_internal_urls(self, paths: list[str]) -> list[str]:
        parsed_url = urlparse(self.page.url)
        origin = f"{parsed_url.scheme}://{parsed_url.netloc}"
        return [f"{origin}{path if path.startswith('/') else f'/{path}'}" for path in paths]

    def verify_urls_api_responses(
        self,
        urls: list[str],
        timeout: int = 15000,
        url_type: str = "URL",
        max_status_code: int = 399,
        disallow_404: bool = False,
    ) -> None:
        for url in urls:
            response = self.page.request.get(url, timeout=timeout)
            status = response.status
            assert status >= 200, f"Expected {url_type} to be reachable: {url} (actual status: {status})"
            assert status <= max_status_code, f"Expected {url_type} to be reachable: {url} (actual status: {status})"
            if disallow_404:
                assert status != 404, f"Expected {url_type} not to be missing: {url} (actual status: {status})"

    def verify_internal_paths_api_responses(self, paths: list[str], timeout: int = 15000) -> None:
        urls = self.build_internal_urls(paths)
        self.verify_urls_api_responses(urls, timeout=timeout, url_type="internal URL")
