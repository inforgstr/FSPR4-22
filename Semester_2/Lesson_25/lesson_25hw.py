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
    Find similar data based on tags and dump it into a JSON file.

    Args:
        data: List of dictionaries representing the data.

    Returns:
        A string indicating the status of the function.
    """
    similarities = []

    # Iterate over each dictionary in the data list
    for i in range(len(data)):
        try:
            # Split the tags string into a list and update the dictionary
            data[i]["tags"] = data[i]["tags"].split(", ")

            # Get the list of tags for the current dictionary
            data_tags = data[i]["tags"]

            # Initialize a counter to track the number of similarities
            counter = 0

            # Iterate over each tag in the list of tags
            for tag in range(len(data_tags)):
                # Iterate over each dictionary in the data list, excluding the current dictionary
                for x in data[:i] + data[i + 1 :]:
                    # Check if the current tag is present in the "tags" key of other dictionaries
                    if data_tags[tag] in x["tags"]:
                        counter += 1

                # If there is at least one similarity and it is the last tag in the list,
                # append a tuple with the similarity count and the current dictionary to the similarities list
                if counter >= 1 and tag == len(data_tags) - 1:
                    similarities.append((counter, data[i]))

                # If it is not the last tag, increment the similary quantity
                elif tag < len(data_tags) - 1:
                    counter += 1
        except (TypeError, KeyError):
            continue
    # sorting with sorted function, that makes sortlist with most similtar value
    similarities = sorted(similarities, key=lambda x: x[1]["published"])

    # sorting all dates
    result = [x[1] for x in sorted(similarities, key=lambda x: x[0], reverse=True)]

    # rewriting date into string, avoid JSON erros
    for x in result:
        x["published"] = str(x["published"])

    try:
        # saving result in json file
        with open("file.json", "w") as file:
            json.dump(result, file, indent=4)
    except TypeError as te:
        return (
            "Please check your dictionary data, once you change it into string.\nException: %s"
            % te
        )
    # return Done if the function completed its work correctly
    return "Done!"


print(find_similars(posts))
