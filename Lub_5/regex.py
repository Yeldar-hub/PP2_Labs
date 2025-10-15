# Task - 1
import re
pattern = r'ab*'
while True:
    text = input("> ")

    if text.lower() == "exit":
        print("Выход из программы!")
        break

    if re.fullmatch(pattern, text):
        print(f"Match: {text}")
    else:
        print(f"Not match: {text}")

# Task - 2
import re
pattern = r'ab{2,3}'
while True:
    text = input("> ")

    if text.lower() == "exit":
        print("The end.")
        break

    if re.fullmatch(pattern, text):
        print(f"Match: {text}")
    else:
        print(f"Not match: {text}")

# Task - 3
import re
pattern = r'^[a-z]+_[a-z]+$'
while True:
    text = input("> ")

    if text.lower() == "exit":
        print("The end.")
        break

    if re.fullmatch(pattern, text):
        print(f"Match: {text}")
    else:
        print(f"Not match: {text}")

# Task - 4
import re
pattern = r'^[A-B][a-b]+$'

while True:
    text = input("> ")

    if text.lower() == "exit":
        print("The end.")
        break

    if re.fullmatch(pattern, text):
        print(f"Match: {text}")
    else:
        print(f"Not match: {text}")

# Task - 5
import re
pattern = r'^a.*b$'

while True:
    text = input("> ")

    if text.lower() == "exit":
        print("The end.")
        break

    if re.fullmatch(pattern, text):
        print(f"Match: {text}")
    else:
        print(f"Not match: {text}")

# Task - 6
import re
pattern = r'[ ,.]'

while True:
    text = input("> ")

    if text.lower() == 'exit':
        print("The end.")
        break

    result = re.sub(pattern, ":", text)
    print(result)

# Task - 7
import re

while True:
    text = input("> ")

    if text.lower() == "exit":
        print("The end.")
        break

    words = re.split('_', text)
    camel_case = words[0].lower() + ''.join(w.capitalize() for w in words[1:])
    print("CamelCase:", camel_case)

# Task - 8
import re

while True:
    text = input("> ")

    if text.lower() == "exit":
        print("The end.")
        break

    parts = re.split(r'(?=[A-Z])', text)
    print("Split:", parts)

# Task - 9
import re

while True:
    text = input("> ")

    if text.lower() == "exit":
        print("The end.")
        break

    new_text = re.sub(r'([A-Z])', r' \1', text).strip()
    print("With spaces:", new_text)

# Task - 10
import re

while True:
    text = input("> ")

    if text.lower() == "exit":
        print("The end.")
        break

    snake_case = re.sub(r'([A-Z])', r'_\1', text).lower()
    print("snake_case:", snake_case)
