import random


def attack(person1, person2):
    while person1['health'] > 0 or person2['health'] > 0:
        lucky_coin = random.randint(0, 1)
        if lucky_coin == 0:
            person1['health'] -= person2['damage']
        else:
            person2['health'] -= person1['damage']


player = {
    'name': input(),
    'health': 100,
    'damage': 25
}
enemy = {
    'name': 'Orc',
    'health': 130,
    'damage': 18
}

print(player)