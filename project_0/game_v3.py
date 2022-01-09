
import numpy as np

def random_predict(number: int = 1) -> int:
    """Компьютер сам загадывает и сам угадывает число"

    Args:
        number (int, optional): загаданное число. Значение по умолчанию - 1.

    Returns:
        int: число попыток угадывания
    """
    
    count = 0
    min_limit = 1 # создаем две дополнительные переменные, которые будут содержать минимальный и максимальный лимит для генерации числа
    max_limit = 101
    
    while True:
        count+=1
        predict_number = np.random.randint(min_limit,max_limit) # компьютер генерирует случайное число
        if number < predict_number:
            max_limit = predict_number # если загаданное число меньше, чем сгенерированное программой, 
                                       # то максимальный лимит для генерации сокращается до нашего сгенерированного числа
        if number > predict_number:
            min_limit = predict_number # если загаданное число больше, чем сгенерированное программой, 
                                       # то минимальный лимит для генерации сокращается до нашего сгенерированного числа
        if number == predict_number:
            #print(f'Компьютер загадал число {number} и угадал его с {count}-й попытки!')
            break
    return count # возвращаем количество попыток


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем наша программа угадывает загаданное число за 1000 запусков

    Args:
        random_predict ([type]): функция угадывания числа

    Returns:
        int: среднее количество попыток для угадывания
    """
    count_ls = [] # сохраняем в данном списке количество попыток угадывания для каждого числа
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101, size=(1000)) # загадали список чисел (1000 штук) для угадывания
    
    for number in random_array:
        count_ls.append(random_predict(number)) # для каждого загаданного значения из массива мы вставляем результат 
                                                # действия функции random_predict от этого значения в список count_ls
    #score = int(sum(count_ls)/len(count_ls))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает загаданное число в среднем за {score} попыток')
    return(score)

# RUN
score_game(random_predict)