# Use to ask user a pocket number in roulette and display pocket color.

pocket = int(input('Enter the pocket number: '))

if pocket == 0:
    print('The pocket is green.')

# Even    
elif pocket >= 1 and pocket <= 10 or pocket >= 19 and pocket <= 28 and pocket % 2 == 0:
    print('The pocket is black.')
    
# Even
elif pocket >= 11 and pocket <= 18 or pocket >= 29 and pocket <= 36 and pocket % 2 == 0:
    print('The pocket is red.')

# Odd 
elif pocket >= 1 and pocket <= 10 or pocket >= 19 and pocket <= 28:
    print('The pocket is red.')  
    
# Odd
elif pocket >= 11 and pocket <= 18 or pocket >= 29 and pocket <= 36:
    print('The pocket is black.')
    
else:
    print("Error: Please enter a number from '0-36'.")