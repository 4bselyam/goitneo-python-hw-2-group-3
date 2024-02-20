def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid input provided. Please check your input and try again."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        return "Error: Missing name or phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        return "Error: Missing name or new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: Contact not found."


@input_error
def show_phone(args, contacts):
    if not args:
        return "Error: Missing name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])


def execute_command(command, args, contacts):
    if command in ["close", "exit"]:
        print("Good bye!")
        return False
    elif command == "hello":
        print("How can I help you?")
    elif command == "add":
        print(add_contact(args, contacts))
    elif command == "change":
        print(change_contact(args, contacts))
    elif command == "phone":
        print(show_phone(args, contacts))
    elif command == "all":
        print(show_all(contacts))
    else:
        print("Invalid command.")
    return True


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if not execute_command(command, args, contacts):
            break


if __name__ == "__main__":
    main()
