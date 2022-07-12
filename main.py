class Armor:
    def __init__(self, *args):
        self.armors_tup = args
        self.armors = {}
        for i in args:
            self.armors[i[0]] = i[1]

    def __repr__(self):
        if len(self.armors) == 0:
            return f'Armor()'
        else:
            return f'{self.armors_tup}'

    def add(self, key):
        if key in self.armors.keys():
            self.armors[key] += 1
        else:
            self.armors[key] = 1


class GhostInArmor(Armor):
    def __init__(self, *args, name='Canterville'):
        super().__init__()
        self.name = name

    def __getitem__(self, key):
        pass


if __name__ == '__main__':
    ar = Armor(("helmet", 1), ("glove", 2))
    ar.add("bib")
    print(ar)
    print(Armor())
    gia = GhostInArmor(("knee pad", 2), ("handlebar", 1), ("shoe", 1), name="Ghost")
    print(gia)
