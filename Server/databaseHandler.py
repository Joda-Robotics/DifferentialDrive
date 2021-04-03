# File to handle database interactions and other account functions

import pymysql
from datetime import datetime

db = pymysql.connect(host="localhost",
                    user="user",
                    password="checkem",
                    database="Joda")

mycur = db.cursor()

def checkUsername(username):
    # Check database to find username
    mycur.execute("SELECT Username FROM users WHERE Username = '"+username+"'")
    user1 = mycur.fetchone()
    if bool(user1) > 0:

        user1 = ''.join(user1)
    if username == user1:
        return True
    else:
        return False

def completeReg(username,password):
    mycur.execute("INSERT INTO users (Username, Password, Created) VALUES (%s,%s,%s)", (username, password, datetime.now()))
    db.commit()

def grabPass(username):
    mycur.execute("SELECT Password FROM users WHERE Username = '"+username+"'")
    grabbed = mycur.fetchone()

    grabbed = ''.join(grabbed)

    return grabbed

def checkPassMatch(Password1, Password2):
    if Password1 == Password2:
        return True
    else:
        return False