a = 'helloooooooooo'

if ((n := len(a)) > 10):
    print(f"too long {n} elements")
too long 14 elements
while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)
14
13
12
11
10
9
8
7
6
5
4
3
2
h
