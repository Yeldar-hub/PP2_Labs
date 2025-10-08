# Task - 1
import math

degrees = float(input("Введите угол в градусах: "))
radians = degrees * (math.pi / 180)

print(f"{degrees} градусов = {radians} радиан")

# Task - 2
base1 = float(input("Введите длину первого основания: "))
base2 = float(input("Введите длину второго основания: "))
height = float(input("Введите высоту: "))

area = ((base1 + base2) / 2) * height

print("Площадь трапеции: ", area)

# Task - 3
n = int(input("Введите количество сторон: "))
s = float(input("Введите длину стороны: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print("Площадь правильного: ", area)

# Task - 4
base = float(input("Введите длину основания: "))
height = float(input("Введите высоту: "))
area = base * height

print(f"Площадь параллелограмма: {area}")
