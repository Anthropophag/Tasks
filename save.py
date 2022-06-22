words = input().split(' : ')
short = []
lrong = []
with_letter = []
for word in words:
    if len(word) < 4:
        short.append(word.lower())
    if len(word) > 7:
        lrong.append(word)
    if 'w' in word:
        with_letter.append(word.lower().capitalize())

print(
    f'Short: {short}\n'
    f'Long: {lrong.sort()}\n',
    f'With letter: {with_letter}',
)
