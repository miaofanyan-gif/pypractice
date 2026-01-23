from flask import Flask
from app.extensions.db import db
from app.api import user_bp
from config.production import ProdutionConfig
from config.development import DevelopmentConfig
import os


def create_app(env="development"):
 # 获取当前文件（__init__.py）的目录路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 拼接得到templates文件夹的绝对路径（向上回退到项目根目录，再找templates）
    template_dir = os.path.join(os.path.dirname(current_dir), 'templates')
    app = Flask(__name__, template_folder=template_dir)
    app.register_blueprint(user_bp)
    config = {'development': DevelopmentConfig, 'production': ProdutionConfig}

    app.config.from_object(config[env])

    db.init_app(app)
    return app
