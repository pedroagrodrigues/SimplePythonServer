#Model file should take care of the object representation and data management
users = [{"username" : "pedro", "password" : "123"}, {"username":"dale", "password": "123"}]

def checkUser(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False
