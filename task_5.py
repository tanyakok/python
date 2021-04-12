class Stationery:
    title = 'канцелярия'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручки')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандаша')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркера')


s = Stationery()
s.draw()
p = Pen()
p.draw()
pc = Pencil()
pc.draw()
h = Handle()
h.draw()
