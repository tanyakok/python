my_list = [156, 17.5, 'я строка', [34, 45], None, True]
print(my_list)
i = 0
for el in my_list:
    print(f'Тип {i}-го элемента: {type(my_list[i])}')
    i += 1
