def fibo(n):
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input("Enter the valu of N: "))
print("{n}th term of Fibonacci series is: ",fibo(n-1))