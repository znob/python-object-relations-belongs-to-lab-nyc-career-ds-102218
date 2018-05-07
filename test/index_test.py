import unittest2 as unittest
import sys
sys.path.insert(0, '..')
from person import Person
from query import Query

class TestQueryPersonClassMethods(unittest.TestCase):

    def test_person_class_init(self):
        global per_1
        global per_2
        global per_3
        global per_4
        global per_5
        per_1 = Person("Jeff", 31)
        per_2 = Person("Molly", 24)
        per_3 = Person("Kevin", 38)
        per_4 = Person("Rachel", 27)
        per_5 = Person("Devin", 25)
        self.assertItemsEqual(Person._all, [per_1, per_2, per_3, per_4, per_5])

    def test_person_class_property_methods(self):
        self.assertEqual(per_1._name, "Jeff")
        self.assertEqual(per_1.name, "Jeff")
        self.assertEqual(per_1._age, 31)
        self.assertEqual(per_1.age, 31)

    def test_query_count_class_method(self):
        self.assertEqual(Query.count(Person), 5)

    def test_query_find_by_name_class_method(self):
        self.assertEqual(Query.find_by_name(Person, "Jeff"), per_1)

    def test_query_name_starts_with_class_method(self):
        self.assertItemsEqual(Query.name_starts_with(Person, 'K'), [per_3])

    def test_query_is_older_than_class_method(self):
        self.assertItemsEqual(Query.is_older_than(Person, 30), [per_1, per_3])

    def test_query_mean_age_class_method(self):
        self.assertEqual(Query.mean_age(Person), 29)
    #
    def test_person_count_class_method(self):
        self.assertEqual(Person.count(), 5)

    def test_person_find_by_name_class_method(self):
        self.assertEqual(Person.find_by_name("Jeff"), per_1)

    def test_person_name_starts_with_class_method(self):
        self.assertEqual(Person.name_starts_with('K'), [per_3])

    def test_person_is_older_than_class_method(self):
        self.assertItemsEqual(Person.is_older_than(30), [per_1, per_3])

    def test_person_mean_age_class_method(self):
        self.assertEqual(Person.mean_age(), 29)
