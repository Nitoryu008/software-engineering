class Person:
    def __init__(self, name, age, address) -> None:
        self._name = name
        self._age = age
        self._address = address

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def address(self) -> str:
        return self._address

    def print_name(self) -> None:
        print(self._name)

    def print_age(self) -> None:
        print(self._age)

    def print_address(self) -> None:
        print(self._address)

    @name.setter
    def name(self, new_name) -> None:
        self._name = new_name

    @age.setter
    def age(self, new_age) -> None:
        self._age = new_age

    @address.setter
    def address(self, new_address) -> None:
        self._address = new_address

    def print_profile(self) -> None:
        self.print_name()
        self.print_age()
        self.print_address()


if __name__ == "__main__":
    p1 = Person("Taro Joho", 20, "Ibaraki")
    p1.age = 21
    p1.print_profile()
    print()
    p2 = Person("Hanako Kagaku", 27, "Tokyo")
    p2.address = "Nagano"
    p2.print_profile()
    print()
