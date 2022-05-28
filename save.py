def copy_this_file():
    filename = __file__
    with open(filename, mode='r') as first:
        name, extension = filename.split('.')
        with open(name + '_copy.' + extension, mode='w', encoding='utf-8') as dublicate:
            print(f'{first.read()}', file=dublicate)


if __name__ == '__main__':
    copy_this_file()
