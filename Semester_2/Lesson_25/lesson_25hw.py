import datetime
import json


posts = [
    {
        "tags": "django, music",
        "title": "Random title",
        "body": "lajksdfjksdf",
        "published": datetime.date(2023, 4, 12),
    },
    {
        "tags": "django, pop",
        "title": "Random title",
        "body": "lajksdfjksdf",
        "published": datetime.date(2022, 4, 12),
    },
    {
        "tags": "django, music",
        "title": "Random title",
        "body": "lajksdfjksdf",
        "published": datetime.date(2021, 4, 12),
    },
    {
        "tags": "django, jazz",
        "title": "Random title",
        "body": "lajksdfjksdf",
        "published": datetime.date(2023, 4, 11),
    },
    {
        "tags": "jazz",
        "title": "Random title",
        "body": "lajksdfjksdf",
        "published": datetime.date(2020, 4, 11),
    },
    {
        "tags": "django, jazz",
        "title": "Random title",
        "body": "lajksdfjksdf",
        "published": datetime.date(2019, 4, 11),
    },
    {
        "tags": "django, django",
        "title": "Random title",
        "body": "lajksdfjksdf",
        "published": datetime.date(2019, 4, 11),
    },
]


def find_similars(data: list[dict]) -> str:
    """
    Args:
        data: int(dict)
    Returns:
        Done if code without exceptions

    Dumps json file all data that filtered with similitaries tags.
    """
    similarity = []

    # sorting by tag
    for i in range(len(data)):
        data[i]["tags"] = data[i]["tags"].split(", ")
        d = data[i]["tags"]
        c = 0
        for tag in range(len(d)):
            for x in data[:i] + data[i + 1 :]:
                if d[tag] in x["tags"]:
                    c += 1

            if c >= 1 and tag == len(d) - 1:
                similarity.append((c, data[i]))

            elif tag < len(d) - 1:
                c += 1

    # sorting with sorted function, that makes sortlist with most similtary value
    similarity = sorted(similarity, key=lambda x: x[1]["published"])

    # sorting with date
    result = [x[1] for x in sorted(similarity, key=lambda x: x[0], reverse=True)]

    # rewriting date into string, avoid JSON erros
    for x in result:
        x["published"] = str(x["published"])


    # saving json file
    with open("file.json", "w") as file:
        json.dump(result, file, indent=4)

    # result
    return "Done!"


print(find_similars(posts))
