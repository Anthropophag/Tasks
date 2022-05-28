import os


def make_dir(patch):
    try:
        os.mkdir(patch)
        print('Директория успешно создана')
    except FileExistsError:
        print('Директория уже была создана')
    except PermissionError:
        print('Недостаточно прав для создания директории')


def remove_dir(patch):
    try:
        os.removedirs(patch)
        print('Директория успешно удалена')
    except FileNotFoundError:
        print('Директория не найдена')
    except PermissionError:
        print('Недостаточно прав для создания директории')


def list_dir():
    print(*[i for i in os.listdir() if os.path.isdir(i)])


def chenge_dir(patch):
    try:
        os.chdir(patch)
        print('Вы успешно перешли в директорию')
    except FileNotFoundError:
        print('Заданной папки не существует')


do = {1: chenge_dir,
      2: list_dir,
      3: remove_dir,
      4: make_dir}

while True:
    choice = input('Выберите пункт:\n'
                   '1. Перейти в папку\n'
                   '2. Посмотреть содержимое текущей папки\n'
                   '3. Удалить папку\n'
                   '4. Создать папку\n'
                   '5. Выйти\n'
                   '---------------------\n'
                   'Ваш выбор: ')
    try:
        if len(choice.split()) == 2:
            choice, foldername = choice.split()
            choice = int(choice)
            if do.get(choice):
                do[choice](foldername)
        else:
            choice = int(choice)
            if choice == 5:
                break
            if do.get(choice):
                print(do[choice]())
    except ValueError:
        print('Вы ввели неверные данные')
    except TypeError:
        print('Вы не указали имя папки')
