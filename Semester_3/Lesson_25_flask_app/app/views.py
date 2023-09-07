from flask import render_template, url_for, redirect

from app.app import app
from app.models import pets


@app.template_filter("pluralize")
def pluralize_string(string: str) -> str:
    try:
        number = int(string)
        if number == 0 or number > 1:
            return "s"
        return ""
    except ValueError:
        return ""


@app.route("/")
def index():
    return render_template("index.html", categories=pets.keys())


@app.route("/animals/<animal_type>/")
def pet_list(animal_type):
    pet_type = pets.get(animal_type)

    if pet_type is None:
        return redirect(url_for("index"))

    context = {
        "pets": pet_type,
        "pets_type": animal_type,
    }

    return render_template("pet_list.html", data=context)


@app.route("/animals/<animal_type>/<animal_name>/")
def pet_detail(animal_type, animal_name):
    detail = list(
        filter(lambda pet: pet["name"] == animal_name, pets.get(animal_type, ""))
    )

    if not detail:
        return redirect(url_for("index"))

    context = {
        "pets_type": animal_type,
        "pet_detail": detail[0],
    }

    return render_template("pet_detail.html", data=context)
