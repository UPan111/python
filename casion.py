#casion
import random

sMax = 0
for i in range(3):
    print('round:', i + 1)
    input('go')
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 + d2 > sMax:
        sMax = d1 + d2
    print('Player', '\tDice1:', d1, 'Dice2', d2, '\tscore:', d1 + d2)
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6)
    print('AI', '\tDice3:', d3, 'Dice4', d4, '\tscore:', d3 + d4)
print('Best:',sMax)
