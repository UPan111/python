#casino3诈金花
import random
#建议先做顺子：循环100000次，统计有多少个顺子，这就是统计概率
b = 0
s = 0
d = 0
for i in range(100000):
    print('round: ', i +1)
    d1=random.randint(1, 6)
    d2=random.randint(1, 6)
    d3 =random.randint(1, 6)
    if d1 == d2 == d3:
        b += 1
    if 
