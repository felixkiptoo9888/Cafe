# dictionary stores data using key/ value approach
# mostly used to store an object data in json format: ie car details
person = {'name': 'Ken',
          'age': 22,
          'residence': 'nairobi',
          'weight': 72.5,
          'height': 1.5,
          'email': 'ken@gmail.com',
          'marks': 410}
print(person)
print(person['name'])
print(person['email'])

# append a new entry into a dictionary
person['marks'] = 500
print(person)

person['address'] = 'Haven Court, Waiyaki Way'
print('adding address', person)
del person ['weight']
print('delete weight', person)

# CRUD
# Delete the whole dictionary: del person
del person