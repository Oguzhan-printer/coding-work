
num1= int(input('Please enter a  first number : '))
num2= int(input('Please enter a second number : '))
transaction = input('Please enter a transaction type (addition, subtraction, multiplication, division) : ')

match transaction:
    case 'addition':
        print(f'The result of the addition of {num1} and {num2} is {num1 + num2}')
    case 'subtraction':
        print(f'The result of the subtraction of {num1} and {num2} is {num1 - num2}')
    case 'multiplication':
        print(f'The result of the multiplication of {num1} and {num2} is {num1 * num2}')
    case 'division':
        print(f'The result of the division of {num1} and {num2} is {num1 / num2}')
    case _:
        print('Invalid transaction type')
         