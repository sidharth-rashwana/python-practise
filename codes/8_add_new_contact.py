"""
Create a dictionary phone_book to store names and corresponding phone numbers. Implement a function that adds a new contact to the phone book.
"""

phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Eve": "111-222-3333"
}

new_contact_name = input("Enter a name : \n")

new_contact_number = input('Enter contact number : \n')

phone_book[new_contact_name] = new_contact_number

print(phone_book)
