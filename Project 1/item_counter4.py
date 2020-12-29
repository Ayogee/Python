# This program displays the number of names that is
# stored in a specified file.
# Aaron Gallegos
# 7/12/2020
# ACC ID: a2098917

# We open and associate the .txt file with a Python
# file object / variable.
in_file = open('names.txt', 'r')

# Initialize an accumulator.
count = 0

# We read every string in the entire file.
for line in in_file:
    count += 1
    
# Lastly, we display the number of names in the file.
print('There are a total of ', count, ' names in this file.')

# We close the program.
in_file.close()