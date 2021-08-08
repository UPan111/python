#monte carlo pi
import random
ns = eval(input('times='))
nc = 0
for i in range(ns):
    x = random.random()
    y = random.random()
    if x * x + y * y < 1:
        nc += 1
print ('pi=', 4 * nc / ns)
