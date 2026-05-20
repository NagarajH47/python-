# Q19. Contact Book Application

contacts = {}

def add_contact(name, number):
    contacts[name] = number

def search_contact(name):
    print(contacts.get(name, "Not Found"))

def delete_contact(name):
    if name in contacts:
        del contacts[name]

def display_contacts():
    print(contacts)

add_contact("Rahul", 9876543210)
search_contact("Rahul")
delete_contact("Rahul")
display_contacts()