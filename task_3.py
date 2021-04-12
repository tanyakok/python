class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


p = Position('Вася', 'Пупкин', 'уборщик', 50, 10)
print(p.name)
print(p.surname)
print(p.position + '\n')
print(f'Полное имя: {p.get_full_name()}')
print(f'Полный доход: {p.get_total_income()}\n')
p_1 = Position('Игорь', 'Николаев', 'музыкант', 100, 50)
print(p_1.name)
print(p_1.surname)
print(p_1.position + '\n')
print(f'Полное имя: {p_1.get_full_name()}')
print(f'Полный доход: {p_1.get_total_income()}')
