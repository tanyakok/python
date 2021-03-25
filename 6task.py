titles = ('название', 'цена', 'количество', 'ед')

n = int(input('Сколько товаров добавить в базу: '))
i = 1
structure = list()
for el in range(n):
    product = list()
    print(f'Сбор данных для {i}-го товара. ', end='')
    product.append(input('Введите название: '))
    product.append(int(input('Введите цену: ')))
    product.append(int(input('Введите количество: ')))
    product.append(input('Введите единицы: '))

    my_dict = {titles[0]: product[0], titles[1]: product[1], titles[2]: product[2], titles[3]: product[3]}

    structure.append((i, my_dict))
    i += 1

print(f'Готовая структура: {structure}')

analytics = {}

for el in structure:
    for key, value in el[1].items():
      if key in analytics:
        if not(value in analytics[key]):
          analytics[key].append(value)
      else:
        analytics[key] = [value]
print(f'Аналитика: {analytics}')
