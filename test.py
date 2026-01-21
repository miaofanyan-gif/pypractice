from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
db = SQLAlchemy(app)

print("Flask-SQLAlchemy 初始化成功！")
print(f"版本：{db.__version__}")
