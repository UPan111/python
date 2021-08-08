
#LCM
a, b = eval(input('lcm a,b='))
if a < b:
    a, b = b, a
for n in range(a, a * b + 1, a):
    if n % a == 0 and n % b ==0:
        print(n)
        break

#GCF
a, b = eval(input('gcf a,b='))
if a < b:
    a, b = b, a
for i in range(a + 1, 0, -1):
    if a % i == 0 and b % i ==0:
        print(i)
        break
