n = int(input("Enter number of n terms: "))

if n <= 0:
    print("Fibonacci series up to", n, "is not defined")
elif n == 1:
    print("The first", n, "number in the fibonacci series =")
    print(0)
else:
    first = 0
    second = 1
    print("The first", n, "numbers in the fibonacci series =")
    print(first, second, sep=", ", end="")
    
    
    for i in range(2, n):
        fib = first + second
        first = second
        second = fib
        print(",", fib, end="")
    print()  
