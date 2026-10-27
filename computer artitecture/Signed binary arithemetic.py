def binary(n):
    return format(n & 255, '08b')

def signed(b):
    n = int(b, 2)
    return n - 256 if n >= 128 else n

def calculate(a, b):
    x = binary(a)
    y = binary(b)
    result = binary(a + b)
    decimal = signed(result)

    print("First number :", x)
    print("Second number:", y)
    print("Result binary:", result)
    print("Result decimal:", decimal)

    if a + b < -128 or a + b > 127:
        print("Overflow: Yes")
    else:
        print("Overflow: No")
    print()

print("(a) 25 + (+18)")
calculate(25, 18)

print("(b) (-25) + (-18)")
calculate(-25, -18)