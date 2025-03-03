
print('Four Operation Menu')
print('1. Addition (+)')
print('2. Subtraction(-)')
print('3. Multiplication(*)')
print('4. Division(/)')

choose = input('Choose an operation (1/2/3/4):')

number_1 = int(input('Enter first number:'))
number_2 = int(input('Enter second number:'))

match choose:
    case '1':
        result = number_1 + number_2
        transac_symbol = '+'
    case '2':
        result = number_1 - number_2
        transac_symbol = '-'
    case '3':
        result = number_1 * number_2
        transac_symbol = '*'
    case '4':
        if number_2 != 0:
            result = number_1 / number_2
            transac_symbol = '/'
        else:
            print('Error! Division by zero is not allowed.')
    case _:
            print('Invalid operation.')

if 'result' in locals():
     print(f'{number_1} {transac_symbol} {number_2} = {result}')
     


        
