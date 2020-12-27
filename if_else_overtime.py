hours_base = 40
OT_multiplier = 1.5

hours_worked = float(input('Enter the number of hours worked: '))
hourly_rate = float(input('Enter the hourly rate: '))

if hours_worked > hours_base:
    hours_OT = float(hours_worked - hours_base)
    OT_pay = hours_OT * OT_multiplier * hourly_rate
    gross_pay = (hours_base * hourly_rate) + OT_pay
else:
    gross_pay = hours_base * hourly_rate
    
print('The Gross Pay is: $', format(gross_pay, ',.2f'), sep='')
