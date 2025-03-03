

n = int(input("How many Fibonacci terms do you want? : "))

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series:")
    print(0)
else:
    fib_list = [0, 1]
    for i in range(2, n):
        next_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_fib)
    print("Fibonacci series:")
    for num in fib_list:
        print(num)
    