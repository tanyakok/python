from time import sleep
from random import choices

class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        print('Запуск нового светофора:')
        print(self.__color[0])
        sleep(1)
        for el in reversed(range(8)):
            if not el == 0:
                print(el)
                sleep(1)
        while True:
            current_color = choices(self.__color, weights=[1, 8, 1])[0]
            print(current_color)
            sleep(1)
            if current_color == 'желтый':
                for el in reversed(range(3)):
                    if not el == 0:
                        print(el)
                        sleep(1)
            else:
                print('Светофор сломался!')
                break
            current_color = choices(self.__color, weights=[1, 1, 8])[0]
            print(current_color)
            sleep(1)
            if current_color == 'зеленый':
                for el in reversed(range(4)):
                    if not el == 0:
                        print(el)
                        sleep(1)
            else:
                print('Светофор сломался!')
                break
            current_color = choices(self.__color, weights=[8, 1, 1])[0]
            print(current_color)
            sleep(1)
            if current_color == 'красный':
                for el in reversed(range(8)):
                    if not el == 0:
                        print(el)
                        sleep(1)
            else:
                print('Светофор сломался!')
                break

t_1 = TrafficLight()
t_1.running()
print()
t_2 = TrafficLight()
t_2.running()
