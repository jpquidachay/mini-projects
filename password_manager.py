from cryptography.fernet import Fernet


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input(f"What is your master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

# Function to create key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(
                f"User: {user} | Password: {fer.decrypt(passw.encode())}")


def add():
    name = input(f"Account Name: ")
    pwd = input(f"Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")


while True:
    mode = input(
        f"Would you like to add a new password, view existing ones, or quit? ('view' or 'add' or 'q' to quit): ")

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print(f"Invalid mode.")
        continue
