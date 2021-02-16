# loops = repeating a task n-times
# for loop - uses start, stop, step

for i in range (1, 5, 1):
    p = float(input('enter amount'))
    r = float(input('enter rate'))
    t = float(input('enter duration'))
    print('interest is ', p*r*t)