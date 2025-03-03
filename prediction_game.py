

import random

random_number = random.randint(1, 100)
forecast = 0
forecast_number = 0

print('Keep a number for you. Lets try to guess. ')

while random_number != forecast:
    forecast = int(input('your forecast : '))
    forecast_number += 1

    if forecast < random_number:
        print('your number is too low')
    elif forecast > random_number:
        print('your number is too high')
    else:
        print(f'Congratulations! You were correct in guessing {forecast_number}. The number I kept is: {random_number}')
        