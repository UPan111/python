#prime number counting
import time

def is_prime(x):
    if x < 2 or x != int(x):
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3,int(x ** 0.5)+1, 2):
        if x % i == 0:
            return False
    return True
#--------main---------
n = eval(input('n='))
t0 = time.time()
cnt = 0
for i in range(2, n + 1):
    if is_prime(i):
        cnt += 1
print(time.time() - t0)
print('cnt=', cnt)
