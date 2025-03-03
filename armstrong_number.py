
number = int(input("Enter a number: "))
temp = number
digit_count = len(str(number))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digit_count
    temp //= 10

if number == total:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")