def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner


def parse_input(user_input: str):
    parts = user_input.strip().split()
    if not parts:
        raise ValueError("No command entered.")
    cmd, *args = parts
    return cmd.lower(), args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added with phone number '{phone}'."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Contact '{name}' updated with new phone number '{phone}'."


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"


@input_error
def show_all(_, contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{n}: {p}" for n, p in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Available commands: hello, add <username> <phone>, change <username> <phone>, phone <username>, all, exit, close")

    while True:
        user_input = input("Enter a command: ")

        try:
            command, args = parse_input(user_input)
        except ValueError:
            print("Please enter a command.")
            continue

        if command in ("exit", "close"):
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
            continue

        handler = {
            "add": add_contact,
            "change": change_contact,
            "phone": show_phone,
            "all": show_all,
        }.get(command, lambda args, contacts: "Invalid command. Please try again.")

        print(handler(args, contacts))


if __name__ == "__main__":
    main()
