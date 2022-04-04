import sympy

number = int(input())

if sympy.isprime(number):
    print("This number is prime")
else:
    print("This number is not prime")