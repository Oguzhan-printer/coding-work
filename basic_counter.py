
for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Number between 1-100 divided by both 3 and 5: ",number)
    elif number % 3 == 0:
        print("Number between 1-100 divided by 3: ",number)
    elif number % 5 == 0:
        print("Number between 1-100 divided by 5: ",number)
    else:
        print("Number between 1-100 not divided by 3 or 5: ",number)
