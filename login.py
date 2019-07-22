#login using csv file
import csv
import logging

path = "C:\\Users\\Admin\\Desktop\\python-vijay\\login.csv"
def login():
    username = input("Username :")
    password = input("Password :")
    file = open(path, newline='')
    reader = csv.reader(file)
    header = next(reader)
    data = [l for l in reader]
    for i in data:
        if(i[0] == username):
            if(i[1] == password):
                login = True
                break
            else:
                login = False
        else:
            login = False

    if(login):
        print("\nLogin Successful!!")
    else:
        print("\nInvalid username or password")


def reg():
    username = input("Username :").strip()
    password = input("Password :").strip()
    age = int(input('age :'))
    file = open(path, 'w')
    writer = csv.writer(file)
    if(writer.writerow([username, password, age])):
        print("Register successful!!")
    else:
        print("There is a problem while parsing your request!")

if __name__ == "__main__":
    print("##################### WELCOME #####################\n")
    print("1. Login\n2. Register\n")
    choice=int(input('choice: ').strip())
    if(choice==1):
        login()
    else:
        reg()


