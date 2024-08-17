import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    save_contacts(contacts)
    print(f"Contact for {name} added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. {contact['name']} - {contact['phone']}")

def search_contacts(contacts):
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

def update_contact(contacts):
    search_term = input("Enter name or phone number of the contact to update: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            save_contacts(contacts)
            print("Contact updated.")
            return
    print("No matching contact found.")

def delete_contact(contacts):
    search_term = input("Enter name or phone number of the contact to delete: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted.")
            return
    print("No matching contact found.")

def main():
    contacts = load_contacts()
    print("Contact Book Application")

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Select an option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
