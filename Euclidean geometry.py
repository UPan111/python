#Euclidean geometry
m, n = eval(input('m and n:'))
if m < n:
    m, n = n, m
r = m % n
while r:
    m = n
    n = r
    r = m % n
print ('huge', n)
