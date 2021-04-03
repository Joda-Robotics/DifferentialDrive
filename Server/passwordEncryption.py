#password encryption handler
import bcrypt

def encrypt(Password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(Password.encode(), salt)
    return hashed

def checkpas(Password,storedPassword):
    salt = bcrypt.gensalt()

    if bcrypt.checkpw(Password, storedPassword):
        print("Passwords match")
        return True
    else:
        print("Passwords do not match")
        return False
