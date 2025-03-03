
height = float(input('Please enter the height: '))
weight = float(input('Please enter the weight: '))

index = weight / (height ** 2)

if index < 18.5:
    print('Underweight')
elif index >= 18.5 and index < 25:
    print('Normal weight')
elif index >= 25 and index < 30:
    print('Overweight')
elif index >= 30:
    print('Obese')