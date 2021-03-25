numbers_list = ['зима', 1, 2, 12, 'весна', 3, 4, 5, 'лето', 6, 7, 8, 'осень', 9, 10, 11]
el = int(input('Введите номер месяца: '))

while not (el in numbers_list):
    el = int(input('Такого месяца нет. Попробуйте еще раз: '))

pos = numbers_list.index(el)

# 1,2,3 - 0
# 5,6,7 - 4
# 9,10,11 - 8
# 13,14,15 - 12

if pos in [1, 2, 3]:
    season = numbers_list[0]
elif pos in [5, 6, 7]:
    season = numbers_list[4]
elif pos in [9, 10, 11]:
    season = numbers_list[8]
else:
    season = numbers_list[12]
print(f'{el}-й месяц это {season}')
