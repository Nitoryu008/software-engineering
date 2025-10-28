class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def greet(self):
        print("I am a university student.")
        print(f"I am {self._name}.")
        print(f"I am {self._age} years old.")
