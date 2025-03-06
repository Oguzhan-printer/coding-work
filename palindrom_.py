
kelime3 = input('bir kelime giriniz: ')

ters_kelime = kelime3[::-1]

if kelime3 == ters_kelime:
    print('kelime tersten okunuyorsa bu kelime  polindromdur. ')
else:
    print('kelime tersten okunmuyorsa polindrom kelime değildir.')