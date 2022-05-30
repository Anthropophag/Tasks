class Toy:
    def __init__(self, name, color, typ):
        self.name = name
        self.color = color
        self.typ = typ


class Factory:
    color: object

    def __init__(self, typ: str):
        if typ != 'toy_from_mult' and typ != 'animal':
            print('You writed wrong typ for toy')
        self.typ = typ

    def parch_materials(self):
        match self.typ:
            case 'toy_from_mult':
                print('Was bought:\n'
                      '1. filament\n'
                      '2. stuffing material\n'
                      '3. upholstery fabric\n'
                      'Was сontract signed on the rights to use the character')
                print()
            case 'animal':
                print('Was bought:\n'
                      '1. filament\n'
                      '2. stuffing material\n'
                      '3. upholstery fabric\n'
                      '4. artificial wool')
                print()

    def sewing(self):
        print('Party successfully sewn')
        print()

    def coloration(self, color):
        self.color = color
        print(f'Toy was coloring in {color}')
        print()
        return color

    def get_toy(self, name):
        toy = Toy(name, self.color, self.typ)
        print(f'Toy {toy.name} successfully create')
        return toy


factory_1 = Factory('animal')
factory_1.parch_materials()
factory_1.sewing()
factory_1.coloration('blue')
factory_1.get_toy('Chomic')
