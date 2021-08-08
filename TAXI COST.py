#RT LESSEN TAXI COST
#price list
tBeginPrince = 14
tBeginDst = 3
tPrice = 2.5
tLongDst = 15
dPrice = 2.4
dMin = 13
uPrice = 2.17
uMin = 15
#d = eval(input('distance='))
for dm in range(50, 201, 1):
    d = dm / 10
    #Taxi
    if d < tBeginDst:
        d1, d2 = 0, 0
    elif d < tLongDst:
        d1, d2 = d - tBeginDst, 0
    else:
        d1, d2 = tLongDst - tBeginDst, d - tLongDst
    tMoney = tBeginPrince + d1 * tPrice + d2 * tPrice * 1.5
    #Didi
    dMoney = dPrice * d
    if dMoney < dMin:
        dMoney = dMin
    #uber
    uMoney = uPrice * d
    if uMoney < uMin:
        uMoney = uMin
    #output result
    print('km:', d)
    print('Taxi:', tMoney)
    print('Didi:', dMoney)
    print('Uber:', uMoney)
