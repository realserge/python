class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
       return sum(self._income.values())


a = Position('Alex', 'Ignatev', 'Programmer', 150000, 75000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())