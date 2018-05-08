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
        owners = [car.owner for car in Car.all() if car.make == make]
        return owners

    @classmethod
    def has_oldest_car(cls):
        cars = Car.all()
        oldest = cars[0]
        for car in cars:
            if car.year < oldest.year:
                oldest = car
        return oldest.owner

    def find_my_car(self):
        cars = Car.all()
        for car in cars:
            if car.owner == self:
                return car
        return "You don't have a car yet"

    def drives_same_make_as_me(self):
        cars = Car.all()
        my_car = self.find_my_car()
        same_cars = [car.owner for car in cars if car.owner != self and car.make == my_car.make]
        return same_cars
