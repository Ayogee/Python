male = int(input('How many males are registered in class?: '))
female = int(input('How many females are registered in class?: '))
total = int(male + female)

print('The percentage of males registered in class is', 
      format(male / total, '%'))
print('The percentage of females registered in class is', 
      format(female / total, '%'))