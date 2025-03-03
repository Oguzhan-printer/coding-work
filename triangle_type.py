
first_side_lenght = int(input('Please enter the first side length: '))
second_side_lenght = int(input('Please enter the second side length: '))
third_side_lenght = int(input('Please enter the third side length: '))

if first_side_lenght + second_side_lenght > third_side_lenght and first_side_lenght + third_side_lenght > second_side_lenght and second_side_lenght + third_side_lenght > first_side_lenght:
    print('This is a variegated  triangle')
elif first_side_lenght == second_side_lenght == third_side_lenght:
    print('This is an equilateral triangle')
elif first_side_lenght == second_side_lenght or first_side_lenght == third_side_lenght or second_side_lenght == third_side_lenght:
    print('This is an isosceles triangle')
else:
    print('This is not a triangle')



