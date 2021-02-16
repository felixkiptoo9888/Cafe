# question creat a simple calc
# solution
# prt

p = 50000
r = 5
t = 4
employee = "Anne"

print('Your name is', employee)
print('Your principle amount is', p)
print('at the rate of', r)
print('for', t, 'years')

# calculations
simple_interest = p*t*(r/100)
print(employee, 'your interest will be', simple_interest, 'ksh')

amount = p+simple_interest
print('Your amount is', amount)
