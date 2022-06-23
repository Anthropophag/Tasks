words = input().split(' : ')
short = []
long = []
with_letter = []
for word in words:
    if len(word) < 4:
        short.append(word.lower())
    if len(word) > 7:
        long.append(word)
    if 'w' in word:
        with_letter.append(word.lower().capitalize())
short.sort()
long.sort()

print('Short: ', end='')
print(*short, sep='; ')
print('Loong: ', end='')
print(*long[::-1], sep='; ')
print('With letter: ', end='')
print(*with_letter, sep='; ')
