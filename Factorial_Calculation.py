
number = int(input('Please enter a number: '))


if number < 0:
    print("Factorial of negative numbers cannot be calculated.")
elif number == 0:
    print("0! = 1")
else:
    factorial = 1
    i = 1
    while i <= number:
        factorial *= i
        i += 1
    print(f"{number}! = {factorial}")