from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    request,
    send_from_directory,
)
from pathlib import Path

from data import (
    recipes,
    types,
    descriptions,
    ingredients,
    instructions,
    comments,
    images,
)
from data import add_ingredients, add_instructions, add_comments, add_image, slug_rand
from forms import RecipeForm, CommentForm

app = Flask(__name__)
base_dir = Path(__file__).parent

app.secret_key = "my-secret-key"

UPLOAD_FOLDER = base_dir / "media"

ALLOWED_EXTENSIONS = ["txt", "jpeg", "png", "jpg", "gif", "webp"]

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/media/<path:name>/")
def media_path(name):
    return send_from_directory("media", name)


@app.route("/")
def index():
    return render_template("index.html", recipes=recipes, title="Recipes")


@app.route("/create-recipe/", methods=["GET", "POST"])
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        new_id = len(recipes) + 1

        file = request.files["image"]
        if file.filename.split(".")[-1] not in ALLOWED_EXTENSIONS:
            return redirect(url_for("index"))

        filename = file.filename

        if (base_dir / "media" / file.filename).exists():
            filename = slug_rand(file.filename)

        file.save(UPLOAD_FOLDER / filename)
        add_image(new_id, f"/media/{filename}")

        recipes[new_id] = form.recipe.data
        types[new_id] = form.category.data
        descriptions[new_id] = form.description.data
        add_ingredients(new_id, form.ingredients.data)
        add_instructions(new_id, form.instructions.data)
        return redirect(url_for("detail", recipe_id=new_id))
    return render_template("create_recipe.html", form=form, title="Recipe Creation")


@app.route("/<int:recipe_id>/", methods=["GET", "POST"])
def detail(recipe_id):
    form = CommentForm()
    if form.validate_on_submit():
        add_comments(recipe_id, form.body.data)
        return redirect(url_for("detail", recipe_id=recipe_id))

    recipe = recipes.get(recipe_id, "")
    recipe_type = types.get(recipe_id, "")
    description = descriptions.get(recipe_id, "")
    ingredient = ingredients.get(recipe_id, "")
    instruction = instructions.get(recipe_id, "")
    recipe_comments = comments.get(recipe_id, "")
    image_path = images.get(recipe_id, "")
    return render_template(
        "recipe_detail.html",
        recipe=recipe,
        description=description,
        recipe_type=recipe_type,
        ingredient=ingredient,
        instruction=instruction,
        title=recipe.title(),
        comments=recipe_comments,
        form=form,
        image=image_path,
    )
