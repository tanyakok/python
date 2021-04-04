# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

from io import open

f = open('subjects', encoding='utf-8')
content = f.readlines()
print(content)

middle_number = ''
final_number = 0
int_number = 0
final_dict = {}

for el in content:
    final_number = 0
    sub = el.split()[0].replace(':', '')
    for part in el.split():
        for el in part:
            try:
                int(el)
                middle_number = middle_number + el
            except ValueError:
                pass
        try:
            int_number = int(middle_number)
            middle_number = ''
            final_number = final_number + int_number
        except ValueError:
            pass
    dict = {sub: final_number}
    final_dict.update(dict)

print(final_dict)

f.close()
