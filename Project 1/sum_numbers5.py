# This program reads all and calculates the total of 
# numbers of a specified file.
# Aaron Gallegos
# 7/12/2020
# ACC ID: a2098917

# First, we open the file and associate with a python
# file Object / Variable.
sum_file = open('numbers.txt', 'r')

# Next, we create an accumulator.
total = 0

# We go through each line and convert to int / add to
# accumulator, 'total'.
for line in sum_file:
    total += int(line)
    
# Next, we display the sum.
print('The sum of the numbers is: ', total)

# Finally, we close the file.
sum_file.close()