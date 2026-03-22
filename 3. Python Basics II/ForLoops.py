# For Loops

for item in 'Zero to Mastery':
    print(item, end=' ')
print()
Z e r o   t o   M a s t e r y 
for item in [1, 2, 3, 4, 5]:
    print(item, end=' ')
print()
1 2 3 4 5 
for item in {1, 2, 3, 4, 5}:
    print(item, end=' ')
print()
1 2 3 4 5 
for item in (1, 2, 3, 4, 5):
    print(item, end=' ')
print(item)
print()
1 2 3 4 5 5
# Nested Loops
for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x, end='\t')
1 a	1 b	1 c	2 a	2 b	2 c	3 a	3 b	3 c	4 a	4 b	4 c	5 a	5 b	5 c	
