
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number == second_number and second_number == third_number and third_number == first_number:
    print("All numbers are equal")
elif first_number == second_number and first_number != third_number:
    print("First and second numbers are equal")
elif second_number == third_number and second_number != first_number:
    print("Second and third numbers are equal")
elif first_number == third_number and first_number != second_number:
    print("First and third numbers are equal")
else:
    print("No two numbers are equal")
