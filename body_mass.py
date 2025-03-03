
height = float(input(' Please enter your height for body mass index : '))
weight = float(input(' Please enter your weight for body mass index : '))

index = weight / (height ** 2)

if index > 25:
    print('You are overweight')
elif index < 18.5:
    print('You are underweight')
else:
    print('You are normal')