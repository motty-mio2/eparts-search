import dataclasses
from abc import ABCMeta, abstractmethod

from .item import item
from playwright.sync_api import sync_playwright


@dataclasses.dataclass
class site(metaclass=ABCMeta):
    def _post_init_(self):
        pass

    def _format_text(self, text: str) -> str:
        table = str.maketrans({v: "" for v in ["\u3000", "\n", "\x0c", "\x0b", "\t"]})
        return text.translate(table).strip()

    def _access_page(self, url: str) -> str:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            html = page.content()
            browser.close()  # type:ignore
        return html

    @abstractmethod
    def search(self, keyword: list[str]) -> list[item]:
        pass
