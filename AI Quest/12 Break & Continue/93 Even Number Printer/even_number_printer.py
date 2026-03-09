# 93. Even Number Printer: Write a Python program to print all even numbers from 1 to 20. Use a `for` loop and `continue` to skip odd numbers.

for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)