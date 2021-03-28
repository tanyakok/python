def summ(string_1):
    '''
    Функция преобразовывает полученную строку в кортеж и складывает элементы кортежа. Результатом функции является сумма кортежа - целое число

    :param string_1: string
    :return: int
    '''
    string_1 = string_1.split()
    s = 0
    for el in string_1:
        try:
            el = int(el)
            s += el
        except ValueError:
            return s
    return s


s = 0
while True:
    data = input('Введите числа через пробел. Для выхода введите "x": ')
    s += summ(data)
    print(f'Сумма всех чисел: {s}')
    if data.endswith('x'):
        break
