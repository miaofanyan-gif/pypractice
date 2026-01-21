from datetime import datetime
from app.extensions.db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, comment='id')
    username = db.Column(db.String(50), nullable=True,
                         unique=True, comment='username')
    age = db.Column(db.Integer, nullable=False,
                    unique=False, comment='age')
    # password_hash = db.Column(
    #   db.String(255), nullable=False, unique=True, comment='pass has')

    create_time = db.Column(db.DateTime, default=datetime.now,
                            nullable=False, unique=True, comment='time')
 # 核心：定义转字典方法，用于序列化

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
