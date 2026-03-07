# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.
dict_keys(['age', 'username', 'weapons', 'is_active', 'clan'])
# 3 Add a new weapon to your user
{'age': 0, 'username': ' ', 'weapons': 'Katana', 'is_active': False, 'clan': None}
# 4 Add a new key to include 'is_banned'. Set it to false
{'age': 0, 'username': ' ', 'weapons': None, 'is_active': False, 'clan': None, 'is_banned': False}
# 5 Ban the user by setting the previous key to True
{'age': 0, 'username': ' ', 'weapons': None, 'is_active': False, 'clan': None, 'is_banned': True}
# 6 create a new user2 my copying the previous user and update the age value and username value.


#ANSWERS BELOW:

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    'age': 0,
    'username': ' ',
    'weapons': None,
    'is_active': False,
    'clan': None
}

# 2 iterate and print all the keys in the above user.
print(user_profile.keys())

# 3 Add a new weapon to your user
user_profile['weapons'] = 'Katana'

# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})

# 5 Ban the user by setting the previous key to True
user_profile['is_banned'] = True

# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user_profile.copy()
user2.update({'age': 50, 'username': 'User2'})
print(user_profile)
print(user2)
{'age': 0, 'username': ' ', 'weapons': 'Katana', 'is_active': False, 'clan': None, 'is_banned': True}
{'age': 50, 'username': 'User2', 'weapons': 'Katana', 'is_active': False, 'clan': None, 'is_banned': True}
