my_list = input('Введите числа для вхождения в Рейтинг через пробел: ')
my_list = my_list.split()
my_list = list(map(int, my_list))
number = int(input('Введите новое число: '))

my_list.append(number)
my_list.sort()
my_list.reverse()

my_list = map(str, my_list)
print('Рейтинг:', ', '.join(my_list))
