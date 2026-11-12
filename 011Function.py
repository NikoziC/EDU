def multiply(a,b):
    return a * b
print(multiply(20, 30))


def welcome(name):
    print(f"Welcome {name}")

welcome("Nikita")


def checks(a):
    if a == 0:
        print("zero")
    elif a > 0:
        print("positive")
    else:
        print("negative")

checks(8)


def factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact *= i
    print(fact)

factorial(8)


def aver(a, b, c):
    return (a + b + c) / 3

print(aver(7, 8, 90))

