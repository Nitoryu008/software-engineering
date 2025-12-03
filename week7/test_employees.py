import unittest
from employees import Employees
from person import Person


class TestEmployees(unittest.TestCase):
    def setUp(self) -> None:
        self.persons = [
            Person("Tsukuba Taro", 20, "Ibaraki"),
            Person("Amakubo Jiro", 20, "Ibaraki"),
            Person("Toshin Saburo", 20, "Tokyo"),
        ]
        self.employees = Employees()
        for person in self.persons:
            self.employees.add_person(person)

    def test_len(self):
        self.assertEqual(len(self.employees), 3)

    def test_iterator(self):
        i = 0
        for person in self.employees:
            self.assertEqual(person, self.persons[i])
            i = i + 1

    def test_remove_nth(self):
        self.employees.remove_nth(1)
        self.assertEqual(len(self.employees), 2)
        self.assertEqual(self.employees.get_nth(0), self.persons[0])
        self.assertEqual(self.employees.get_nth(1), self.persons[2])
        self.employees.remove_nth(0)
        self.employees.remove_nth(0)
        self.assertEqual(len(self.employees), 0)
