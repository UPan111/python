# RT Lesson 体操计分

s = 0#累加总分变量
sMax = 0
sMin, sMinID = 10, 0
scList = [9.8, 9.2, 9.5, 10, 9.4, 10, 9.3, 9.7]
for i in range(len(scList)):#枚举每个分数
    sc = scList[i]#sc是第i裁判的打分
    if sMax < sc:
        sMax= sc
    if sMin > sc:
        sMin = sc
        sMinID = i
    s += sc
    print(sc)
print('max=', sMax)
print('min=',sMin)
print('avg=', s / len(scList))#Step1:计算输出平均分
avg2 = (s - sMax - sMin) / (len(scList) - 2)
print('avg2', int(avg2 * 1000 + 0.5) / 1000)#Step2:计算输出去掉一个最高分、去掉一个最低分之后的平均分”
print('min:', sMin, '\tNo=', sMinID + 1)#Step3:计算输出“打最低分的裁判编号”
