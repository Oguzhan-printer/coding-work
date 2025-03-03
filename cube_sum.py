
N = int(input('Please enter a number :'))

sum = 0

for i in range(1, N+1):
     sum = sum + i**3
    
print('Sum of cubes between 1-N : ', sum)