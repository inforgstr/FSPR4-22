import json
import os
import datetime

from pathlib import Path


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

        except (TypeError, KeyError):
            continue
    # sorting with sorted function, that makes sortlist with most similtar value
    similarities = sorted(similarities, key=lambda x: x[1]["published"])

    # sorting for all similar posts
    result = [x[1] for x in sorted(similarities, key=lambda x: x[0], reverse=True)]

    # rewriting date into string, avoid JSON erros
    for x in result:
        x["published"] = str(x["published"])

    try:
        # create base variable to set path to main directory
        base = Path(__file__).resolve().parent.parent

        # check if path is available
        try:
            os.mkdir("%s/results/" % base)
        except (OSError, FileExistsError):
            pass

        # saving result into json file
        with open("%s/results/file.json" % base, "w") as file:
            json.dump(result, file, indent=4)

    except TypeError as te:
        return (
            "Please check your dictionary data, once you change it into string.\nException: %s"
            % te
        )

    # If result not empty
    if result:
        # If there are results, print the count and the first tag
        print("Have found %s on %s tag:\n" % (len(result), result[0]["tags"][0]))


        for res in result:
            # Extract the relevant information from each result
            title = res["title"]
            tag = res["tags"][1]
            published_date = res["published"]

            # Extract the relevant information from each result
            s = f"\t- {title}"
            c = "_" * (len(s) + 3)


            # Print the formatted result with title, tag, published date, and separator line
            print(f"{s}\n\t\t- {tag} - {published_date}\n\t{c}")
    else:
        print("No such results for each tags.")
