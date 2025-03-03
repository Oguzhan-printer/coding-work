
#Task 1

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

Collection = first_number + second_number
Extraction = first_number - second_number
Multiplication = first_number * second_number
Division = first_number / second_number
Full_division = first_number // second_number
Mode_retrieval = first_number % second_number
Base_taking = first_number ** second_number

print('Collection result:',Collection)
print('Extraction result:',Extraction)
print('Multiplication result:',Multiplication)
print('Division result:',Division)
print('Full division result:',Full_division)
print('Mode retrieval result:',Mode_retrieval)
print('Base taking result:',Base_taking)

#Task 2

take_radius = int(input("Enter the radius: "))
area_circle = 3.14 * (take_radius ** 2)
print(area_circle)