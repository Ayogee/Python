# Use to ask user to enter a year.  Will calculate and display
# the number of days in February that year. (Leap Year)

year = int(input('Enter a year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print('In ', year, ', February has 29 days.')
    else:
        print('In ', year, ', February has 28 days.')
        
elif year % 4 == 0:
    print('In ', year, ', February has 29 days.')
else:
    print('In ', year, ', February has 28 days.)')