def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
#--------main---------
while True:
    n = eval(input('n='))
    for n1 in range(n, 1, -1):
        if is_prime(n1):
            Max = n1
            break
    if Max == n1:
        print('biggest',Max)
