day = int(input("Enter a number (1-7): "))

if day == 1:
    print('The corresponding day of the week is: Monday.')
elif day == 2:
    print('The corresponding day of the week is: Tuesday.')
elif day == 3:
    print('The corresponding day of the week is: Wednesday.')
elif day == 4:
    print('The corresponding day of the week is: Thursday.')
elif day == 5:
    print('The corresponding day of the week is: Friday.')
elif day == 6:
    print('The corresponding day of the week is: Saturday.')
elif day == 7:
    print('The corresponding day of the week is: Sunday.')
    
else:
    if day < 1 or day > 7:
        print("Error: Please use numeric characters '1-7' only.")