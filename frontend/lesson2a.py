# operators
# control statements - if, if else, elif, for loop, nested program
# if, if else, elif, are for decision making
weight = float(input('enter your weight: '))
height = float(input('please enter your height: '))

BMI = weight/pow(height,2)

print('Your weight is', weight,'kgs')
print('Your height is', height,'meters')
print('Your body mass index is', BMI)

if BMI <=17:
    print('Underweight')
elif BMI>17 and BMI<=22.5:
    print('normal')
elif BMI>22.5 and BMI<30:
    print('Overweight')
else:
    print('see a physician')