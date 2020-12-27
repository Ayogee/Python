# The get_login_name function acceps a first name,
# last name, and ID number as arguments.  It returns
# a system login name.

def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name.
    # If name is less than 3 characters, the slice
    # will return the entire first name.
    set1 = first[0:3]
    
    # Get the first three letters of the last name.
    # If name is less than 3 characters, the slice
    # will return the entire last name.
    set2 = last[0:3]
    
    # Get the first three characters of the student ID.
    # If the ID number is less than 3 characters, the 
    # slice will return the entire ID number.
    set3 = idnumber[-3:]
    
    # Put the sets of characters together.
    login_name = set1 + set2 + set3
    
    # Return the login name.
    return login_name
