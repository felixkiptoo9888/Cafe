# list and tuples
# list is an array that stores multiple values in a single variable
points = [12, 23, 45, 22, 32, 23, 34, 54, 32, 26, 21]
# picking a variable in an array
print(points[3])  # prints variable 3 only
print(points[2:])  # prints variables above variable 2
print(points[:3])  # prints variable below variable 3
print(points[4:7])  # prints from 4 to 6

# list with strings
vegetables = ['spinnach', 'sukumawiki', 'cabbages', 'kales', 'corriander', 'x', 'y']
print('The grocery has the following greens', vegetables)
print(vegetables[:3])
print(type(vegetables))

# advantages of a list
# :they are dynamic and flexible

vegetables.append('fruits')
vegetables.remove('x')
vegetables.insert(3, 'kienyeji')
print(vegetables)

# more on list
cars = [[['Hilux', 'filder'], 'Nissan'], ['Ford', 'Canter'], ['Bike', 'Bycycle']]
print(cars)
print(cars[0][0][1])
# =================================================================================
# tuples are same as list, the only difference is that tuples cannot be appended or changed
ENGLISH = (50,54,67,354,76,765,76,56,46,45,45,34,65,65,65,65,45,76,43)
print(ENGLISH)
print(ENGLISH[:7])
# list are mutables- update, tuples are immutable - no updating
print(type(ENGLISH))

