# This program compares two strings.
# Get a password from the user.
password = input('Enter the password: ')

# Determine whether the correct password was entered.
if password == 'prospero123':
    print('Password accepted.')
    print('Here is the secret code: XYZ123')
else:
    print('Incorrect password.')