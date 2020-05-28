class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} едет'

    def stop(self):
        return f'{self.name} стоит'

    def turn(self, direction):
        return f'{self.name} поворачивает {direction}'
    def show_speed(self):
        return f'Текущая скорость {self.name}  {self.speed}'


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость городского авто {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше, чем разрешено для городского авто'
        else:
            return f'Скорость {self.name} в норме для городского авто'
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость рабочего авто {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше, чем разрешено для рабочего авто'
class PoliceCar(Car):
        def police(self):
            if self.is_police:
                return f'{self.name} из полиции'
            else:
                return f'{self.name} не из полиции'


chevy = SportCar(100, 'Красный', 'Chevy', False)
mitsu = TownCar(30, 'Белый', 'Mitsu', False)
caddy = WorkCar(70, 'Перламутр', 'Caddy', True)
ford = PoliceCar(110, 'Синий',  'Ford', True)
print(chevy.turn('влево'))
print(caddy.stop())
print(f'{ford.go()} и {ford.show_speed()}')
print(f'{mitsu.name} {mitsu.color}')
print(f'{chevy.name} Полицейское авто? {chevy.is_police}')
print(f'{ford.name}  Полицейское авто? {ford.is_police}')
print(chevy.show_speed())
print(mitsu.show_speed())
print(ford.police())
print(ford.show_speed())