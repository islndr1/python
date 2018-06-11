import os
user = {0: ["admin", "admin", "admin"]}
countUsers = len(user)
standardPassword = "qwerty"
fileBd = "users.txt"

def rewriteBd():
    f = open(fileBd, 'w')
    for i in range(countUsers):
        f.write(str(i) + " " + user[i][0] + " " + user[i][1] + " " + user[i][2] + "\n")
    f.close()

def initBd():
    global countUsers
    OpenFile = True
    try:
        f = open(fileBd, 'r')
    except FileNotFoundError:
        OpenFile = False
    if OpenFile:
        for line in f:
            length = len(line)
            data = []
            j = 0
            temp = ""
            for i in range(length):
                if (line[i] != ' ') and (line[i] != '\n'):
                    temp += line[i]
                else:
                    data.insert(j, temp)
                    temp = ""
                    j += 1
            user[int(data[0])] = [data[1], data[2], data[3]]
        countUsers = len(user)
        f.close()
    else:
        rewriteBd()
    return

def main():
    initBd()
    work = True

    while work:
        print("Menu: ")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = int(input("Your choice: "))
        if choice == 1:
            logIn()
        elif choice == 2:
            register()
        elif choice == 3:
            work = False
        else:
            print("There is no such action.")
            os.system('pause')
    return

def UserMenu(id):
    work = True
    MyId = id
    while work:
        print("You are logged in as an user.(" + user[MyId][0] + ")")
        print("1. Change username")
        print("2. Change password")
        print("3. Logout")
        choice = int(input("Your choice: "))
        if choice == 1:
            changeLogin(MyId)
        elif choice == 2:
            changePassword(MyId)
        elif choice == 3:
            work = False

def AdminMenu(id):
    work = True
    MyId = id
    while work:
        if user[MyId][2] == "user":
            print("You have been reset privileges.")
            os.system('pause')
            return
        print("You are logged in as an administrator.("+user[MyId][0]+")")
        print("1. Create user")
        print("2. Change username")
        print("3. change password")
        print("4. Reset user password")
        print("5. Modify user role")
        print("6. List of all users")
        print("7. Logout")
        choice = int(input("Your choice: "))
        if choice == 1:
            register(True)
        elif choice == 2:
            changeLogin(MyId)
        elif choice == 3:
            changePassword(MyId)
        elif choice == 4:
            resetPassword()
        elif choice == 5:
            changeRole()
        elif choice == 6:
            userslist()
        elif choice == 7:
            work = False

def register(role = False):
    print("New user registration")
    check = True
    default = "user"
    global countUsers

    while check:
        login = input("Enter Login: ")
        check = False
        for i in range(countUsers):
            if login == user[i][0]:
                print("The username is already taken.")
                check = True
                break
            
    if login != '':
        password = input("Enter password: ")
    if role:
        print("Role")
        print("1. Admin")
        print("2. User")
        Choice = int(input("Select role: "))
        if Choice == 1:
            default = "admin"
        else:
            default = "user"
            
    if (login != '') and (password !=''):
        user[countUsers] = [login, password, default]
        countUsers = len(user)
        rewriteBd()
        print("The user successfully registered")
    else:
        print("The entered data is empty")
    os.system('pause')
    return

def userslist():
    print("ID\t\tLogin\t\tPassword\t\tRole")
    for i in range(countUsers):
        print(str(i)+"\t\t"+user[i][0]+"\t\t"+user[i][1]+"\t\t\t"+user[i][2])
    os.system('pause')
    return

def changeLogin(id):
    print("Changing the username")
    check = True
    while check:
        login = input("Enter a new username: ")
        check = False
        for i in range(countUsers):
            if login == user[i][0]:
                print("This username already exists.")
                check = True
                break
    user[id][0] = login
    print("Username changed.")
    rewriteBd()
    os.system('pause')
    return

def changePassword(id):
    print("Changing the password")
    user[id][1] = input("Enter a new password: ")
    print("Password has been changed.")
    rewriteBd()
    os.system('pause')
    return

def resetPassword():
    print("Reset password")
    id = int(input("Enter the user ID: "))
    if (id >= countUsers) and (id < 0):
        print("This ID is missing.")
    else:
        user[id][1] = standardPassword
        print("The password was reset.")
        rewriteBd()
    os.system('pause')
    return

def changeRole():
    print("To reassign a user role")
    id = int(input("Enter the user ID: "))
    if (id >= countUsers) and (id < 0):
        print("This ID is missing.")
    else:
        print("Role")
        print("1. Admin")
        print("2. User")
        Choice = int(input("Select role: "))
        default = "user"
        if Choice == 1:
            default = "admin"
        user[id][2] = default
        print(user[id][0] + " changed to " + user[id][2])
        rewriteBd()
        os.system('pause')
    return

def logIn():
    print("Login")
    login = input("Enter your username: ")
    password = input("Enter your password: ")
    for i in range(countUsers):
        if (login == user[i][0]) and (password == user[i][1]):
            print(" ")
            if user[i][2] == "admin":
                AdminMenu(i)
            else:
                UserMenu(i)
            return
    print("Login / password entered incorrectly.")
    os.system('pause')
    return

main()
