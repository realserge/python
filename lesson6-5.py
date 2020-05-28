class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки маркером')

a = Stationary('Кисть')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
a.draw()
pen.draw()
pencil.draw()
handle.draw()