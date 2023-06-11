from abc import ABC, abstractmethod

import constants


class Character(ABC):
    def __init__(self, model: str, arm_power: int):
        self.model = model
        self.arm_power = arm_power
        self.health = 100

    def attack(self, other):
        other.health -= self.arm_power

    @abstractmethod
    def __str__(self):
        pass

    def __eq__(self, other):
        return self.health == other.health

    def __gt__(self, other):
        return self.health > other.health

    def __ge__(self, other):
        return self.health >= other.health

    def __lt__(self, other):
        return self.health < other.health


class Tank(Character):

    def __init__(self, model: str, color: str, speed: float):
        super().__init__(model=model, arm_power=constants.TankSettings.TANK_POWER.value)
        self.speed = speed
        self.color = color

    def __str__(self):
        return f'I am a tank, my color is {self.color}'


class Artillery(Character):

    def __init__(self, model: str):
        super().__init__(model=model, arm_power=constants.ArtSettings.ART_POWER.value)

    def __str__(self):
        return f'I am an art, my power is {self.arm_power}'


class Battery:
    def __init__(self, battery_power: float = 5000):
        self.battery_power = battery_power

    @property
    def is_alive(self):
        return self.battery_power > 1000


class Javelin(Artillery):

    def __init__(self, model: str, battery: Battery):
        super().__init__(model=model)
        self.arm_power = constants.JavelinSettings.JAVELIN_POWER.value
        self.battery = battery

    @property
    def can_work(self):
        return self.battery.is_alive

    def attack(self, other):
        if self.can_work:
            other.health -= self.arm_power
            self.battery.battery_power = 500
            print(55555555555555)
        else:
            print('cannot work')


tank1 = Tank(model='abrams', color='yellow', speed=55.6)
art = Artillery(model='M777')
battery = Battery(5000)
javelin = Javelin('wunder waffe', battery)
battery.battery_power = 10
javelin.attack(tank1)
# tank1.attack(art)
battery2 = Battery(5500)
javelin.battery = battery2
javelin.attack(tank1)
javelin.attack(tank1)

print(tank1 >= art)

pass