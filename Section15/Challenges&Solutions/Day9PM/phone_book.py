"""
File: phone_book.py
-----------------
This program allows the user to store and lookup phone numbers
in a phone book.  They can "add", "lookup" or "quit".
"""
COMMAND_NOT_FOUND_MESSAGE = "This command is not found try again!"

def main():
    phone_book = {}
    print(f"Welcome to Phone Book!  This program stores phone numbers of contacts.  "
          f"You can add a new number, get a number, "
          f"or quit ('add', 'lookup', 'quit').")

    operation = get_input()
    while operation != 'quit':
        result = check_operation(operation, phone_book)
        if result:
            print(result)
        operation = get_input()

def get_input():
    print("Enter your command at the prompt.")
    return input("('add', 'lookup', 'quit') > ")

def check_operation(operation, data):
    if operation == 'lookup':
        return search_from_data(data)
    elif operation == 'add':
        return add_to_data(data)
    elif operation == 'quit':
        return quit()
    else:
        return COMMAND_NOT_FOUND_MESSAGE

def search_from_data(data):
    name = input("name? ")
    if name in data:
        return data[name]
    else:
        return f"{name} not found."

def add_to_data(data):
    name = input("name? ")
    number = input("number? > ")
    data[name] = number
    return None

def quit():
    return 'quit'

if __name__ == '__main__':
    main()