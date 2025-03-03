
wheather = str(input('what is the weather ( snowy, rainy, sunny): '))
degree = int(input('Enter the air temperature: '))

if wheather == 'sunny'and degree >= 25:
    print('You can have a picnic.')
elif wheather == 'rainy':
    print('Dont forget to take an umbrella.')
elif wheather == 'snowy' and degree <= 0:
    print('You can go skiing.')
else:
    print('You can stay at home.')

