#sprt
x = eval(input('x(x>1)='))
p = eval(input('point='))
t = 10 ** p
bottom, top = 1, x
while True:
    a = (bottom + top) / 2
    print(a, bottom, top)
    if int(bottom * t) == int(top * t):
        print(int(top * t) / t)
        break
    if a * a > x:
        top = a
    elif a * a < x:
        bottom = a
    else:
        print('Got it')
        break
