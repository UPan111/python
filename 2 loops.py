#2 loops
'''
for y in range(5):
    for x in range(5):
        print('y=', y, 'x=', x, end = '\t')
    print()
'''
n = eval(input('n='))
for y in range(n):
    for x in range(n - 1 - y):
        print(' ', end = '')
    for x in range(y + 1 + y):
        print('*', end = '')
    print()
for y in range(n - 2, -1, -1):
    for x in range(n - 1 - y):
        print(' ', end = '')
    for x in range(y + 1 + y):
        print('*', end = '')
    print()
