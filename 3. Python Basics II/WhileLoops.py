# While loops

i = 0
while i < 50:
    print(i, end='\t')
    i += 1
else:
    print('\nDone with all the work.')
print()
0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49
Done with all the work.
my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
print()
1
2
3
while True:
    response = input('Say Something: ')
    if response == 'bye':
        break
Say Something: hi
Say Something: bye
