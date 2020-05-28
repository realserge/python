from random import randint
def gen_unique_num(count, min, max):
    arr = []
    while len(arr) < count:
        new = randint(min, max)
        if new not in arr:
            arr.append(new)
    return arr

class Keg:
    __num = None

    def __init__(self):
        self.__num = randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)


class Card:
    __data = None


    def __init__(self):
        numbers = gen_unique_num(15, 1, 90)

        self.__data = []
        for i in range(0, 3):
            tmp = sorted(numbers[5 * i: 5 * (i + 1)])
            for j in range(0, 4):
                index = randint(0, 5)
                tmp.insert(index, 0)
            self.__data += tmp

    def __str__(self):
        separator = '--------------------------'
        arr = separator + '\n'
        for index, num in enumerate(self.__data):
            if num == 0:
                arr += '  '
            elif num == -1:
                arr += ' -'
            elif num < 10:
                arr += f' {str(num)}'
            else:
                arr += str(num)

            if (index + 1) % 9 == 0:
                arr += '\n'
            else:
                arr += ' '

        return arr + separator

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
     index = self.__data.index(num)
     self.__data[index] = -1

    def closed(self):
        return set(self.__data) == {0, -1}


class Game:
    __usercard = None
    __compcard = None
    __kegs = []
    __gameover = False

    def __init__(self):
        self.__usercard = Card()
        self.__compcard = Card()
        self.__kegs = gen_unique_num(90, 1, 90)

    def start(self):
        while True:

            keg = self.__kegs.pop()
            print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
            print(f'----- Ваша карточка ------\n{self.__usercard}')
            print(f'-- Карточка компьютера ---\n{self.__compcard}')

            useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()
            if useranswer == 'y' and not keg in self.__usercard or  useranswer != 'y' and keg in self.__usercard:
                print('Вы проиграли')
                break


            if keg in self.__usercard:
                self.__usercard.cross_num(keg)
                if self.__usercard.closed():
                    print('Вы выиграли')
                    break
            if keg in self.__compcard:
                self.__compcard.cross_num(keg)
                if self.__compcard.closed():
                    print('Вы проиграли')
                    break


game = Game()
game.start()
