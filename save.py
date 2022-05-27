person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if money < 0:
        return 'Не коректтно указана сумма для снятия !'
    if person['money'] - money >= 0:
        person['money'] -= money
        # return 'Вы сняли {} рублей.'.format(money)
        return f'Вы сняли {money} рублей'
    else:
        return 'На вашем счету недостаточно средств!'


def start():
    try:
        card_number, pin_code = input('Введите номер карты и пин код через пробел: ').split()
        card_number = int(card_number)
        pin_code = int(pin_code)
        person = get_person_by_card(card_number)
    except ValueError:
        print('Вы вели некоректный номер или пинкод карты !')
        return
    if person and is_pin_valid(person, pin_code):
        while True:
            try:
                choice = int(input('Выберите пункт:\n'
                                   '1. Проверить баланс\n'
                                   '2. Снять деньги\n'
                                   '3. Выход\n'
                                   '---------------------\n'
                                   'Ваш выбор: '))
            except ValueError:
                print('Неверный ввод, повторите попытку.')
                continue

            if choice == 3:
                break
            elif choice == 1:
                print('Ваш баланс: ', check_account(person))
            elif choice == 2:
                try:
                    money = float(input('Сумма к снятию: '))
                    print(withdraw_money(person, money))
                except ValueError:
                    print('указана некректная сумма !')
    else:
        print('Номер карты или пин код введены не верно!')


start()
