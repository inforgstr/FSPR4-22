from bs4 import BeautifulSoup
import requests

class RequestError(Exception):
    def __init__(self, message):
        self.message = message

def parse_vox(page_count):
    results = []
    for page in range(1, page_count+1):
        try:
            url = f"https://www.vox.com/technology/archives/{page}"
            res = requests.get(url)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")

            links_titles = soup.select(".c-entry-box--compact__title>a")
            authors = soup.select(".c-byline__author-name")
            dates = soup.find_all("time")
            for links_title, author, date in zip(links_titles, authors, dates):
                results.append(
                    {
                        'title': links_title.text,
                        'link': links_title['href'],
                        'author': author.text,
                        'date': date.text.replace('\n', '')
                    }
                )
        except (requests.RequestException, requests.exceptions.ConnectionError) as err:
            raise RequestError(f'An error occurred during the request: {err}')

    return results

def print_results(pages):
    for page in pages:
        print(f"""
        Title: {page['title']}
        Link: {page['link']}
        Author: {page['author']}
        Date: {page['date']}
        """)


def main():
    pages_count = int(input("Pages count: "))
    try:
        pages = parse_vox(pages_count)
        print_results(pages)
    except RequestError as err:
        print(err)

main()