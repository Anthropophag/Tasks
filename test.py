with open('output.txt', mode='w') as test:
    str = test.readlines().strip().split('; ')
    for test_znach in str:
        print(test_znach[1:len(test_znach) - 1].split(','))











