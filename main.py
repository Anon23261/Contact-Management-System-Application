import contact_manager

def display_menu():
print("\nContact Management System")
print("1. Add Contact")
print("2. View All Contacts")
print("3. Search for Contact")
print("4. Delete Contact")
print("5. Exit")

def main():
while True:
display_menu()
try:
choice = int(input("Choose an option (1-5): "))
if choice == 1:
name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")
contact_manager.add_contact(name, phone, email)
elif choice == 2:
contact_manager.view_contacts()
elif choice == 3:
name = input("Enter name to search: ")
contact_manager.search_contact(name)
elif choice == 4:
name = input("Enter name to delete: ")
contact_manager.delete_contact(name)
elif choice == 5:
print("Exiting the Contact Management System. Goodbye!")
break
else:
print("Invalid choice. Please choose a number between 1 and 5.")
except ValueError:
print("Invalid input. Please enter a valid number.")

if name == "main":
main()


