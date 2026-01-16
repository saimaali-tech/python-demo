# What is a Function
# A function is a reusable block of code that performs a specific task.

# def add():
#     a = 5
#     b = 3
#     print(a + b)

# add()

# def greet(name):
#     print("Hello", name)

# greet("Saima")

# # Functions with Multiple Parameters
# def add(a, b):
#     print(a + b)

# add(10, 20)

# # Return Statement
# def add(a, b):
#     return a + b

# result = add(4, 6)
# print(result)

# Default Parameters
def greet(name="User"):
    print("Hello", name)

greet()
greet("Ali")

# Keyword Arguments
def student(name, age):
    print(name, age)

student(age=22, name="Saima")

