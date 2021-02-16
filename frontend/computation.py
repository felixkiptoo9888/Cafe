# salary computation
name = 'Jean Zakwani'
hrs = 40
hrt = 6.75
ftwr = 0.2
stwr = 0.09

GP = hrs*hrt
FTW = ftwr*GP
STW = stwr*GP

TD = FTW+STW

NP = GP-TD

print('Employee Full Name:', name)
print('Number of Hours worked in a week:', hrs, 'hours')
print('Hourly Pay Rate:', '$', hrt)
print('Gross Pay:', '$', GP)
print('Federal Tax Withholding (20%):', '$', FTW)
print('State Tax Withholding rate(9%):', '$', STW)
print('Total Deduction:', '$', TD)
print('Net Pay:', '$', NP)
