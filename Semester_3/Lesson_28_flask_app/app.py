from flask import Flask, render_template, url_for
import flask_sqlalchemy


app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:[hn2006]@localhost:5432/Test_flask"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = flask_sqlalchemy.SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), index=True, unique=True)
    author_name = db.Column(db.String(50), index=True, unique=False)
    author_surname = db.Column(db.String(80), index=True, unique=False)
    month = db.Column(db.String(20), index=True, unique=False)
    year = db.Column(db.Integer, index=True, unique=False)
    reviews = db.relationship("Review", backref="book", lazy="dynamic")
    annotations = db.relationship("Annotation", backref="book", lazy="dynamic")

    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month, self.year)


class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=False)
    surname = db.Column(db.String(80), unique=False, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    reviews = db.relationship("Review", backref="reviewer", lazy="dynamic")
    annotations = db.relationship("Annotation", backref="author", lazy="dynamic")

    def __repr__(self):
        return "Reader ID: {}, email: {}".format(self.id, self.email)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, unique=False)
    text = db.Column(db.String(200), unique=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    reviewer_id = db.Column(db.Integer, db.ForeignKey("reader.id"))

    def __repr__(self):
        return "Review ID: {}, {} stars {}".format(self.id, self.stars, self.book_id)


class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), unique=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey("reader.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))

    def __repr__(self):
        return "<Annotation {}-{}:{} >".format(
            self.reviewer_id, self.book_id, self.text
        )

@app.route("/profile/<int:user_id>/")
def profile_detail(user_id):
    profile = Reader.query.get_or_404(user_id)
    reviews = "-".join(str(x) for x in profile.reviews.all())
    ann = "-".join(str(x) for x in profile.annotations.all())
    return f"Profile: <br>name: {profile.name}<br>surname: {profile.surname}<br>email: {profile.email}<br>reviews:{reviews}<br>annotations:{ann}"


@app.route("/books/<year>/")
def book_detail(year):
    book = Book.query.filter_by(year=year).first_or_404()
    reviews = "<br><br>".join(str(x) for x in book.reviews.all())
    ann = "<br><br>".join(str(x) for x in book.annotations.all())
    return f"Book: <br>Title: {book.title}<br>Author name: {book.author_name}<br>month: {book.month}<br>reviews:<br>{reviews}<br>annotations:{ann}"


@app.route("/review/<int:review_id>/")
def reviewer_detail(review_id):
    review = Review.query.get_or_404(review_id)
    book = Book.query.get_or_404(review.book_id)
    reviewer = Reader.query.get_or_404(review.reviewer_id)
    return f"Profile: <br>stars: {review.stars}<br>content: {review.text}<br>Book: {book}<br>reviewer:{reviewer}"
