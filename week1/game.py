class Character:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def print_status(self):
        print(f"Name:  {self.name}")
        print(f"HP:  {self.hp}")


class Enemy(Character):
    def __init__(self, name: str, hp: int, evilness: int):
        super().__init__(name, hp)
        self.evilness = evilness

    def print_status(self):
        super().print_status()
        print(f"Evilness:  {self.evilness}")


class Player(Character):
    def __init__(self, name: str, hp: int, experience: int):
        super().__init__(name, hp)
        self.experience = experience

    def print_status(self):
        super().print_status()
        print(f"Experience:  {self.experience}")

    def attack(self, enemy: Enemy):
        self.experience += 1
        print(f"{self.name} attacks {enemy.name}!")
        print(f"Experience: {self.experience - 1} -> {self.experience}")


if __name__ == "__main__":
    p = Player("ITF", 100, 0)
    e = Enemy("Wizard", 30, 78)
    p.print_status()
    e.print_status()
    p.attack(e)
    p.attack(e)
