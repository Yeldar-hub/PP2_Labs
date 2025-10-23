# Task - 1
import math 
numbers = [1, 2, 3, 4, 5]
result = math.prod(numbers)
print(result)

# Task - 2
text = input("Введите текст: ")
upper = 0
lower = 0
for i in text:
    if i.isupper():
        upper += 1
    else:
        lower += 1
print("Lower case: ", lower)
print("Upper case: ", upper)

# Task - 3
text = input("Введите строку: ")
rev_text = reversed(text)
rev_text = (''.join(rev_text))

if text == rev_text:
    print("Text is polyndrom")
else:
    print("Text is not polyndrom")

# Task - 4
import time
import math
num = int(input())
miliseconds = int(input())

time.sleep(miliseconds / 1000)
result = math.sqrt(num)

print(f"Square root of {num} after {miliseconds} miliseconds is {result}")

# Task - 5
my_tuple = (True, True, True)
print(all(my_tuple))