import hashlib # For hashing passwords
import getpass # For securely getting user input

password_manager = {} # store the key values pairs of username/hashed password

def create_account(): 
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ") # use the getpass library to hide password input
    hashed_password = hashlib.sha256(password.encode()).hexdigest() # hash the password using SHA-256
    password_manager[username] = hashed_password
    print("Account created successfully.")

def login(): # now we create the login function 
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password: # checks if given username+password exists
        print("Login successful!")
    else:
        print("Invalid username or password")

# Now we create a menu to pick either function 1 or 2

def main():
    while True: # While this is true, we prompt the different choices
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            print("Goodbye !")
            break
        else:
            print("Invalid choice.")
    print(choice)

if __name__ == "__main__": # helps to import that script as a 'library' in other scripts 
    main()
