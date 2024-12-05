# Import necessary module and file
import csv
from file_manager import manage_file

def remove_contact():
    reader = manage_file()  # To catch the file data
    try:
        phone = input("Enter the phone number to remove: ").strip()
        is_num = int(phone)  # Check if the phone number is numeric to handle error

        for each_contact in reader:  # Loop to match the phone number
            if each_contact['Phone'] == phone:
                reader.remove(each_contact)  # Remove the contact
                print("Contact deleted successfully!")

                with open('contact_book.csv', mode='w', newline='') as file:  # Writing the updated data
                    writer = csv.DictWriter(file, fieldnames=['Name', 'Email', 'Phone', 'Address'])
                    writer.writeheader()
                    writer.writerows(reader)
                return
        print("No such contact exists. Please try again.")

    except Exception as e:
        print("Oops! Invalid phone number. Only digits are allowed. Please try again.")