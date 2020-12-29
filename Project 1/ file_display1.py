# This program displays all numbers in a specified file.
# Aaron Gallegos
# 7/12/2020
# ACC ID: a2098917

# Starting off, we associate the .txt file with a Python
# file object, variable, 'in_file'.
in_file = open('numbers.txt', 'r')

# We read the entire file using the 'read' method.
num_In_File = in_file.read()

# We close the program.
in_file.close()

# Lastly, we display the contents of the variable:
# 'num_In_File'
print(num_In_File)