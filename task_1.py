# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

calc, rate, hours, extras = argv

rate = int(rate)
hours = int(hours)
extras = int(extras)

print('Скрипт расчета заработной платы сотрудника')
print(f'Рабочая ставка: {rate}')
print(f'Сотрудник отработал: {hours} часов')
print(f'Премия: {extras}')
print(f'Заработная плата: {(hours * rate) + extras}')
