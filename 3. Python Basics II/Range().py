# Range()

print(range(100))
print(range(0, 100))
range(0, 100)
range(0, 100)
for number in range(10):
    print(number, end=' ')
print()
0 1 2 3 4 5 6 7 8 9 
for _ in range(10):
    print('Hi', end=' ')
print()
Hi Hi Hi Hi Hi Hi Hi Hi Hi Hi 
for number in range(0, 10, 2):
    print(number, end=' ')
print()
0 2 4 6 8 
for number in range(0, 10, -1):
    print(number, end=' ')
print()
Nothing
for number in range(10, 0, -1):
    print(number, end=' ')
print()
10 9 8 7 6 5 4 3 2 1 
for number in range(10, 0):
    print(number, end=' ')
print()
Nothing
for number in range(10, 0, -2):
    print(number, end=' ')
print()
10 8 6 4 2 
for _ in range(2):
    print(list(range(10)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
