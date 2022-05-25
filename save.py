import re

with open('input.txt', mode='r', encoding='utf-8') as text:
    start_text = text.readlines()

verse = ''
for i in start_text:
    verse = verse + i.strip()

patern = '(\.\.\.)'
if re.search(patern, verse) is None:
    print('В тексте нет нескольких точек подряд')
else:
    print('В тексте есть белее оденой точки подряд')
