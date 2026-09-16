# Saroj KC
# September 15, 2026
# Assignment Name: P1HW1
# Description: A mathematical calculator doing exponents and basic algebra based on user inputs.

# calculate exponents

print("----- Calculating Exponents-----")
print()

base = int(input("Enter a base number: "))
exponent = int(input("Enter a exponent: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result, "!!")

# calculate addition and subtraction
print("-----Addition and Subtraction-----")
print()

num1 = int(input("Enter a first integer to add: "))
num2 = int(input("Enter a second integer to add: "))
num3 = int(input("Enter a third integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result, "!!")