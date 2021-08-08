#Fibonacci
s = eval(input('s(s>1)='))
n1, n2 = 0, 1
print(n1, n2)
n = n1 + n2
while n <= s:
    print(n)
    n1, n2 = n2, n
    n = n1 + n2
