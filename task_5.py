# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce

f = open('numb_file.txt', 'w+')
numbers = input('Введите набор чисел через пробел: ')
f.write(numbers)

f.seek(0)
content = f.readlines()


def my_func(first_el, second_el):
    return int(first_el) + int(second_el)


result = reduce(my_func, content[0].split())
print(f'Сумма введенных чисел: {result}')
f.close()
