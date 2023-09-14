import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.join(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "myDB.db")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class Recipe(db.Model):
    __tablename__ = "recipe"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), index=True)
    recipe_type = db.Column(db.String(50), index=True)
    description = db.Column(db.Text)
    ingredients = db.Column(db.Text)
    instructions = db.Column(db.Text)
    comments = db.relationship(
        "Comment",
        backref="recipe",
        lazy="dynamic",
        cascade="all, delete, delete-orphan",
    )

    def __repr__(self):
        return "%s - type: %s" % (self.title, self.recipe_type)


class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"))
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "%sth recipe - %sth comment" % (self.recipe_id, self.id)


@app.route("/")
def home():
    recipes = Recipe.query.all()
    return render_template("index.html", title="Recipes", recipes=recipes)


@app.route("/recipes/<int:recipe_id>")
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    comments = [x for x in recipe.comments.all()]
    return render_template("recipe_detail.html", recipe=recipe, comments=comments)
