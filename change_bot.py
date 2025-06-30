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


@input_error
def parse_input(user_input: str):
    parts = user_input.strip().split()
    cmd, *args = parts
    return cmd.lower(), args


@input_error
def add_contact(args, contacts):
    name, phone = args  # ValueError буде автоматично, якщо не 2 аргументи
    contacts[name] = phone
    return f"Contact '{name}' added with phone number '{phone}'."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone  # KeyError буде автоматично, якщо name не існує
    return f"Contact '{name}' updated with new phone number '{phone}'."


@input_error
def show_phone(args, contacts):
    name = args[0]
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

        result = parse_input(user_input)
        if isinstance(result, str):
            print(result)
            continue

        command, args = result

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
