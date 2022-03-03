"""
Использование модуля random
для создания простейшей игры в кости.
"""
import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)
sum1 = dice1 + dice2
sum2 = dice3 + dice4
if sum1 > sum2:
    print('Игрок 1 победил!')
elif sum1 == sum2:
    print('Ничья')
else:
    print('Игрок 2 победил!')
print('Игрок 1:',dice1,dice2,'\n'
      'Игрок 2:',dice3,dice4,'\n', end="")