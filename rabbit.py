#rabbit
h, f = eval(input('h,f='))
flag = 0
for r in range (0, h + 1):
    c = h - r
    if r * 4 + c * 2 == f:
        print('rabbit:', r, '\tRooster', c)
        flag += 1
if flag == 0:
    print ('no answer')
