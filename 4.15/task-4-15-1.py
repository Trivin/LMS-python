class Transport(object):

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def Print(self):
        print(f'{self.name} Скорость: {self.max_speed} Пробег: {self.mileage}')

Autobus = Transport('Renaul Logan', 180, 12)
Autobus.Print()