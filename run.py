from contact import Contact

def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_contact=Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(Contact):
    '''
    Function to save contact
    '''
    Contact.save_contact

def del_contact(Contact):
    '''
    Function to delete a contact
    '''
    Contact.delete_contact

def find_contact(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Contact.find_by_number(number)

def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Contact.contact_exist(number)

def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contact()

def copy_email_clipboard(number):
    """
    Function that returns the email of an existing contact
    """
    return Contact.copy_email(number)

def main():
    print("Welcome to your contact list Application. What is your name?")
    user_name = input()
    print(f"Hello, {user_name}. What would you like us to do for you?")
    print("\n")
    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list, delc - delete contact, cpc - copy contact email to the clipboard ")
        short_code = input().lower()
        if short_code == "cc":
            print("Create New Contact:")
            print("-" * 10)

            print("First Name ...")
            f_name = input()

            print("Last Name ...")
            l_name = input()

            print("Phone Number ...")
            p_number = input()

            print("Email Address ...")
            e_address = input()

            save_contacts(create_contact(f_name,l_name,p_number,e_address))
            print("\n")
            print(f"New Contact {f_name} {l_name} Has Been Created")

        elif short_code == "dc":
            if display_contacts():
                print("Here is youy contact List")
                print("\n")

                for contact in display_contacts():
                    print(f"{contact.first_name} {contact.last_name} ... {contact.phone_number}")
                    print("\n")
            else:
                print("You dont seem to have saved contact in your contact list")
                print("\n")

        elif short_code == "fc":
            print("Enter The number You wish to search for")
            search_number = input()
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print('-' * 10)

                print(f"Phone number.......{search_contact.phone_number}")
                print(f"Email address.......{search_contact.email}")
            else:
                print("That contact does not exist")

        elif short_code == "delc":
            print("Enter The number You wish to delete")
            del_number = input()
            if check_existing_contacts(del_number):
                delete_contact = find_contact(del_number)
                del_contact(delete_contact)
            else:
                print("Contact to delete Not Found.Try again")

        elif short_code == "cpc":
            print("Enter The number You wish to copy its email to the clipboard")
            cp_email_no = input()
            if check_existing_contacts(cp_email_no):
                no_found = find_contact(cp_email_no)
                email_found = copy_email_clipboard(no_found)
                print(f"{email_found}")
            else:
                print("We found no email belong to your contact. Try again")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I dont Understand your command, use the short codes given")

if __name__ == "__main__":
    main()

