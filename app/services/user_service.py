
from app.models.User import User


class UserService():
    @staticmethod
    def index():
        users = User.query.get(1)

        return users
