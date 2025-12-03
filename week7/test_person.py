import unittest
from person import Person


class TestPerson(unittest.TestCase):
    def test_name(self):
        b = Person("Taro Joho", 20, "Ibaraki")
        self.assertEqual(b.name, "Taro Joho")
