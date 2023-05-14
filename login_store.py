"""Module importing json which would be used to convert the data in store.txt to a dictionary"""
import json

def store_user(username: str, password: str, role: str) -> str:
    """Stores username, password and role of a user
    
    Args:
    username -- username inputed by the user
    password -- password inputed by the user
    role -- user's role

    Return: It does not have a return statement
    """
    details = {"Username":username, "Password":password, "Role":role, "Permission":"read"}
    with open('store.txt', 'w', encoding='utf-8') as login_storer:
        login_storer.write(str(details))
store_user("Delta", "12345", "janitor")

def read_file() ->any:
    """Reads the store.txt file where the user's username and password is kept
    
    Keyword arguments:
    argument -- No argument
    Return: returns the user's login details
    """
    with open('store.txt', 'r', encoding='utf-8') as data:
        file_data = data.read()
    file_data = file_data.replace("'","\"" )
    login_details = json.loads(file_data)
    return login_details

def check_user() ->any:
    """Checks if a user's username and password is accurate
    
    Keyword arguments:
    argument -- No argument
    Return: returns True or False
    """
    username = input("Username: ")
    password = input("Password: ")
    auth_data = read_file()
    access = ('Access Granted' if (auth_data["Username"] == username)
              and (auth_data["Password"] == password) else 'Access Denied')
    return access

def check_role() ->any:
    """Checks the role of a user and returns their permission based on their roles.
    Username ans Password has to be correct befor it returns the permission.
    
    Keyword arguments:
    argument -- No argument
    Return: return user's permission if username and password is correct,
    or returns "Access Denied" if incorrect.
    """
    user_data = read_file()
    user_check = check_user()
    if user_check == 'Access Granted':
        return f"Role: {user_data['Role']} \nPermmissions: {user_data['Permission']}"
    return user_check

print(check_role())
