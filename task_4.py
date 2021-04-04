# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

f = open('count_eng')
content = f.readlines()
print(content)

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for el in content:
    val = my_dict.get(el.split()[0])
    new_string = ' '.join([val, el.split()[1], el.split()[2]])
    out_f = open('count_rus.txt', 'a')
    out_f.write(f'{new_string}\n')


out_f = open('count_rus.txt')
content = out_f.readlines()
print(content)
print('Done!')
f.close()
out_f.close()
