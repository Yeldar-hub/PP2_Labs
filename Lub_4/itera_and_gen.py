# Task - 1
n = int(input("Введите число: "))
def my_generator():
    for i in range(n + 1):
        yield i ** 2

for num in my_generator():
    print(num)

# Task - 2
n = int(input("Введите число: "))
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
print(", ".join(str(num) for num in even_generator(n)))

# Task - 3
n = int(input("Введите число: "))
def new_generator(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for num in new_generator(n):
    print(num)

# Task - 4
def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
for num in squares(a, b):
    print(num)

# Task - 5
def versa_generator(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Введите число: "))
for num in versa_generator(n):
    print(num)