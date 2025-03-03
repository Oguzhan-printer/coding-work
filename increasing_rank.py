
number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))
number3 = int(input("Enter the third integer: "))

if number1 <= number2 and number1 <= number3:
    smallest = number1
    if number2 <= number3:
        middle = number2
        largest = number3
    else:
        middle = number3
        largest = number2
elif number2 <= number1 and number2 <= number3:
    smallest = number2
    if number1 <= number3:
        middle = number1
        largest = number3
    else:
        middle = number3
        largest = number1
else:
    smallest = number3
    if number1 <= number2:
        middle = number1
        largest = number2
    else:
        middle = number2
        largest = number1

print("Numbers sorted from smallest to largest:")
print(smallest)
print(middle)
print(largest)