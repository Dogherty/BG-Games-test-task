def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(x, y):
    return gcd(x, y) == 1

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if are_coprime(num1, num2):
    print(f"{num1} и {num2} взаимно просты.")
else:
    print(f"{num1} и {num2} не взаимно просты.")
