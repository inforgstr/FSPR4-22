"""
https://ycombinator.com/
"""
import json
import requests
import time
import logging

from bs4 import BeautifulSoup
from pathlib import Path
from functools import wraps
from datetime import datetime


# time_counter decorator for counting time
def time_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(
            f"\n#######[TIME-RATE]####### {func.__name__} completed in {time.perf_counter()-start:8f} seconds.\n"
        )
        return result

    return wrapper


# logger decorator for presenting information about https
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(
            format=f"#-------[INFO]#######[{func.__name__}]-------# %(funcName)s %(asctime)s %(message)s",
            level=logging.DEBUG,
        )
        return func(*args, **kwargs)

    return wrapper


@logger
def api_check(url: str) -> BeautifulSoup:
    """
    Returns soup object if url is valid otherwise exception
    """
    try:
        response_txt = requests.get(url).text
        soup = BeautifulSoup(response_txt, "html.parser")
    except Exception as error:
        raise error

    return soup


def get_api_data(soup: BeautifulSoup) -> tuple | Exception:
    """
    Returns tuple of titles_link (titles and links) and score (points) of article
    """
    news_data = []

    try:
        titles_link = soup.select(
            ".titleline"
        )  # getting all tags with class called titleline
        score_parents = soup.select(".subtext")

        for id, title in enumerate(titles_link):
            if score := score_parents[id].find(class_="score"):
                news_data.append(
                    {
                        "title": title.a.text,
                        "link_to_article": title.a["href"],
                        "score": int(score.string.split()[0]),
                    }
                )
            else:
                news_data.append(
                    {
                        "title": title.a.text,
                        "link_to_article": title.a["href"],
                        "score": 0,
                    }
                )
    except AttributeError as error:
        raise error

    return news_data


def write_json(dictionary: dict | list) -> str | Exception:
    """
    Write dictionary data to json file
    """
    try:
        path = Path(__file__).parent / "data.json"
        written_time = datetime.now().strftime("%d day, %m month, %Y - %H:%M")

        dictionary = {
            "last update": written_time,
            "data": dictionary,
        }

        with open(path, "w") as json_file:
            json.dump(dictionary, json_file, indent=4)
    except FileNotFoundError as error:
        raise error


@time_counter
def get_ycombinator_news(url: str, pages: int = 10) -> list[dict] | dict:
    """
    Returns all hacker news from hacker https://news.ycombinator.com/ by sorting their score
    """
    ycombinator_news = []

    for i in range(1, pages + 1):
        try:
            soup = api_check(url + f"?p={i}")
            news_data = get_api_data(soup)
            ycombinator_news.extend(news_data)
        except TypeError as error:
            return error

    sorted_news = sorted(
        ycombinator_news, key=lambda dictionary: dictionary["score"], reverse=True
    )

    return sorted_news


def main(prompt):
    url = "https://news.ycombinator.com/"
    news = get_ycombinator_news(url, prompt)

    write_json(news)
    print("Completed!", f"Written {len(news)} articles.")


if __name__ == "__main__":
    prompt = int(input("How many pages do you want to save? "))
    main(prompt)
