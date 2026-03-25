from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Database configuration (adjust as needed)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tarefas.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Import models so SQLAlchemy registers them
    from models.tarefa_model import Tarefa

    # Create tables
    with app.app_context():
        db.create_all()

    return app