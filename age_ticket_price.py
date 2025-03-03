
Age = int(input('Please enter your age: '))

if 5 >= Age >= 0:
    print('Free of charge ')
elif 6 >= Age >= 18:
    print('Pay 10 dollars ')
elif 19 >= Age >= 64:
    print('Pay 20 dollars ')
elif Age >= 65:
    print('Pay 15 dollars ')
else:
    print('Invalid age')

