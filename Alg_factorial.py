def iter_factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact

print (iter_factorial(4))
