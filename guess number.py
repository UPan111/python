#guess number
n = eval(input('num='))
bottom, top = 1, n + 1
while bottom != top:
    a = int((bottom + top) / 2)
    print('I guess', a)
    ans = input('> or < or = ?')
    if ans== '>':
        top = a
    elif ans == '<':
        bottom = a
    else:
        print('Got it')
        break
print(a)
