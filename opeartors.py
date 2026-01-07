# Arithmetic Operators
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333
print(a % b)    # 1
print(a ** b)   # 1000
print(a // b)   # 3


# Assignment Operators
x = 10
x += 5
print(x)   # 15

x *= 2
print(x)   # 30


# Comparison (Relational) Operators

a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True


# Logical Operators
x = 5

print(x > 3 and x < 10)   # True
print(x > 10 or x < 8)    # True
print(not(x > 3))         # False

# Bitwise Operators
a = 5   # 0101
b = 3   # 0011

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6
print(a << 1)  # 10
print(a >> 1)  # 2

# //Membership Operators
numbers = [1, 2, 3, 4, 5]

print(3 in numbers)        # True
print(10 not in numbers)  # True
