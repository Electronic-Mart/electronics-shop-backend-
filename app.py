from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.models.db import db
from backend.models import User, Product, Order
from flask_migrate import Migrate
from backend.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(debug=True)