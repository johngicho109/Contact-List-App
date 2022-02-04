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
    pass

if __name__ == "__main__":
    main()

