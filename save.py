from PIL import Image


class LifeCaseRobot:
    def __init__(self, *skils: str, serial='0001'):
        self.skils = list(skils)
        self.serial = serial

    def __pow__(self, other: int):
        start_serial = str(int(self.serial) ** other)
        if len(start_serial) >= 4:
            self.serial = start_serial[-4:]
            return self
        else:
            self.serial = f'{"0" * (4 - len(start_serial))}{start_serial}'
            return self

    def __repr__(self):
        if self.skils:
            return f"LifeCaseRobot({str(self.skils)[1:-1]}, serial='{self.serial}')"
        else:
            return f"LifeCaseRobot(serial='{self.serial}')"

    def __invert__(self):
        new_action = [self.skils[i] for i in range(0, len(self.skils) - 1, 2)]
        return LifeCaseRobot(*new_action, serial=self.serial[::-1])

    def __call__(self, number: int) -> list:
        finish = []
        count = 0
        count_2 = 0
        while count != number:
            while len(self.skils) > count_2:
                for i in self.skils:
                    ser_number = int(self.serial) + (count + 1)
                    new_exeamp = LifeCaseRobot(
                        i,
                        serial=f'{"0" * (4 - len(str(ser_number)))}{ser_number}'
                    )
                    finish.append(new_exeamp)
                    count += 1
                    count_2 += 1
            else:
                ser_number = int(self.serial) + (count + 1)
                new_exeamp = LifeCaseRobot(serial=f'{"0" * (4 - len(str(ser_number)))}{ser_number}')
                finish.append(new_exeamp)
                count += 1
        return finish

    def extend(self, array: list):
        for i in array:
            if i not in self.skils:
                self.skils.append(i)
        self.skils.sort(reverse=False)
        self.skils.sort(key=len)

    def upgrade(self, func) -> str:
        self.skils = list(map(func, self.skils))
        ser_number = str(int(self.serial) + 1)
        self.serial = f'{"0" * (4 - len(ser_number))}{ser_number}'
        return 'READY'

    def evaluate(self, filename: str) -> tuple:
        img = Image.open(filename)
        pixels = img.load()
        x, y = img.size
        all_rgb = [0, 0, 0]
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                all_rgb[0] += r
                all_rgb[1] += g
                all_rgb[2] += b
        difference = []
        for i in all_rgb:
            for j in all_rgb:
                if i - j not in difference:
                    difference.append(i - j)
        ser_number = str(int(self.serial) + max(difference))
        if len(ser_number) <= 4:
            self.serial = f'{"0" * 4 - len(ser_number)}{ser_number}'
        else:
            self.serial = f'{ser_number[-4:]}'
        return tuple(all_rgb)

    def robotic(self, *args) -> dict:
        finish = {}
        for i in args:
            count = 0
            for j in self.skils:
                if i in j:
                    count += 1
            finish[i] = count
        return finish


if __name__ == '__main__':
    lcr = LifeCaseRobot('care')
    lcr1 = LifeCaseRobot('clean', serial='1005')
    actions = ['cook', 'wash', 'drive']
    print(lcr.extend(actions))
    actions.clear()
    lcr1 **= 12
    lcr1.extend(['draw'])
    lcr2 = ~lcr1
    print(lcr, lcr1, lcr2, sep='\n')
    print(lcr.evaluate('robot.png'))
    print(lcr)

    # lcr = LifeCaseRobot('think')
    # actions = ['read', 'write', 'think']
    # lcr.extend(actions)
    # actions.clear()
    # print(lcr.upgrade(lambda x: x.title()))
    # print(lcr)
    # # res = lcr(5)
    # # res[0].extend(['divide'])
    # # print(res)
