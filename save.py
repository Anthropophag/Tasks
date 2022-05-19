from random import randint


def attack(person1, person2):
    lucky_coin = randint(0, 1)
    while person1['health'] > 0 or person2['health'] > 0:
        if lucky_coin == 0:
            person1['health'] -= person2['damage']
        else:
            person2['health'] -= person1['damage']
    if person1['health'] > 0:
        print('WINER - ', person1['name'])
        print('health - ', person1['health'])
    else:
        print('WINER - ', person2['name'])
        print('health - ', person2['health'])


def harm(damege, armor):
    return damege / armor


name = input()

with open('name_enemy.txt', mode='r', encoding='utf-8') as enemy_inf:
    enemy_inf = enemy_inf.readlines()
enemy = {}
for parm in enemy_inf:
    inf = parm.strip().split()
    enemy[inf[0]] = inf[1]
print(enemy)

with open('name_hero.txt', mode='r', encoding='utf-8') as hero_inf:
    hero_inf = hero_inf.readlines()
hero = {}
for parm in hero_inf:
    inf = parm.strip().split()
    hero[inf[0]] = inf[1]
print(hero)






