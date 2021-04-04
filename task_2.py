# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

f = open('love_letter')
content = f.readlines()
print(content)
print(f'В файле {len(content)} строки')
for el in content:
    print(f'В {content.index(el) + 1} строке {len(el.split())} слова')
f.close()
