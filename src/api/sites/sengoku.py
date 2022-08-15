import dataclasses
import pathlib
import re
import sys

from bs4 import BeautifulSoup

sys.path.append(str(pathlib.Path(__file__).parents[1]))

from common.base_site import site
from common.item import item


@dataclasses.dataclass
class sengoku(site):
    def search(self, keyword: list[str]) -> list[item]:
        search_url: str = (
            "https://www.sengoku.co.jp/mod/sgk_cart/search.php?multi="
            + " ".join(keyword)
            + "&search_btn=%E5%95%86%E5%93%81%E6%A4%9C%E7%B4%A2"
        )
        soup = BeautifulSoup(self._access_page(url=search_url), "html.parser")

        x = soup.find_all("td", class_="item_list1_image")[0]
        y = x.find_all("a")[1]
        print(y)

        # ls: list[dict[str, str | int | None]] = []
        ls: list[item] = []
        for i, j, k in zip(
            soup.find_all("td", class_="item_list1_image"),
            soup.find_all("td", class_="item_list1_name"),
            soup.find_all("td", class_="item_list1_detail"),
        ):
            # ls.append(
            #     {
            #         "img": "https://www.sengoku.co.jp" + i.find_all("a")[1].img["src"]
            #         if len(i.find_all("a")) > 1
            #         else None,
            #         "name": self._format_text(j.a.text),
            #         "description": self._format_text(j.find("div", class_="item_list1_description").text),
            #         "price": int(re.search(r"¥(\d*)", j.find("div", class_="item_list1_price").text).group()[1:]),
            #         "link": "https://www.sengoku.co.jp/mod/sgk_cart" + k.div.a["href"][1:],
            #         "available": bool(k.find_all("span")),
            #     }
            # )
            price_base = re.search(r"¥(\d*)", j.find("div", class_="item_list1_price").text)
            if price_base is not None:
                price = int(price_base.group()[1:])
            else:
                price = None

            ls.append(
                item(
                    name=self._format_text(j.a.text),
                    available=bool(k.find_all("span")),
                    description=self._format_text(j.find("div", class_="item_list1_description").text),
                    price=price,
                    link="https://www.sengoku.co.jp/mod/sgk_cart" + k.div.a["href"][1:],
                    img="https://www.sengoku.co.jp" + i.find_all("a")[1].img["src"]
                    if len(i.find_all("a")) > 1
                    else None,
                )
            )
        return ls


# https://www.sengoku.co.jp/mod/sgk_cart/detail.php?code=EEHD-4HW8

if __name__ == "__main__":
    s = sengoku()
    items = s.search(keyword=["raspberry"])
    print(items)
