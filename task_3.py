# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

from functools import reduce

f = open('employees')
content = f.readlines()
print(content)

print('Сотрудники с окладом менее 20000:')
for el in content:
    if int(el.split()[len(el.split())-1]) < 20000:
        print(el.split()[0])


def my_func(first_el, second_el):
    return first_el + second_el

my_list = []
for el in content:
    my_list.append(int(el.split()[len(el.split())-1]))

print(f'Средний доход сотрудников: {reduce(my_func, my_list)/len(content):.0f}')

f.close()
