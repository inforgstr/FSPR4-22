from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField, FileField
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    recipe_category = [
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
    ]

    image = FileField("Upload recipe image", validators=[DataRequired()])
    recipe = StringField("Recipe name", validators=[DataRequired()])
    category = RadioField(
        "Recipe category", choices=recipe_category, validators=[DataRequired()]
    )
    description = TextAreaField("Recipe description", validators=[DataRequired()])
    ingredients = TextAreaField("Ingredients", validators=[DataRequired()])
    instructions = TextAreaField("Instructions", validators=[DataRequired()])
    submit = SubmitField("Add Recipe")


class CommentForm(FlaskForm):
    body = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Post Comment")
