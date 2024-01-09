class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def update_contact(self, name, phone, email, address):
        contact = self.search_contact(name)
        if contact:
            contact.phone = phone
            contact.email = email
            contact.address = address

    def delete_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)

def main():
    contact_book = ContactBook()
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == 2:
            contact_book.view_contacts()
        elif choice == 3:
            name = input("Enter the name to search: ")
            contact = contact_book.search_contact(name)
            if contact:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("Contact not found")
        elif choice == 4:
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            address = input("Enter the new address: ")
            contact_book.update_contact(name, phone, email, address)
        elif choice == 5:
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == 6:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
