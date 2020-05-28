class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def make_road(self, weight, cm):
        result = self._width*self._length*weight*cm
        return result
road = Road(500,2000)
print("Масса полотна: ", road.make_road(36,7)/1000, "т")
