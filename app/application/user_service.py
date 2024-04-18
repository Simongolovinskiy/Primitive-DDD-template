from app.domain.entities.user import User


class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, user_id, name, email, age):
        user = User(user_id, name, email, age)
        self.users.append(user)
        return user

    def get_all_users(self):
        return self.users
