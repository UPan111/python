#goldbach
while True:
    n = eval(input('n='))
    for n1 in range(2, n - 1):
        flag = True
        for i in range(2, n1):
            if n1 % i == 0:
                flag = False
                break
        if flag == False:
            continue
        n2 = n - n1
        n2flag = True
        for i in range(2, n - n1):
            if n2 % i == 0:
                n2flag == False
                break
            if flag == False:
                continue
        if flag == True and n2flag == True:
            print(n1,n2)
