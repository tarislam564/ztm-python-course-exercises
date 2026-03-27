# Enumerate()

for i, char in enumerate('Helllooo'):
    print(i, char)
0 H
1 e
2 l
3 l
4 l
5 o
6 o
7 o
for i, char in enumerate([1, 2, 3]):
    print(i, char)
0 1
1 2
2 3
for i, char in enumerate(range(100)):
    if char == 50:
        print(f"index of 50 is: {i}")
index of 50 is: 50
