from users import User
from getpass import getpass
import time

if __name__ == '__main__':
    user = User()
    user_name = "admin"
    while(True):
        print("Hi! You are logged in  as "+user_name + '\n')
        if(user_name == "admin"):
            val = input(
                " Press 1 to login as another user \n Press 2 for creating New User \n Press 3 to edit roles \n ")
            if(val == '1'):
                user_name_temp = input("Enter Username:")
                password = getpass("Enter Password for " +
                                   user_name_temp + ": ")
                if(user.check_user_pass(user_name_temp, password) == 0):
                    user_name = user_name_temp

            if(val == '2'):
                new_user = input("Enter Username:")
                new_passwd = getpass("Enter Password for " + new_user + ": ")
                user.add_user_details(new_user, new_passwd)

        else:
            val = input(
                "Press 1 to login as another user \nPress 2 for view roles \n Press 3 for access resource \n ")
            if(val == '1'):
                username = input("Enter Username:")
                password = getpass("Enter Password for" + username + ": ")
                user.check_user_pass(username, password)
