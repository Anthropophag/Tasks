class Person:
    health: int

    def __init__(self):
        self.health = 150
        self.armor = 0
        self.demage = 0

    def _clean_damage(self):
        return self.armor - self.demage

    def attack(self, name_person):
        if person.armor > 0:
            uron = self._clean_damage()
            person.armor -= uron
            print(f'You dealt {uron} damage to an {name_person.name}')
        else:
            person.health += person.armor
        if person.health > 0:
            uron = self._clean_damage()
            person.health -= uron
            print(f'You dealt {uron} damage to an {name_person.name}')
        else:
            print(f'{person.name} defeated')


class Player(Person):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.demage = 15
        self.armor = 30
        print(f'Created player {name}')

    demage = 15
    armor = 30


class Enemy(Person):
    def __init__(self):
        super().__init__()
        self.name = 'Orc'
    demage = 25
    armor = 10


player1 = Player('Vonerut')
person = Enemy()

player1.attack(person)

print(person.health)
