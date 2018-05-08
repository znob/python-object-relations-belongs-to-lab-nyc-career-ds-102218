import unittest2 as unittest
import sys
sys.path.insert(0, '..')
from person import Person
from car import Car

class TestQueryPersonClassMethods(unittest.TestCase):
    
    global dwight
    dwight = Person("Dwight Schrute", "Paper Salesperson")
    global pam
    pam = Person("Pam Beasley", "Secretary")
    global michael
    michael = Person("Michael Scott", "Regional Manager")
    global stanley
    stanley = Person("Stanley Hudson", "Paper Salesperson")
    global jim
    jim = Person("Jim Halpert", "Paper Salesperson")
    global meredith
    meredith = Person("Meredith Palmer", "Purchaser - Supplier Relations")
    global ford_minivan
    ford_minivan = Car("Ford", "Aerostar Minivan", 1997, meredith)
    global corolla
    corolla = Car("Toyota", "Corolla", 2000, jim)
    global chrylser300
    chrylser300 = Car ("Chrysler", "300C", 2008, stanley)
    global chrysler
    chrysler = Car("Chrysler", "Sebring Convertible", 2004, michael)
    global toyota
    toyota = Car("Toyota", "Yaris", 2007, pam)
    global datsun
    datsun = Car("Datsun", "280Z", 1978, dwight)

    def test_person_property_methods(self):
        self.assertEqual(dwight._name, "Dwight Schrute")
        self.assertEqual(dwight.name, "Dwight Schrute")
        self.assertEqual(dwight._occupation, "Paper Salesperson")
        self.assertEqual(dwight.occupation, "Paper Salesperson")

    def test_car_property_methods(self):
        self.assertEqual(datsun._make, "Datsun")
        self.assertEqual(datsun.make, "Datsun")
        self.assertEqual(datsun._model, "280Z")
        self.assertEqual(datsun.model, "280Z")
        self.assertEqual(datsun._year, 1978)
        self.assertEqual(datsun.year, 1978)
        self.assertEqual(datsun._owner, dwight)
        self.assertEqual(datsun.owner, dwight)
        self.assertItemsEqual(Car._all, [ford_minivan, corolla, chrysler, chrylser300, toyota, datsun])
        self.assertItemsEqual(Car.all(), [ford_minivan, corolla, chrysler, chrylser300, toyota, datsun])

    def test_cars_driven_by_class_method(self):
        self.assertItemsEqual(Car.cars_driven_by("Secretary"), [toyota])

    def test_drives_a_class_method(self):
        self.assertItemsEqual(Person.drives_a("Toyota"), [jim, pam])

    def test_has_oldest_car_class_method(self):
        self.assertEqual(Person.has_oldest_car(), dwight)

    def test_drives_same_make_as_me_instance_method(self):
        self.assertItemsEqual(jim.drives_same_make_as_me(), [pam])
