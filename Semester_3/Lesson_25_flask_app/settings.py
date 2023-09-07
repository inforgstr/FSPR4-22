from dotenv import dotenv_values
from pathlib import Path

from app.app import app

# Define base dir
BASE_DIR = Path(__file__).parent

# Set template and static folder path
app.template_folder = BASE_DIR / "web" / "templates"
app.static_folder = BASE_DIR / "web" / "static"

# Set up flask configurations
flask_config = dotenv_values(BASE_DIR / ".env.secret")

# Debug mode True or False
DEBUG_MODE = True if flask_config.get("FLASK_DEBUG") == "True" else False
