# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

from json import dump

with open('firms.txt') as f:
    content = f.readlines()

i = 0
average_profit = 0
my_list = []
my_dict = {}

for el in content:
    profit = int(el.split()[2]) - int(el.split()[3])
    if profit> 0:
        average_profit += profit
        i += 1
    my_dict.update({el.split()[0]: profit})

my_list.append(my_dict)
average_profit = round(average_profit / i)
print(f'Средняя прибыль компаний: {average_profit}')
my_list.append({'average_profit': average_profit})
print(my_list)

with open('firms.json', 'w') as f_json:
    dump(my_list, f_json)
