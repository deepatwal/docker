def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print("The first 10 values in the Fibonacci series are:")
print("printing the values using ")
for i in range(1, 11):
    print(fib(i))
