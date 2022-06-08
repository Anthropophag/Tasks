from random import randint


class Player:
    def __init__(self, name: str, age: int, email: str):
        self.email = email
        self.age = age
        self.name = name

    def _generate_index(self):
        random_index = []
        for _ in range(5):
            while True:
                random_num = randint(0, 8)
                if random_num not in random_index:
                    random_index.append(random_num)
                    break
        return random_index

    def _generate_card(self):
        card = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] for _ in range(3)]
        for st in range(3):
            random_index = self._generate_index()
            for ind in random_index:
                while True:
                    random_num = randint(1, 90)
                    if random_num not in card:
                        card[st][ind] = random_num
                        break
        return card

    def start_play(self):
        player_card = self._generate_card()
        computer_card = self._generate_card()
        ind = 89
        on_of = 0
        use_keg = []
        while on_of == 0:
            random_keg = randint(1, 90)
            if random_keg in use_keg:
                continue
            else:
                print(f'Your got keg {random_keg}')
                print('-------Your card-------')
                for i in player_card:
                    print(*i)
                print('-----------------------')
                print('-----Computer card-----')
                for i in computer_card:
                    print(*i)
                print('-----------------------')
                choice = input('Cross out a number?\n'
                               '    y / n\n'
                               'Your choice: ')
                for ind, nums in enumerate(player_card):
                    if random_keg in nums:
                        if choice == 'y':
                            player_card[ind][nums.index(random_keg)] = '-'
                            use_keg.append(random_keg)
                        else:
                            print('You lose :(')
                            on_of += 1
                    if random_keg not in nums:
                        if choice == 'y':
                            print('You lose :(')
                            on_of += 1
                        else:
                            on_of += 0
                print('Сomputer move...')


if __name__ == '__main__':
    chel = Player('wrtwt', 34, 'sgf')
    chel.start_play()
