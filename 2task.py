# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds_left = (seconds - minutes * 60) % 60

print(f'Время: {hours :02}:{minutes :02}:{seconds_left :02}')