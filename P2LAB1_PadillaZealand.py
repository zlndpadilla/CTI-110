# Zealand Padilla
# 9/16/2026
# P2LAB1
# Circle calculation from user measurements

# Import math module
import math

# Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Make calculations
diameter = radius * 2
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Return values
print(f"The diameter of the circle is {diameter:.1f}\n")
print()
print(f"The circumference of the circle is {circumference:.2f}\n")
print()
print(f"The area of the circle is {area:.3f}\n")