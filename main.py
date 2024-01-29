def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except KeyError:
            return "There is no such contact"
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Enter user name"
    return wrapper

@input_error
def add_contact(contacts, name, phone):
    if not name or not phone:
        raise ValueError("Give me name and phone please")
    contacts[name] = phone
    return f"Contact {name} added"

@input_error
def change_contact(contacts, name, phone):
    if not name or not phone:
        raise ValueError("Give me name and phone please")
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Contact {name} updated"

@input_error
def show_phone(contacts, name):
    if name not in contacts:
        raise KeyError
    return contacts[name]

@input_error
def show_all_contacts(contacts):
    if not contacts:
        return "Contact list is empty"
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    while True:
        user_input = input(">").lower()
        command = user_input.split()[0]

        if command == "hello":
            print("How can I help you?")
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == "add":
            _, name, phone = (user_input.split() + [None, None])[:3]
            print(add_contact(contacts, name, phone))
        elif command == "change":
            _, name, phone = (user_input.split() + [None, None])[:3]
            print(change_contact(contacts, name, phone))
        elif command == "phone":
            _, name = (user_input.split() + [None])[:2]
            print(show_phone(contacts, name))
        elif user_input == "show all":
            print(show_all_contacts(contacts))
        else:
            print("Unknown command or wrong format")

if __name__ == "__main__":
    main()
