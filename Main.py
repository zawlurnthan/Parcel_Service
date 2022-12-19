# Zaw Than, Student ID:#001368744

from Hash import get_hash
from Truck import check_status

print('\n-----------------------------------------------')
print('The Western Governors University Parcel Service')
print('-----------------------------------------------')


def get_choice():
    """ This function give the instructions to user how to use program and take input as a choice to run program. """
    ch = input("\nEnter a number from 1 to 4 to choose below options:\n"
               "1. To see the status of all packages at a time between 8:35 a.m. and 9:25 a.m.\n"
               "2. To see the status of all packages at a time between 9:35 a.m. and 10:25 a.m.\n"
               "3. To see the status of all packages at a time between 12:03 p.m. and 1:12 p.m.\n"
               "4. To see individual package information.\n")
    return ch


def get_package_info(num):
    """ This function is used to show package info according to user in inquiry. """
    h = get_hash()
    p = h.search(int(num))  # create package from list of the search result.
    note = 'N/A' if not p[0].note else p[0].note
    print(
        f'\nID Number: {p[0].id}\n'
        f'Address: {p[0].address}\n'
        f'City: {p[0].city}\n'
        f'State: {p[0].state}\n'
        f'Postal Code: {p[0].zip}\n'
        f'Deadline: {p[0].deadline}\n'
        f'Weight: {p[0].weight} kg\n'
        f'Note: {note}\n'
        f'Status: {p[0].status}\n')


def get_id_number():
    """ This function is used to get package number. """

    num = int(input("Enter package id from 1 to 40\n"))
    if num < 41 and num > 0:
        get_package_info(num)
    else:
        print('Invalid package number, Try again!')


def get_process(choice):
    """ This function do process of user interface. """

    if choice == '1':
        print('\nStatus of all packages at a time between 8:35 a.m. and 9:25 a.m.')
        print('----------------------------------------------------------------\n')
        check_status(9, 25, 00)

    elif choice == '2':
        print('\nStatus of all packages at a time between 9:35 a.m. and 10:25 a.m.')
        print('-----------------------------------------------------------------\n')
        check_status(10, 25, 00)

    elif choice == '3':
        print('\nStatus of all packages at a time between 12:03 p.m. and 1:12 p.m.')
        print('------------------------------------------------------------------\n')
        check_status(13, 12, 00)

    elif choice == '4':
        get_id_number()

    else:
        print("Invalid entry, try again!")


# Running the user interface in main page.
choice = get_choice()
get_process(choice)
