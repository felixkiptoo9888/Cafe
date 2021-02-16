
First_Name = str(input('Enter your first name: '))
Second_Name = str(input('Enter your second name: '))
Gross = float(input('Enter your gross salary: '))
Children = int(input('Enter the number of children you have: '))

Net_Income = (Gross-(Children*3000))

# tax calculation
if Net_Income > 50000:
    tax = (0.15*50000) + (0.25*(Net_Income-50000))
    print('Your Income Tax Is', '$', tax)
elif Net_Income < 500000:
    tax = (0.15*Net_Income)
    print('Your income tax is: ', '$', tax)
else:
    print('Invalid')




