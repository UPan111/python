#casion2
import random

n = 0
pWin, plose, pTie = 0, 0, 0
for i in range(300):
    print('round:', i + 1)
    input('go')
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print('Player', '\tDice1:', d1, 'Dice2', d2, '\tscore:', d1 + d2)
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6)
    print('AI', '\tDice3:', d3, 'Dice4', d4, '\tscore:', d3 + d4)
    if d1 + d2 < d3 + d4:
        print('you lose!')
        plose += 1
    if d1 + d2 > d3 + d4:
        print('you Win!')
        pWin += 1
    if d1 + d2 == d3 + d4:
        print('Tie!')
        pTie += 1
print('player', '\tWin', pWin, 'Lose:', plose, 'Tie:', pTie)
if pWin == plose:
    n += 1
for j in range(n):
    print('round:', j + 1)
    input('go')
    d5 = random.randint(1, 6)
    d6 = random.randint(1, 6)
    print('Player', '\tDice1:', d5, 'Dice2', d6, '\tscore:', d5 + d6)
    d7 = random.randint(1, 6)
    d8 = random.randint(1, 6)
    print('AI', '\tDice3:', d7, 'Dice4', d8, '\tscore:', d7 + d8)
    if d1 + d2 < d3 + d4:
        print('you lose!')
        plose += 1
    if d1 + d2 > d3 + d4:
        print('you Win!')
        pWin += 1
    if d1 + d2 == d3 + d4:
        print('Tie!')
        pTie += 1
    print('player', '\tWin', pWin, 'Lose:', plose, 'Tie:', pTie)
    if pWin != plose:
        break
        
