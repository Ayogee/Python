# A = P(1+RN)NT
# A is the amount of money in the account after the specified number of years
# P is the principal amount that was originally deposited into the account
# R is the the annual interest rate
# N is the the number of times per year that the interest is compounded
# T is the the specified number of years the account will be left to earn
# interest

principal = int(input('Enter the amount that was originally deposited: '))
int_rate = int(input('Enter the annual interest rate: '))
times_compound = int(input('Enter the number of times per year that the interest is compounded: '))
years = int(input('Enter the number of years the account will be left to earn interest: '))
total_amount = principal * (1 + (int_rate/100)) * times_compound * years

print('The amount of money that will be in the account after', years, 'years is $', total_amount)