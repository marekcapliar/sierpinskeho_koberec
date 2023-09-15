from string import ascii_lowercase

fr = open('objednane_jedla.txt', 'r')

zoz = fr.readlines()
print('pocet jedal je', len(zoz), '\n')

zoz_jedal = {}
for i in zoz:
    if i[-2] in ascii_lowercase:
        zoz_jedal[i[-2]] = zoz_jedal.get(i[-2], 0) + 1
    else:
        zoz_jedal[i[-1]] = zoz_jedal.get(i[-1], 0) + 1
print('pocet jednotlivych jedal:', zoz_jedal, '\n')

malo_jedal = []
for i in zoz_jedal:
    if zoz_jedal[i] < 20:
        malo_jedal.append(i)

if len(malo_jedal) == 0:
    print('kazde jedlo si objednalo dostatok stravnikov')
else:
    print('nedostatok objednaneho jedla:', malo_jedal)