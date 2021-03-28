def my_func(num_1, num_2, num_3):
    '''
    Функция подсчитывает сумму двух наибольших чисел

    :param num_1: int
    :param num_2: int
    :param num_3: int
    :return: int
    '''
    my_list = [num_1, num_2, num_3]
    max_1 = max(my_list)
    my_list.remove(max_1)
    max_2 = max(my_list)
    return max_1 + max_2


value_1 = int(input('Введите первое число: '))
value_2 = int(input('Введите второе число: '))
value_3 = int(input('Введите третье число: '))
print(f'Сумма двух наибольших чисел: {my_func(value_1, value_2, value_3)}')
