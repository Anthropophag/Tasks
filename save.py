count_row = 0
while True:
    try:
        count_row += 1
        mags = []
        withes = []
        wizards = input()
        match count_row % 2:
            case 0:
                for i in wizards.split():
                    if i[0] == '3':
                        mags.append(i)
                print(*mags, sep='_')
            case 1:
                for i in wizards.split():
                    i = int(i)
                    if i - i // 10 * 10 == 7:
                        withes.append(i)
                print(*withes, sep='_')
    except EOFError:
        break
