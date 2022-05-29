class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} driving')

    def stop(self):
        print(f'{self.name} stoped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        if speed > 100:
            print('Car not for town')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        if speed < 100:
            print('Car not for race')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        print('Remember that this car must be returned in good condition')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def siren(self, condition: str):
        if condition == 'on':
            print('Siren on !')
        if condition == 'off':
            print('Siren off.')
