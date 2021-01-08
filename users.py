import time


class User():
    def __init__(self):
        self._users = [{'username': "admin", 'password': "admin"}]
        pass

    def add_user_details(self, username, password):
        if not any(usernames['username'] == username for usernames in self._users):
            self._users.append({'username': username, 'password': password})
            time.sleep(1)
            print("Congrats User Created Successfully")
            print(self._users[1])
        else:
            print("User already exists Please create another user")

    def check_user_pass(self, username, password):
        dict = {'username': username, 'password': password}
        print(dict)
        if dict not in self._users:
            print("Userid or password incorrect Please try again")
            return 1
        else:
            return 0

    def roles
 # def assign_roles_users(self, username, roles):
