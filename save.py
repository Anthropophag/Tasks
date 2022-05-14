names = ['Акакий', 'Геродот', 'Аристотель', 'Птолемей', 'Декарт', 'Цезарь']
salaries = [129, 341, 933, 792, 124356, 45]
data = dict(zip(names, salaries))

with open('salary.txt', mode='w', encoding='utf-8') as no_tax:
    for key, val in data.items():
        if val <= 50000:
            print(f'{key} - {val}', file=no_tax)

with open('salary.txt', encoding='utf-8') as no_tax:
    zp = no_tax.readlines()

for inf in zp:
    name = inf.strip().split(' - ')[0]
    start_salar = int(inf.strip().split(' - ')[1])
    salar = start_salar - start_salar * 0.13
    print(f'{name.upper()} - {salar}')