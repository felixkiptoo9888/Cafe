# PROMPTING A NUMBER ENTERED IF ITS NEGATIVE POSITIVE OR ZERO
Number= float(input('Enter a number: '))
# logic
if Number>0:
    print('The Number is Positive')
    if Number >100:
        print('get bonus points')
elif Number<0:
    print('The number is negative')
elif Number ==0:
    print('The number is zero')
else:
    print('Invalid')

# calculations with more logic & more conditions (assignment)
