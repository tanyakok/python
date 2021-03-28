def my_func(x, y):
    '''
    Функция возвращает результат возведения числа X в степень Y посредством математической операции

    :param x: float
    :param y: int
    :return: float
    '''
    return x ** y


def my_func_2(x, y):
    '''
    Функция возвращает результат возведения числа X в степень Y посредством циклических действий

    :param x: float
    :param y: int
    :return: float
    '''
    a = x
    for i in range(abs(y)-1):
        x *= a
    return 1 / x


num_1 = None
num_2 = None
while (type(num_1) is not float):
    num_1 = input('Введите действительное положительное число: ')
    try:
        num_1 = abs(float(num_1))
    except ValueError:
        print('Это не число!')

while (type(num_2) is not int):
    num_2 = input('Введите целое отрицательное число: ')
    try:
        num_2 = int(num_2)
    except ValueError:
        print('Это не число!')
if num_2 >= 0:
    num_2 = -1 * num_2

print(f'Введенные числа: {num_1} и {num_2}')
print(my_func(num_1, num_2))
print(my_func_2(num_1, num_2))
