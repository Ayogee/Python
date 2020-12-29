# This program calculates the average of all numbers
# stored in a specified file.
# Aaron Gallegos
# 7/12/2020
# ACC ID: a2098917

# First we open the file.
avg_file = open('numbers.txt', 'r')
                
# Next, we create accumulators.
sum_numbers = 0
num_numbers = 0

# We go through each line, convert to int, and add to
# accumulators.
for line in avg_file:
    sum_numbers += int(line)
    num_numbers += 1

# Next, we calculate the average.
average = sum_numbers / num_numbers

# We display the average.

print('The average of the numbers is: ', average)

# Lastly, we close the file.
avg_file.close()