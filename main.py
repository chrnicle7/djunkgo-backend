from flask import Flask
from flask.blueprints import Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from decouple import config

from flask_jwt_extended import JWTManager

import config as app_cfg
import routes

app = Flask(__name__)
api = Api(app)

if config('ENV') == "dev":
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = app_cfg.DB_URL_DEV
else:
    app.debug= False
    app.config["SQLALCHEMY_DATABASE_URI"] = ""
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = app_cfg.JWT_SECRET_KEY

db = SQLAlchemy(app)
jwt = JWTManager(app)
for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run()