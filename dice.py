# Aaron Gallegos
# Test 2 - Part 2
# ACC ID: a2098917
# 7/13/2020
# Programming Problem # 2
# This program rolls a die 100,000 times, keeps 
# track of the outcomes, and displays to the screen the 
# percentages of each outcome.

# First, we load contents of random module into memory.
import random

# Next, we set MIN, MAX constants for die and set amount of rolls.
MIN = 1
MAX = 6
ROLLS = 100000

# Set accumulators to zero.
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

# Use for Loop to simulate rolls a predetermined number of times.
for x in range (0, ROLLS + 1):
    roll = random.randint(MIN, MAX)
    if roll == 1:
        ones += 1
    elif roll == 2:
        twos += 1
    elif roll == 3:
        threes += 1
    elif roll == 4:
        fours += 1
    elif roll == 5:
        fives += 1
    elif roll == 6:
        sixes += 1
        
# Display results of rolls in percentages.
print('1 was rolled ', format((ones / ROLLS * 100), '.2f'), '% of the time.')
print('2 was rolled ', format((twos / ROLLS * 100), '.2f'), '% of the time.')
print('3 was rolled ', format((threes / ROLLS * 100), '.2f'), '% of the time.')
print('4 was rolled ', format((fours / ROLLS * 100), '.2f'), '% of the time.')
print('5 was rolled ', format((fives / ROLLS * 100), '.2f'), '% of the time.')
print('6 was rolled ', format((sixes / ROLLS * 100), '.2f'), '% of the time.')