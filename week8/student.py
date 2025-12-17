from telephone_number import TelephoneNumber


class Student:
    def __init__(
        self,
        name: str,
        school: str,
        school_area_code: str,
        school_number: str,
    ) -> None:
        self._name = name
        self._school = school

        self._school_telephone = TelephoneNumber()
        self._school_telephone.area_code = school_area_code
        self._school_telephone.number = school_number

    @property
    def name(self) -> str:
        return self._name

    @property
    def school(self) -> str:
        return self._school

    @property
    def school_telephone_number(self) -> str:
        return self._school_telephone.telephone_number
