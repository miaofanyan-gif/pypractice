from flask import Flask
from app.extensions.db import db
from app.api import user_bp
from config.production import ProdutionConfig
from config.development import DevelopmentConfig
import os


def create_app(env="development"):
    print(555)
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    config = {'development': DevelopmentConfig, 'production': ProdutionConfig}

    app.config.from_object(config[env])

    db.init_app(app)
    return app
