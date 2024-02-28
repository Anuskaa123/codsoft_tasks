class Contact:
    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, address, email):
        new_contact = Contact(name, phone, address, email)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_query):
        found_contacts = [contact for contact in self.contacts if search_query.lower() in contact.name.lower() or search_query in contact.phone]
        if not found_contacts:
            print("No contacts found.")
            return
        for contact in found_contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Address: {contact.address}, Email: {contact.email}")

    def update_contact(self, name, new_phone=None, new_address=None, new_email=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_phone:
                    contact.phone = new_phone
                if new_address:
                    contact.address = new_address
                if new_email:
                    contact.email = new_email
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

def main():
    book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, address, email)
        elif choice == "2":
            book.list_contacts()
        elif choice == "3":
            search_query = input("Enter name or phone number to search: ")
            book.search_contact(search_query)
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number (or press Enter to skip): ")
            new_address = input("Enter new address (or press Enter to skip): ")
            new_email = input("Enter new email (or press Enter to skip): ")
            book.update_contact(name, new_phone or None, new_address or None, new_email or None)
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            book.delete_contact(name)
        elif choice == "6":
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()