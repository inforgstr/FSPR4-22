import random
import string


recipes = {1: "fried egg", 2: "buttered toast"}
types = {1: "Breakfast", 2: "Breakfast"}
descriptions = {1: "Egg fried in butter", 2: "Toasted bread spread with butter"}
ingredients = {
    1: ["1 pad of butter", "1 Egg", "A pinch of salt"],
    2: ["1 pad of salted butter", "1 slice of bread"],
}
instructions = {
    1: {
        "Step 2": "Crack the egg into the buttered pan",
        "Step 5": "Serve egg after about a minute and a half",
        "Step 1": "Melt butter in pan over medium-low heat",
        "Step 4": "Flip egg after about a minute and a half",
        "Step 3": "Sprinke the pinch of salt onto cooking egg",
    },
    2: {
        "Step 3": "Put the pad of butter on the toasted bread",
        "Step 4": "After a minute spread the melted butter onto the bread",
        "Step 1": "Put the bread in the toaster",
        "Step 2": "Take the toast out of the toaster",
    },
}

images = {}

comments = {1: ["Yummy!!", "Egg-cellent ;->"], 2: ["Toasty", "What a great recipe!"]}


def add_ingredients(recipe_id=None, text=None):
    if recipe_id and text:
        text_list = text.strip().split("\n")
        ingredients[recipe_id] = text_list


def add_comments(recipe_id=None, content=None):
    if recipe_id and content:
        content_lst = content.strip().split("\n")
        if recipe_id not in comments:
            comments[recipe_id] = content_lst
        comments[recipe_id].extend(content_lst)


def add_instructions(recipe_id=None, text=None):
    if recipe_id and text:
        text_list = text.strip().split("\n")
        instructions_dict = {}
        for i, instruction in enumerate(text_list):
            instructions_dict["Step {}".format(i + 1)] = instruction

        instructions[recipe_id] = instructions_dict


def add_image(recipe_id=None, path=None):
    if recipe_id and path:
        images[recipe_id] = path


def slug_rand(filename: str) -> str:
    letters = string.ascii_letters + string.digits
    file = "".join(filename.split(".")[:-1])
    ext = "".join(filename.split(".")[-1])
    randomized = file + "".join(random.choice(letters) for x in range(10))
    return randomized + "." + ext
