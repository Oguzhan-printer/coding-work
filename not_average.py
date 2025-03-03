
course_1 =int(input('please enter the first course grade: '))
course_2 = int(input('please enter the second course grade: '))
course_3 = int(input('please enter the third course grade: '))

average = (course_1 + course_2 + course_3) / 3

if average >= 50:
    print('you passed')
else:
    print('you failed')