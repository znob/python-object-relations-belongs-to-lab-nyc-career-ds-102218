# import car class here
from car import Car

class Person:

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation

    @property
    def name(self):
        return self._name

    @property
    def occupation(self):
        return self._occupation

    @classmethod
    def drives_a(cls, make):
        cars = list(filter(lambda car.owner: car.make == make, Car.all()))
        return cars

    def drives_same_make_as_me(self):
        pass
