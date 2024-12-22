import os

from flask import Flask

from src.models.base import db
from src.routes.users import users_bp
from src.routes.posts import posts_bp


def create_app():
    app = Flask(__name__)
    
    # Default configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///:memory:")
    
    db.init_app(app)
    app.register_blueprint(users_bp)
    app.register_blueprint(posts_bp)
    
    return app


def main() -> None:
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
