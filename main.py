#imports PersonalAssistant.py file
from PersonalAssistant import PersonalAssistant
import json

#ADD CODE: open JSON file and pass data to PersonalAssistant class
with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
    todo_list = json.load(todos)
    birthday_list = json.load(birthdays)
    contact_list = json.load(contacts)
    assistant = PersonalAssistant(todo_list, birthday_list, contact_list)

done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    **** Birthdays *****
    4: Get Birthday
    5: Add Birthday
    6: Remove Birthday
    **** Contacts *****
    7: Get a Single Contact
    8: Add a Contact
    9: Delete a Contact

    Select a number or type 'Exit' to quit: 

    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
        
    # Get Birthdays        
    elif user_command == "4":
        print("Your current birthdays:")
        for name in birthday_list:
            print (f"{assistant.get_birthday(name)}")
        user_input = input("Who's birthday do you want to look up? ")
        print(f"\n{assistant.get_birthday(user_input)}")
    # Add someones birthday to the list
    elif user_command == "5":
        name = input("Who's birthday do you want to add? ")
        birthday = input("What is their birthday (use format: mm/dd/yyyy? ")
        assistant.add_birthday(name, birthday)
    # Remove someones birthday from the list
    elif user_command == "6":   
        print("Your current birthdays:")
        for name in birthday_list:
            print (f"{assistant.get_birthday(name)}")
        name = input("Who's birthday do you want to remove?")
        assistant.remove_birthday(name)
        
    # Get Contacts
    elif user_command == "7":
        print("Your current contacts:")
        for name in contact_list:
            print (f"{name}")
        user_input = input("Who's do you want to look up? ")
        print(f"\n{user_input}:{assistant.get_contact(user_input)}")
    # Add Contact
    elif user_command == "8":
        name = input("What is the name of the contact? ")
        job_title = input("What is their job title? ")
        assistant.add_contact(name, job_title)
    # Remove Contact
    elif user_command == "9":
        print("Your current contacts:")
        for name in contact_list:
            print (f"{name}")
        name = input("Who do you want to remove? ")
        assistant.remove_contact(name)

    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# ADD CODE: write data to JSON file
with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
    json.dump(assistant.get_todos(), write_todos)
    json.dump(assistant.get_birthdays(), write_birthdays)
    json.dump(assistant.get_contacts(), write_contacts)