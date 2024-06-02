from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''
master_pwd = input("What is the master password? ")
def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user, "| Password:",passw+"\n")
def add():
    name = input("Account name: ")
    pwd = input("Enter password: ")
    with open('passwords.txt','a') as f:        # opening a text file and closing it automatically--> 'a' -> append mode
        f.write(name+"|"+pwd+"\n")
while True:
    mode = input("Would you like to add a new password or view existing ones (view,add)?Enter q for quit ")
    if mode.lower() == "q":
        break
    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()
    else:
        print("Invalid mode.")
        continue