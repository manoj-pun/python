# Build a simple phonebook using a dictionary. Write functions: add_contact(book, name,
# number), remove_contact(book, name), lookup(book, name) that prints a friendly message if not
# found, and list_all(book) that prints all contacts sorted alphabetically by name.

phonebook = {}

def add_contact(book, name, number):
    book[name] = number
    print(f"{name} added successfully.")

def remove_contact(book, name):
    if name in book:
        del book[name]
        print(f"{name} removed successfully.")
    else:
        print(f"{name} not found.")

def lookup(book, name):
    if name in book:
        print(f"{name}'s number is {book[name]}")
    else:
        print(f"{name} not found in phonebook.")

def list_all(book):
    if not book:
        print("Phonebook is empty.")
        return
    
    for name in sorted(book):
        print(f"{name}: {book[name]}")


# add_contact(phonebook, "Alice", "9841111111")
# add_contact(phonebook, "Bob", "9802222222")
# add_contact(phonebook, "Charlie", "9813333333")

# lookup(phonebook, "Bob")

# list_all(phonebook)

# remove_contact(phonebook, "Alice")

# list_all(phonebook)