#Fibonacci2
num = 0
s = 0
a, b = eval(input('a~b='))
n1, n2 = 0, 1
print(n1, n2)
n = n1 + n2
while n <= b:
    if n >= a:
        print(n)
        s += n
        num += 1
    n1, n2 = n2, n
    n = n1 + n2
print('num=', num)
print('sum=', s)
