from app.app import app
from settings import DEBUG_MODE

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, use_reloader=DEBUG_MODE, use_debugger=DEBUG_MODE)
