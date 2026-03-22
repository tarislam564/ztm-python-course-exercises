# Is vs ==

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
print()
True
False
False
True
True

print(True == True)
print('1' == 1)
print([1, 2, 3] == [1, 2, 3])
print()
True
False
True

print(True is 1)
print('1' is 1)
print([] is 1)
print(10 is 10.0)
print([1, 2, 3] is [1, 2, 3])
print()
False
False
False
False
False

print(True is True)
print('1' is '1')
print([] is [])
True
True
False
