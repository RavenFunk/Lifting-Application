## Lifting Application

# Lists

lifts = [

]


# Functions

def help_Function():
    print("Available commands:")
    for command in commands:
        print(f"- {command}: {commands[command][1]}")

def exit_Function():
    # Exits the program
    return

def add_Lift_Function():
    lift_To_Add = input("Enter the name of the lift to add: ")
    lifts.append({"name": lift_To_Add})
    print("List of Lifts:")
    for lift in lifts:
        print(f"- {lift['name']}")
    
    return

def remove_Lift_Function():
    lift_To_Remove = input("Enter the name of the lift to remove: ")
    if lift_To_Remove in lifts["name"]:
        lifts.remove(lift_To_Remove)
        print(f"{lift_To_Remove} has been removed from the list.")
    else:
        print(f"{lift_To_Remove} is not in the list.")
    return

def list_lifts_Function():
    if len(lifts) == 0:
        print("No lifts in the list.")
        return
    else:
        print("List of Lifts:")
        for lift in lifts:
            print(f"- {lift}")

def edit_Lift_Function():

    return


# Commands
commands = {
    "help": [help_Function, "This displays the list of available commands"],
    "exit": [exit_Function, "Exits the application"],
    "add lift": [add_Lift_Function, "This adds a new lift to the list"],
    "remove lift": [remove_Lift_Function, "This removes a lift from the list"],
    "list lifts": [list_lifts_Function, "This displays the list of lifts"],
    "edit lift": [edit_Lift_Function, "This lets you edit properties your lifts"]
}

print("Enter 'help' for a list of helpful commands.")
while True:
    
    user_input = input("> ")

    if user_input in commands:
        commands[user_input][0]()
    else:
        print("Unknown command. Type 'help' for a list of commands.")