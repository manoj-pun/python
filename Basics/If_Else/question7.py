# A user tries to log in. Write if-else logic that prints the correct
# message: - If username is correct AND password is correct → 'Login
# successful' - If username is correct BUT password is wrong → 'Wrong
# password' - If username is wrong → 'User not found' - If account is
# locked (is_locked=True), regardless of credentials → 'Account locked.
# Contact support.' Stored: username='admin' password='secret123'

userusername = "admin"
userpassword = "secret123"
is_locked = False

username = input("Enter the username: ")
password = input("Enter the password: ")

if is_locked:
    print("Account locked. Contact support.")
elif username == userusername and password == userpassword:
    print("Login successful")
elif username == userusername and password != userpassword:
    print("Wrong password")
else:
    print("User not found")