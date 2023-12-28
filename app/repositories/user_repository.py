from app.util.json_util import read_json, write_json

USER_DATA = read_json("data/user_data.json")

class UserRepository():
    def add_user(self, user):
        USER_DATA.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
        write_json("data/user_data.json", USER_DATA)