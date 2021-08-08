#fruit
pApple = 3.5
pBanana = 5.5
a, b = eval(input('weight of apple and banana:'))
if b < 5:
    b0, b1, b2, b3 =b, 0, 0, 0
if b < 10:
    b0, b1, b2, b3 =5, b-5, 0, 0
if b < 20:
    b0, b1, b2, b3 =5, 5, b-10, 0
else:
    b0, b1, b2, b3 =5, 5, 10, b-20
money = a * pApple + \
        b0 * pBanana + \
        b1 * pBanana * 0.8 + \
        b2 * pBanana * 0.7 + \
        b3 * pBanana * 0.6
print('amount:' , money)
