class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')
        self.speed = 0

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышает норму 60!')
        else: print(f'Скорость: {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышает норму 40!')
        else: print(f'Скорость: {self.speed}')

class PoliceCar(Car):
    pass

c = Car(75, 'розовая', 'Audi', False)
print(c.speed)
print(c.name)
print(c.color)
print(c.is_police)

c.go()
c.show_speed()
c.turn('вправо')
c.turn('влево')
c.stop()
c.show_speed()
print()

t = TownCar(70, 'белый', 'Toyota', False)
print(t.speed)
print(t.name)
print(t.color)
print(t.is_police)

t.go()
t.show_speed()
t.turn('вправо')
t.turn('влево')
t.stop()
t.show_speed()
print()

s = SportCar(120, 'красный', 'Tesla', False)
print(s.speed)
print(s.name)
print(s.color)
print(s.is_police)

s.go()
s.show_speed()
s.turn('вправо')
s.turn('влево')
s.stop()
s.show_speed()
print()

w = WorkCar(45, 'черный', 'Subaru', False)
print(w.speed)
print(w.name)
print(w.color)
print(w.is_police)

w.go()
w.show_speed()
w.turn('вправо')
w.turn('влево')
w.stop()
w.show_speed()
print()

p = PoliceCar(90, 'синий', 'Jeep', True)
print(p.speed)
print(p.name)
print(p.color)
print(p.is_police)

p.go()
p.show_speed()
p.turn('вправо')
p.turn('влево')
p.stop()
p.show_speed()
