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
    lift_To_Add = str.lower(input("Enter the name of the lift to add: "))
    lifts.append({lift_To_Add: {}})
    print("List of Lifts:")
    for lift in lifts:
        print(f"- {lift}")
    
    return

def remove_Lift_Function():
    lift_To_Remove = str.lower(input("Enter the name of the lift to remove: "))



    for lift in lifts:
        if lift_To_Remove in lift:
            if str.lower(input("Are you sure?: ")) == "yes":
                lifts.remove(lift)
                print(f"{lift_To_Remove} has been removed from the list.")
            else:
                print(f"{lift_To_Remove} has not been removed")
            return
    print(f"{lift_To_Remove} is not in the list")

def list_lifts_Function():\
    
    if len(lifts) == 0:
        print("No lifts in the list.")
        return

    print("List of Lifts:")
    for lift in lifts:
        print(f"- {lift}")


# Edit functions

def edit_Lift_Logic(lift: dict):
    print("Enter 'edit help' for a list of helpful edit commands")
    editing = True
    while editing:
        edit_Input = str.lower(input("What would you like to do?: "))
    
        if edit_Input == "edit help":
            print("Available edit commands:")
            for command in edit_Commands:
                print(f"- {command}: {edit_Commands[command][1]}")
            continue
            
            

        if edit_Input in edit_Commands:
            if edit_Input == "add":
                edit_Commands[edit_Input][0](lift)
            elif edit_Input == "exit":
                print("Exiting edit process...")
                return
            else:
                edit_Commands[edit_Input][0]() 
        else:
            print("Unknown command. Enter 'edit help' for a list of helpful commands")
            continue

        

    
    
    

def edit_Lift_Function():
    lift_Input = str.lower(input("Enter the name of the lift to edit: "))
    for lift in lifts:
        if lift_Input in lift:   
            lift_To_Edit = lift
            edit_Lift_Logic(lift_To_Edit)
            return
    print("Lift not found, please try again.")

def edit_Add_Function(lift: dict):
    lift_Name = next(iter(lift))
    print("Type 'options' to view the available options to add")
    adding = True
    while adding:

        options = {
            "string": "A sentence or text",
            "integer": "A whole number",
            "float": "A number with decimals",
        }

        
        print(f"-- Currently Editing: {lift}")

        choice_Input = str.lower(input("What are you adding?: "))

        if choice_Input == "options":
            for option in options:
                print(f"- {option}: {options[option]}")
            continue
        if choice_Input not in options:
            print("Invalid input, restarting add process")
            continue

        name_Input = input(f"Enter this {choice_Input}'s name: ")
        value_Input = input(f"{name_Input}: ")
        if choice_Input in options:
            if choice_Input == "string":
                lift[lift_Name][name_Input] = value_Input
            elif choice_Input == "integer":
                lift[lift_Name][name_Input] = int(value_Input)
            elif choice_Input == "float":
                lift[lift_Name][name_Input] = float(value_Input)
            else:
                print("Choice not detected as an option, restarting add process.")
                continue
        else:
            print("Choice not in options, restarting add process.")
            continue

        print(f"Successfully added {name_Input} to {lift_Name}")
        if str.lower(input("Would you like to see your lift?: ")) == "yes":
            print(lift)

        if str.lower(input("Would you like to exit the editing process?: ")) == "yes":
            adding = False
            break
        else:
            continue


    return

def edit_Remove_Function():
    print("edit remove")
    return

def edit_Edit_Function():
    print("Edit")
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
edit_Commands = {
    "add": [edit_Add_Function, "This adds something to your lift"],
    "remove": [edit_Remove_Function, "This removes something you added to your lift"],
    "edit": [edit_Edit_Function, "This edits something you added to a lift"],
    "exit": [(), "This exits the editing process"],

}

print("Enter 'help' for a list of helpful commands.")
while True:
    
    user_input = input("> ").strip().lower()

    if user_input == "exit":
        print("Bye!")
        break

    if user_input in commands:
        commands[user_input][0]()
    else:
        print("Unknown command. Type 'help' for a list of commands.")