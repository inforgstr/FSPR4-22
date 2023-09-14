import os
import dotenv

from flask import Flask, render_template, url_for

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))

dotenv.load_dotenv(os.path.join(base_dir, ".env"))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "blog.db")
