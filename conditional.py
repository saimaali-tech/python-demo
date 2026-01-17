# # if Statement (Basic Condition)
# age = 20

# if age >= 18:
#     print("You are eligible to vote")

# # if - else Statement
# age = 16

# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")

# # if - elif - else (Multiple Conditions)
# marks = 75

# if marks >= 90:
#     print("Grade A")
# elif marks >= 70:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")


# # Nested if (if inside another if)
# age = 22
# citizen = True

# if age >= 18:
#     if citizen:
#         print("You are eligible to vote")
#     else:
#         print("You must be a citizen")
# else:
#     print("You are underage")

# # Logical Operators in Conditionals
# # (and)
# age = 25
# has_id = True

# if age >= 18 and has_id:
#     print("Entry allowed")


# # (or)
# day = "Sunday"

# if day == "Saturday" or day == "Sunday":
#     print("It's a weekend")

#     # (not)
#     is_raining = False

# if not is_raining:
#     print("You can go outside")

# Comparison Operators in Conditions
# x = 10
# y = 20

# if x != y:
#     print("x is not equal to y")

#     # Membership Conditions (in, not in)
# fruits = ["apple", "banana", "mango"]

# if "apple" in fruits:
#     print("Apple is available")

# # (not in)
# if "orange" not in fruits:
#     print("Orange is not available")


# Ternary Conditional (One-Line if)
# age = 17

# status = "Adult" if age >= 18 else "Minor"
# print(status)


#  example
username = "admin"
password = "4567"

if username == "admin" and password == "567889":
    print("Login successful")
else:
    print("Invalid credentials")
