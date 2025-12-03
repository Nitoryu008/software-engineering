from person import Person
from typing import Iterable, Iterator, List


class Employees(Iterable[Person]):
    def __init__(self) -> None:
        self._persons = []

    def get_nth(self, index: int) -> Person:
        return self._persons[index]

    def add_person(self, person: Person) -> None:
        self._persons.append(person)

    def __len__(self) -> int:
        return len(self._persons)

    def __iter__(self) -> Iterator[Person]:
        return EmployeesIterator(self)

    def remove_nth(self, index: int):
        self._persons.remove(self.get_nth(index))


class EmployeesIterator(Iterator[Person]):
    def __init__(self, es: Employees) -> None:
        self.employees = es
        self._index = 0

    def __next__(self) -> Person:
        if self._index >= len(self.employees):
            raise StopIteration

        result = self.employees.get_nth(self._index)
        self._index += 1
        return result
