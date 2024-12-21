import os

from flask import Flask

from src.models.base import db
from src.routes.users import users_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db.init_app(app)
app.register_blueprint(users_bp)

def main() -> None:
    app.run(host="0.0.0.0", port=5000, debug=True)
