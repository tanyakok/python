from sys import argv
from itertools import count

generator, begin, end = argv


for el in count(int(begin)):
    if el > int(end):
        break
    else:
        print(el)
