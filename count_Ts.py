# This program counts the number of times
# the letter T (uppercase or lowercase)
# appears in the string.

def main():
    # Create a variable to use to hold the count.  
    # The accumulator must start with 0.
    count = 0
    
    # Get a string from the user.
    my_string = input('Enter a sentence: ')
    
    # Count the Ts.
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count += 1
            
    # Print the result.
    print('The letter T appears', count, 'times.')
    
# Call the main function.
main()