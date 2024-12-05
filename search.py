# Import necessary file
from file_manager import manage_file

def search_contact():
    reader = manage_file()  # To catch the file data
    name = input("Enter name or letter to search: ").title().strip()
    contact_found = False  # Assuming flag is false

    for each_contact in reader:  # Loop to match the name or first letter
        if each_contact['Name'] == name or each_contact['Name'][:1] == name[:1]:
            print(f"\nName: {each_contact['Name']}\n"
                  f"Phone number: {each_contact['Phone']}\n"
                  f"Email address: {each_contact['Email']}\n"
                  f"Address: {each_contact['Address']}")
            contact_found = True  # Change flag to true

    if not contact_found:
        print("No contact matched your search. Please try again.")