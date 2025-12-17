class TelephoneNumber:
    def __init__(self, area_code: str = "", number: str = "") -> None:
        self._area_code = area_code
        self._number = number

    @property
    def area_code(self) -> str:
        return self._area_code

    @area_code.setter
    def area_code(self, value: str) -> None:
        self._area_code = value

    @property
    def number(self) -> str:
        return self._number

    @number.setter
    def number(self, value: str) -> None:
        self._number = value

    @property
    def telephone_number(self) -> str:
        return self._area_code + "-" + self._number
