import json
import bs4
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime


def set_driver_chrome(url: str) -> webdriver.Chrome:
    """
    Set up chrome driver
    """
    try:
        driver = webdriver.Chrome()

        driver.get(url)

        return driver
    except Exception as error:
        raise error


def get_single_article_data(article: bs4.Tag) -> dict:
    """
    Get full data of single article
    """
    article_title = article.find(attrs={"class": {"_5ncu0TWl"}}).string
    article_title_link = article.find(attrs={"class": {"_5ncu0TWl"}})["href"]
    article_date = article.find(attrs={"class": {"_9u4PrQql", "JJ0p5dnD"}}).string
    article_desctiption = article.find(attrs={"class": {"ULACyEdG"}}).string
    article_author = None
    article_author_role = None

    news = {
        "article_title": article_title,
        "article_date": article_date,
        "article_link": article_title_link,
        "article_desctiption": article_desctiption,
    }

    if article_author := article.find(class_="-GPe57GX Q5lCM4EP xeEyB3Bw"):
        article_author_role = article.select("span")[-1].string
        article_author = article_author.find("a").string

    news.update(
        {
            "article_author": article_author,
            "article_author_role": article_author_role,
        }
    )

    return news


def btn_click(driver: webdriver.Chrome, css_selector: str, count: int) -> None:
    """
    Click button count times by css selector
    """
    for _ in range(count):
        btn = driver.find_element(By.CSS_SELECTOR, css_selector)
        btn.click()
        time.sleep(0.5)


def get_driver_content(link: str, clicks: int) -> BeautifulSoup:
    """
    Get driver's page source
    """
    driver = set_driver_chrome(link)
    btn_click(driver, "._2JA4Lc-M.C4VJiA-U.Z0VHlF-z.auYD2sJm", clicks)

    content = driver.page_source
    driver.close()
    soup = BeautifulSoup(content, "html.parser")
    return soup


def get_forbes_news(links: dict) -> list[dict]:
    """
    Get forbes news by section of links key element
    """
    data = []

    for link, count_click in links.items():
        soup = get_driver_content(link, count_click)

        section_title = soup.find(attrs={"class": {"Bg1Io"}}).string
        articles = soup.find_all(attrs={"class": {"B6j66vzQ"}})

        full_article_data = {
            "section_title": section_title,
            "section_link": link,
            "button_clicks": count_click,
            "section_news": [],
        }

        for article in articles:
            news = get_single_article_data(article)
            full_article_data["section_news"].append(news)

        data.append(full_article_data)

    return data


def json_writer(data: list) -> None:
    """
    Write dict to json file with default path
    """
    path = Path(__file__).parent / "forbes-news.json"

    dictionary = {
        "last_update": datetime.now().strftime("%Y year, %m month, %d day, at %H:%M"),
        "news": data,
    }

    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(dictionary, file, indent=2, ensure_ascii=False)

    except FileNotFoundError as error:
        raise error


def main() -> str:
    try:
        # key: link to section, value: count of button clicks
        forbes_news_links = {
            "https://forbes.com/news": 2,
            "https://forbes.com/money": 3,
            "https://forbes.com/innovation": 5,
            "https://forbes.com/lifestyle": 1,
            "https://forbes.com/worlds-billionaires": 0,
            "https://forbes.com/leadership": 2,
        }
        forbes_news = get_forbes_news(forbes_news_links)
        json_writer(forbes_news)

        print("Success!")
    except ValueError as error:
        return error


if __name__ == "__main__":
    main()
