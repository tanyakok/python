def int_func(my_string):
    '''
    Функция переводит первый символ полученной строки в верхний регистр, остальные - в нижний

    :param my_string: string
    :return: string
    '''
    my_string = my_string.capitalize()
    return my_string


word = input('Введите слово из маленьких латинских букв: ')
print(int_func(word))

user_string = input('Введите слова, разделенные пробелом: ')
user_string = user_string.split()
answer_string = []
for el in user_string:
    el = int_func(el)
    answer_string.append(el)
answer_string = ' '.join(answer_string)
print(answer_string)
