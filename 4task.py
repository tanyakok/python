words = input('Введите несколько слов через пробел: ')
words = words.split()
i = 1
for el in words:
    print(f'{i}. {el[:10]}')
    i += 1
