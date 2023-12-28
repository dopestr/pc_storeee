from .models import Users, InputUser, UserGroup
from db_manager import base_manager

def get_user():
    res = base_manager.execute("SELECT id, username, email, password  FROM Users")
    print(res)
    return Users(id=res["id"], username=res["username"], email=res["email"],password=res["password"],)

def add_user(new_users: InputUser):
    res = base_manager.execute("INSERT INTO Users(id, username, email, password)"
                               " VALUES (?, ?, ?, ?, ?)"
                               "RETURNING id", args=(new_users.user_id, new_users.username, new_users.email, new_users.password))
    return UserGroup(code=res['code'], id=res['data'][0][0])


def update_user(users_id: int, users: Users):
    res = base_manager.execute("UPDATE Users SET username = ?, email = ?, password = ? WHERE id = ?",
                               args=(users.username, users.email, users.password))
    return UserGroup(code=res['code'], id=users_id)


def delete_user(users_id: int):
    res = base_manager.execute("DELETE FROM users WHERE id = ?",
                               args=(users_id,))
    return UserGroup(code=res['code'], id=users_id)