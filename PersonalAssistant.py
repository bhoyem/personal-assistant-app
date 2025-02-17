# Give the class a name
class PersonalAssistant:

  # Add an __init__ function here
  def __init__(self, todos, birthdays, contacts):
    # self.contacts = {
    #     'Ann': 'Marketing Coordinator',
    #     'Chelsea': 'Software Developer',
    #     'Nichole': 'Sales Representative',
    #     'Max': 'Technical Writer'
    # }
    self.todos = todos
    self.birthdays = birthdays
    self.contacts = contacts

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todos(self):
    return self.todos

  def get_birthdays(self):
    return self.birthdays

  def get_birthday(self, name):
    if name in self.birthdays:
      return f"{name}'s birthday is on {self.birthdays[name]}."
    else:
      return f"{name}'s birthday is not in the list."

  def add_birthday(self, name, date):
    if name in self.birthdays:
      return f"{name}'s birthday is already in the list."
    else:
      self.birthdays[name] = date
      return print(f"\n{name}'s birthday has been added.")

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return print(f"{name}'s birthday has been removed.")
    # if (name == "Ann"):
    #   return "Birthday is 12/10/12!"
    # elif (name == "Chelsea"):
    #   return 'Birthday is 10/05/77!'
    # elif (name == "Nichole"):
    #   return "Birthday is 05/10/79!"
    # else:
    #   print("Can't find a birthday for this person...")

  # Complete the get_contact function code
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "There's no contact by that name"

  def get_contacts(self):
    return self.contacts

  def add_contact(self, name, job_title):
    if name in self.contacts:
      return f"{name} is already in the contact list."
    else:
      self.contacts[name] = job_title
      return print(f"{name} has been added to the contact list.")

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      return print(f"{name} has been removed from the contact list.")


# Code to test output of the class
# assistant = PersonalAssistant()
# assistant.add_todo("Pick up groceries")
# print(assistant.get_todos())

# Change name to one from your contacts
# print(assistant.get_birthday("Ann"))
# print(assistant.get_contact("Chelsea"))