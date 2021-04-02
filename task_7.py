from math import factorial

def fact(n):
    for el in range(1, n + 1):
        yield el

n = int(input('Введите число для нахождения факториала: '))
print(fact(n))

for el in fact(n):
    print(f'{el}! = {factorial(el)}')
