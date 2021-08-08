#statistics2
nList = list(eval(input('nList=')))
nMax, nMaxID = nList[0], 0
nMin, nMinID = nList[0], 0
s = 0
for i in range(len(nList)):
    s += nList [i]
    if nMax < nList[i]:
        nMax = nList[i]
        nMaxID = i
    if nMin > nList[i]:
        nMin = nList[i]
        nMinID = i
print('sum:', s)
print('avg:', s/len(nList))
print('Max:', nMax, '\tNo', nMaxID + 1)
print('min:', nMin, '\tNo', nMinID + 1)

