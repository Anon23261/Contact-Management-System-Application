contacts = []

def add_contact(name, phone, email):
contact = {
"name": name,
"phone": phone,
"email": email
}
contacts.append(contact)
print(f"Contact {name} added successfully.")

def view_contacts():
if contacts:
print("\nAll Contacts:")
for i, contact in enumerate(contacts, start=1):
print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
else:
print("No contacts found.")

def search_contact(name):
results = [contact for contact in contacts if contact["name"].lower() == name.lower()]
if results:
print("\nSearch Results:")
for contact in results:
print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
else:
print(f"No contact found with the name {name}.")

def delete_contact(name):
global contacts
initial_count = len(contacts)
contacts = [contact for contact in contacts if contact["name"].lower() != name.lower()]
if len(contacts) < initial_count:
print(f"Contact {name} deleted successfully.")
else:
print(f"No contact found with the name {name}.")
