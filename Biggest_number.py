
first_number = int(input('Enter the first number :')) 
second_number = int(input('Enter the second number :'))
third_number = int(input('Enter the third number :'))

if first_number > second_number and first_number > third_number:
    print(first_number, 'is the largest number')
elif second_number > first_number and second_number > third_number:
    print(second_number, 'is the largest number')
elif third_number > first_number and third_number > second_number:
    print(third_number, 'is the largest number')
else:
    print('All numbers are equal')

