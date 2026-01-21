
from app.models.User import User


class UserService():
    @staticmethod
    def index():
        users = User.query.get(1)

        return {'usename': users.username, "age": users.age, 'create_time': users.create_time}
