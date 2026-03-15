# Build a simple login system. Store a dictionary of usernames and passwords. Write a function
# login(username, password) that gives the user 3 attempts. After each failed attempt, print how
# many tries remain. After 3 failures, print 'Account locked'. On success, print 'Welcome,
# username!'.

usernamePasswords = {
    "manoj": "12345",
    "david": "67890"
}

def login(username, password):
    attempts = 3

    while attempts > 0:
        if username in usernamePasswords and usernamePasswords[username] == password:
            print(f"Welcome, {username}!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Try again! {attempts} attempts remaining.")
                username = input("Enter username: ")
                password = input("Enter password: ")
            else:
                print("Account locked")

login("xyz", "12345")



