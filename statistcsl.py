#statistcsl
n = eval(input('num='))
s = 0
aMax = -9999999 #足够烂的先站在擂台上
aMin = 9999999
for i in range(n):
    print('No.', i + 1)
    a = eval(input('a='))
    s = s + a
    if a > aMax:#打擂台
        aMax = a #谁赢谁站在擂
    if a < aMin:
        aMin = a
print('sum:', s)
print('avg:', s / n)
print('max:', aMax)
print('min:', aMin)
