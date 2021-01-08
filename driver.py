from users import User
from getpass import getpass
import time
from roles import Roles

if __name__ == '__main__':
    user = User()
    user_name = "admin"
    while(True):
        print("Hi! You are logged in  as "+user_name + '\n')
        if(user_name == "admin"):
            val = input(
                " Press 1 to login as another user \n Press 2 for creating New User \n  ")
            if(val == '1'):
                user_name_temp = input("Enter Username:")
                password = getpass("Enter Password for " +
                                   user_name_temp + ": ")
                if(user.check_user_pass(user_name_temp, password) == 0):
                    user_name = user_name_temp

            if(val == '2'):
                new_user = input("Enter Username:")
                new_passwd = getpass("Enter Password for " + new_user + ": ")
                if(user.add_user_details(new_user, new_passwd) == 0):
                    roles_quantity = int(input(
                        "Enter the number of roles to assign to user"))
                    roles = []
                    while(roles_quantity != 0):
                        role_input = input("Enter roles:")
                        roles.append(role_input)
                        roles_quantity = roles_quantity - 1
                    user.assign_roles_users(new_user, roles)

        else:
            val = input(
                "Press 1 to login as another user \nPress 2 for view roles \n Press 3 for access resource \n ")
            if(val == '1'):
                username = input("Enter Username:")
                password = getpass("Enter Password for" + username + ": ")
                user.check_user_pass(username, password)
            if(val == '2'):
                user.get_roles_users(user_name)
            if(val == '3'):
                print("Enter resource and action details")
                resource = input("Enter resource:- ")
                action = input("Enter Action:- ")
                user.has_access(user_name, resource, action)
        exit_var = input("To continue press y or to end the program press n")
        if(exit_var == 'n'):
            break
