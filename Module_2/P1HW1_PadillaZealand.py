# Zealand Padilla
# 9/15/2026
# P1HW1
# Perform math calculations

print("----Calculating Exponents----")

print()
print()

#Get integer values from user
base_value = int(input("Enter an integer as the base value: "))
exponent_value = int(input("Enter an integer as the exponent: "))

#Calculate the result
exponent_result = base_value ** exponent_value

print()
print()

#Return result
print(base_value, "raised to the power of", exponent_value, "is", exponent_result, "!!")

print()
print()

print("----Addition and Subtraction----")

print()
print()

#Get integer values from user
starting_value = int(input("Enter a starting integer: "))
additive_value = int(input("Enter an integer to add: "))
subtractive_value = int(input("Enter an integer to subtract: "))

#Calculate the result
arithmetic_result = starting_value + additive_value - subtractive_value

print()
print()

#Return result
print(starting_value, "+", additive_value, "-", subtractive_value, "is equal to", arithmetic_result)
