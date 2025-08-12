import re
from typing import List, Dict

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from .utils import init_driver

BASE_URL = "https://books.toscrape.com/"


def _parse_rating(element) -> int:
    classes = element.get_attribute("class").split()
    ratings = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    for cls in classes:
        if cls in ratings:
            return ratings[cls]
    return 0


def scrape_books() -> pd.DataFrame:
    """Scrape book data from the Books to Scrape website."""
    print("Iniciando coleta de dados...")
    driver = init_driver()
    driver.get(BASE_URL)
    records: List[Dict] = []
    page = 1

    while True:
        print(f"Coletando dados da página {page}...")
        books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
        for book in books:
            title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
            price_text = book.find_element(By.CSS_SELECTOR, "p.price_color").text
            price = float(re.sub(r"[^0-9.]", "", price_text))
            availability = book.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
            rating = _parse_rating(book.find_element(By.CSS_SELECTOR, "p.star-rating"))
            records.append(
                {
                    "titulo": title,
                    "preco": price,
                    "disponibilidade": availability,
                    "classificacao": rating,
                }
            )
        try:
            next_link = driver.find_element(By.CSS_SELECTOR, "li.next a")
            next_link.click()
            page += 1
        except NoSuchElementException:
            break

    driver.quit()
    print(f"Coleta finalizada. Total de {len(records)} livros coletados.")
    return pd.DataFrame(records)
