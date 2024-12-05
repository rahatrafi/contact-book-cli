# Import necessary module and file
import csv
from file_manager import manage_file

def add_contact():
    reader = manage_file()  # To catch the file data
    try:
        phone = input("Enter phone number: ").strip()
        is_num = int(phone)  # Check if the phone number is numeric to handle error

        for each_contact in reader:  # Loop to check the duplicate phone number
            if each_contact['Phone'] == phone:
                print("This phone number already exists. Please try a different one.")
                return

        contact = {
            'Name': input('Enter name: ').title().strip(),
            'Email': input('Enter email address: '),
            'Phone': phone,
            'Address': input('Enter address: ')
        }
        print("New contact added successfully!")

        with open('contact_book.csv', 'a', newline='') as file:  # Adding the new contact
            writer = csv.DictWriter(file, fieldnames=['Name', 'Email', 'Phone', 'Address'])
            writer.writerow(contact)

    except Exception as e:
        print("Oops! Invalid phone number. Only digits are allowed. Please try again.")