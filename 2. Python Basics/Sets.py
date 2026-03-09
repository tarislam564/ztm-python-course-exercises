# Sets

my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(2)
print(my_set)
{1, 2, 3, 4, 5, 100}
my_list = [1, 2, 3, 4, 4, 5, 5]
print(set(my_list))
print(list(my_set))
{1, 2, 3, 4, 5}
[1, 2, 3, 4, 5, 100]

new_set = my_set.copy()
my_set.clear()
print(my_set)
print(new_set)
print('\n')
set()
{1, 2, 3, 4, 5, 100}

# Set Methods

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set))
{1, 2, 3}
print(my_set.intersection(your_set))
{4, 5}
print(my_set.isdisjoint(your_set))
False
print(my_set.issubset(your_set))
False
print(my_set.issuperset(your_set))
False
print(my_set.union(your_set))
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
my_set.difference_update(your_set)
print(my_set)
{1, 2, 3}
my_set.discard(5)
print(my_set)
{1, 2, 3, 4}

