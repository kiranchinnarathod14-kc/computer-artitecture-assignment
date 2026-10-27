# Logical shift operations on 8-bit binary numbers

a = "10110110"
print("Original:", a)

for i in range(2):
    a = a[1:] + "0"
    print("Left Shift Step", i + 1, ":", a)

print("Final Left Shift Result:", a)

b = "11010100"
print("\nOriginal:", b)

for i in range(2):
    b = "0" + b[:-1]
    print("Right Shift Step", i + 1, ":", b)

print("Final Right Shift Result:", b)