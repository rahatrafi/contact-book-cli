# Import necessary modules
import os
import csv

def manage_file():
    if os.path.exists('contact_book.csv'):  # Check if the file exists
        with open('contact_book.csv', mode='r', newline='') as file:  # Reading the existing data
            reader = list(csv.DictReader(file))  # Convert data into a list
        return reader

    else:
        with open('contact_book.csv', mode='w', newline='') as file:  # Creating a new csv file
            fieldnames = ['Name', 'Email', 'Phone', 'Address']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()