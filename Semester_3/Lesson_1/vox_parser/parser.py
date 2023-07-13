import json
import requests
import bs4

from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime


def conn_check(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    except Exception as error:
        raise error


def get_by_article(article: bs4.Tag) -> dict:
    topic = article.find(class_="c-entry-box--compact__labels")
    article_link = article.find(class_="c-entry-box--compact__title").a["href"]
    article_title = article.find(class_="c-entry-box--compact__title").a.string
    topic_title = None
    topic_link = None

    authors = [
        author.string for author in article.find_all(class_="c-byline__author-name")
    ]

    posted_at = datetime.fromisoformat(
        article.select(".c-byline__item.c-byline__item")[-1]["datetime"]
    ).strftime("%Y year, %m month, %d day, at %H:%M")

    data = {
        "authors": authors,
        "article_title": article_title,
        "article_link": article_link,
        "posted_date": posted_at,
    }

    if topic:
        topic_title = topic.span.string
        topic_link = topic.a["href"]

    data.update(
        {
            "topic_title": topic_title,
            "topic_link": topic_link,
        }
    )
    return data


def get_vox_data(soup: BeautifulSoup) -> list | dict:
    news = []

    articles = soup.select(".c-compact-river__entry")
    for article in articles:
        data = get_by_article(article)
        news.append(data)

    return news


def write_json(data: list | dict, page_count: int) -> None:
    try:
        json_path = Path(__file__).parent / "vox-news.json"
        news_data = {
            "last updated": datetime.now().strftime(
                "%Y year, %m month, %d day. At %H:%M"
            ),
            "pages_count": page_count,
            "vox-news": data,
        }

        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(news_data, json_file, indent=4, ensure_ascii=False)

    except FileNotFoundError as error:
        raise error


def get_news_by_paging(url, page_count) -> str:
    vox_news = []

    try:
        for i in range(1, page_count + 1):
            soup = conn_check(f"{url}/{i}")
            news = get_vox_data(soup)
            vox_news.extend(news)

        return vox_news

    except Exception as error:
        raise error


def main(prompt):
    try:
        prompt = int(prompt)
        url = "https://vox.com/technology/archives/"

        news = get_news_by_paging(url, prompt)
        write_json(news, prompt)

        print("Success!")
    except ValueError as error:
        return error


if __name__ == "__main__":
    prompt = input("Count of page(s): ")
    main(prompt)
