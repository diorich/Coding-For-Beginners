import time
users = {}
status = ""

def mainMenu():
    global status
    status = input("Do you have a login account? y/n? Or press q to quit.")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    elif status =="q":
        quit()
    elif status =="r":
        readUsers()

def newUser():
    createLogin = input("Create a login name: ")
    print(users)
    if createLogin in users:
        print("\nLogin name already exists!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created!\n")
        logins=open("logins.txt","a")
        logins.write("\n" + createLogin + " " + createPassw)
        logins.close()

def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    # check if user exists and login matches password
    if login in users and users[login] == passw:
        print("\nLogin Successful!\n")
        print("User:", login, "accessed the system on:", time.asctime())
    else:
        print("\nUser doesn't exist or wrong password!\n")

def readUsers():
    global users
    f = open("logins.txt","r")
    for line in f:
        print(line)

    f.close()

while status !="q":
    status = mainMenu()