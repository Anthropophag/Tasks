import re


def registration(NL, email):
    patern_name = '[A-Z][a-z]+ [A-Z][a-z]+'
    patern_email = '[a-z0-9_\.]+@[a-z0-9]+\.[com|org|ru]+'
    count = 0
    while count == 0:
        if re.match(patern_name, NL) is None:
            NL = input('Имия или фомилия введены неверно, повторите попытку: ')
        else:
            print('Имя и фамилия введены верно')
            count += 1
    count = 0
    while count == 0:
        if re.match(patern_email, email) is None:
            email = input('email введён не правлиьлно, повторите попытку: ')
        else:
            print('email введён верно')
            count += 1


NL = input()
email = input()
registration(NL, email)
