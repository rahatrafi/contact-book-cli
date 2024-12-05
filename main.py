"""

Date: December 4, 2024
Developed by Rahat Rafi

Project: Contact Book Management System
Description:
A simple CLI application for managing a contact book, built with raw Python.
Users can add, view, remove, and search contacts.
Data is saved in a CSV file, ensuring the contact book stays updated after closing.

"""

# Import necessary files
import add
import view
import remove
import search
from file_manager import manage_file

manage_file()  # Check the file to read or create

while True:  # Start the main program and menu loop
    print("\nWelcome to the Contact Book Management System!\n"
          "Please choose an option from the menu:\n"
          "[0] Exit\n"
          "[1] Add\n"
          "[2] View\n"
          "[3] Remove\n"
          "[4] Search")
    option = input("Enter option: ")

    if option == "0":
        print("Exiting the Contact Book Management System. Goodbye!")
        break
    elif option == "1":
        add.add_contact()  # Add a new contact
    elif option == "2":
        view.view_contacts()  # View all contacts
    elif option == "3":
        remove.remove_contact()  # Remove a specific contact
    elif option == "4":
        search.search_contact()  # Search for contact information
    else:
        print("Oops! Invalid choice. Please select an option between 0 and 4.")