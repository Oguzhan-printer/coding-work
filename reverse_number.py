

number = int(input('Please enter a number: '))
reverse_number = 0

while number > 0:
    last_step = number % 10  
    reverse_number = (reverse_number * 10) + last_step 
    number = number // 10  
print(reverse_number)