from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from backend.models.db import db
from backend.models import User, Product, Order
from backend.config import Config

from backend.routes.product_api import product_api
from backend.routes.user_api import user_api
from backend.routes.order_api import order_api
from backend.routes.analytics_api import analytics_api

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(product_api)
app.register_blueprint(user_api)
app.register_blueprint(order_api)
app.register_blueprint(analytics_api)

if __name__ == "__main__":
    app.run(debug=True)
