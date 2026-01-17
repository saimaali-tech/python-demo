# Loop through a list
# fruits = ["apple", "banana", "mango"]

# for fruit in fruits:
#     print(fruit)


# # Loop through a string
# name = "Python"

# for char in name:
#     print(char)


# # Loop with range()
# for i in range(5):
#     print(i)


# # range(stop)
# range(5)   # 0 to 4
# range(2, 6)  # 2 to 5
# range(1, 10, 2)  # 1, 3, 5, 7, 9

# while Loop in Python
i = 1

while i <= 5:
    print(i)
    i += 1

# break Statement
for i in range(10):
    if i == 5:
        break
    print(i)

# continue Statement
for i in range(5):
    if i == 2:
        continue
    print(i)

# continue Statement
for i in range(6):
    if i == 5:
        continue
    print(i)

# Nested Loops (Loop inside a Loop)
for i in range(4, 6):
    for j in range(1, 4):
        print(i, j)

# Loop with else (Less Known but Important)
for i in range(8):
    print(i)
else:
    print("Loop completed successfully")
