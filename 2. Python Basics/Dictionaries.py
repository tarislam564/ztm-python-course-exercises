# Dictionaries

dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'c': True
}

print(dictionary['a'][1])
print(dictionary)
print('\n')
2
{'a': [1, 2, 3], 'b': 'Hello', 'c': True}


# Dictionary Methods

user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20
}

print(user.get('age', 55))
20
user2 = dict(name='JohnJohn')
print(user2)
{'name': 'JohnJohn'}
print('basket' in user)
True
print('size' in user)
False
print('age' in user.keys())
True
print('Hello' in user.values())
True
print(user.items())
dict_items([('basket', [1, 2, 3]), ('greet', 'Hello'), ('age', 20)])
user2 = user.copy()
user.clear()
print(user)
{}
print(user2)
{'basket': [1, 2, 3], 'greet': 'Hello', 'age': 20}
print(user2.pop('age'))
20
print(user2.popitem())
('greet', 'Hello')
user2.update({'age': 55})

print(user2)
{'basket': [1, 2, 3], 'age': 55}
print('\n')
