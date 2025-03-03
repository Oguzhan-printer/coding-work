
exam_grade = int(input('Please enter your exam grade'))

if 90 >= exam_grade >= 90:
    print('Your examination grade is A')
elif 80 >= exam_grade >= 89:
    print('Your examination grade is B')
elif 70 >= exam_grade >= 79:
    print('Your examination grade is C')
elif 60 >= exam_grade >= 69:
    print('Your examination grade is D')
elif 0 >= exam_grade >= 59:
    print('Your examination grade is F')