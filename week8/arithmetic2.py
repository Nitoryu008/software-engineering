import unittest
from typing import Generic, Sequence, TypeVar, Union

T = TypeVar("T", int, float)


class NumList(Generic[T]):
    def __init__(self, numbers: Sequence[T]) -> None:
        self.numbers: list[T] = list(numbers)

    def sum(self) -> Union[T, int]:
        return sum(self.numbers)

    def average(self) -> float:
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

    def max(self) -> T | None:
        if not self.numbers:
            return None
        return max(self.numbers)


class IntList(NumList[int]):
    def __init__(self, numbers: list[int]) -> None:
        super().__init__(numbers)

    def sum(self) -> int:
        return sum(self.numbers, start=0)

    def translate_to_dots(self) -> list[str]:
        return ["." * num for num in self.numbers]


class FloatList(NumList[float]):
    def __init__(self, numbers: list[float]) -> None:
        super().__init__(numbers)

    def sum(self) -> float:
        return sum(self.numbers, start=0.0)

    def map_floor(self) -> list[int]:
        import math

        return [math.floor(num) for num in self.numbers]


class TestIntList(unittest.TestCase):
    def test_int_list(self) -> None:
        il = IntList([1, 2, 3, 4, 5])
        self.assertEqual(il.sum(), 15)
        self.assertEqual(il.average(), 3.0)
        self.assertEqual(il.max(), 5)
        self.assertEqual(il.translate_to_dots(), [".", "..", "...", "....", "....."])


class TestFloatList(unittest.TestCase):
    def test_float_list(self) -> None:
        fl = FloatList([3.14159, 2.71828, 1.41421, 1.61803, 0.69314])
        self.assertAlmostEqual(fl.sum(), 9.58525)
        self.assertAlmostEqual(fl.average(), 1.91705)
        max_val = fl.max()
        assert max_val is not None
        self.assertAlmostEqual(max_val, 3.14159)
        self.assertEqual(fl.map_floor(), [3, 2, 1, 1, 0])


if __name__ == "__main__":
    unittest.main()
