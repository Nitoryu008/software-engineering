import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def test_school_telephone_number(self):
        student = Student(
            name="Taro",
            school="Example High School",
            school_area_code="029",
            school_number="853-2063",
        )

        self.assertEqual(
            student.school_telephone_number,
            "029-853-2063",
        )


if __name__ == "__main__":
    unittest.main()
