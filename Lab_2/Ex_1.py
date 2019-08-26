# Sa se scrie o functie care sa returneze o lista cu primele n numere din sirul lui Fibonacci.

def Fibonacci(n):
    fib = [1,1]
    for i in range(2 , n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib    

print(Fibonacci(15))
