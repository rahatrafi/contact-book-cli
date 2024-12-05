# Import necessary file
from file_manager import manage_file

def view_contacts():
    reader = manage_file()  # To catch the file data

    if reader:  # Check the file if empty or not
        for each_contact in reader:  # Loop to show all contacts
            print(f"\nName: {each_contact['Name']}\n"
                  f"Phone number: {each_contact['Phone']}\n"
                  f"Email address: {each_contact['Email']}\n"
                  f"Address: {each_contact['Address']}\n")

    else:
        print("The contact book is empty. Add a new contact to get started!")