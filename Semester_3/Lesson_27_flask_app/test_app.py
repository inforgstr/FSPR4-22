import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.join(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "myDB.db")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), index=True, unique=True)
    author_name = db.Column(db.String(50), index=True, unique=True)
    month = db.Column(db.String(20), index=True, unique=True)
    year = db.Column(db.Integer, index=True, unique=True)
    reviews = db.relationship(
        "Review",
        backref="book",
        lazy="dynamic",
        cascade="all, delete, delete-orphan",
    )

    def __repr__(self):
        return f"{self.title} - {self.author}"


class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    surname = db.Column(db.String(80), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))

    def __repr__(self):
        return f"Reader ID: {self.id}, email: {self.email}"


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, unique=True)
    text = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return f"Reviewer ID: {self.id}, stars: {self.stars}"


class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(20), unique=True)

    def __repr__(self):
        return f"Annotation {self.text}"


with app.app_context():
    db.create_all()
