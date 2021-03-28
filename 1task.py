def division(arg_1, arg_2):
    '''
    Функция выполняет деление двух чисел

    :param arg_1: float - делимое
    :param arg_2: float - делитель
    :return: float
    '''
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return 'Деление на ноль'


divident = float(input('Введите делимое: '))
divisor = float(input('Введите делитель: '))
print(division(divident, divisor))
