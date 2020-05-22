from time import sleep
class TrafficLight:
    __color = 'Зеленый'

    def running(self):
        cyrcle = {'Красный' : 7, 'Желтый' : 2, 'Зеленый' : 8}
        if self.__color != 'Зеленый':
            print('Светофор сломался')
            return
        for i in cyrcle:
            self.__color = i
            print(self.__color)
            sleep(cyrcle[i])
            
traffic_light = TrafficLight()
traffic_light.running()
traffic_light._TrafficLight__color = 'Желтый'
traffic_light.running()
print(traffic_light._TrafficLight__color)
