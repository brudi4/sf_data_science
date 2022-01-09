"""Игра Угадай число"""

import numpy as np

number = np.random.randint(1,101) # загадываем число

# количество попыток
count = 0

while True:
    count+=1
    predict_number = int(input('Угадайте число от 1 до 100!'))
    
    if predict_number < number:
        print('Число должно быть больше!')
    elif predict_number > number:
        print('Число должно быть меньше!')
    else:
        print(f'Вы угадали число с {count}-й попытки! Это число {number}!')
        break

