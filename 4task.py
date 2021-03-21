# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = input('Введите целое положительное число: ')

while not(number.isdecimal() == True and int(number) > 0):
    number = input('Число должно быть целым и положительным: ')

amount = len(number) - 1
i = 0
max_number = number[i]
while i < amount:
    i += 1
    if max_number < number[i]:
        max_number = number[i]
print('Самая большая цифра в числе: ', max_number)