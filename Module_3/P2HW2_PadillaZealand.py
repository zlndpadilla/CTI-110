# Zealand Padilla
# 9/17/2026
# P2HW2
# Grade Summarizer and Calculator

# Get Module Grades From User Input
mod1_grade = float(input("Enter grade for Module 1: "))
mod2_grade = float(input("Enter grade for Module 2: "))
mod3_grade = float(input("Enter grade for Module 3: "))
mod4_grade = float(input("Enter grade for Module 4: "))
mod5_grade = float(input("Enter grade for Module 5: "))
mod6_grade = float(input("Enter grade for Module 6: "))
print()

# Create list that stores grades
grade_collection = [mod1_grade, mod2_grade, mod3_grade, mod4_grade, mod5_grade, mod6_grade]

# Calculate and Print Results
lowest_grade = min(grade_collection)
highest_grade = max(grade_collection)
grade_sum = sum(grade_collection)
grade_average = grade_sum / len(grade_collection)

print(f"{'-'*12}Results{'-'*12}")
print(f"{'Lowest Grade:':<20} {lowest_grade:.2f}")
print(f"{'Highest Grade:':<20} {highest_grade:.2f}")
print(f"{'Sum of Grades:':<20} {grade_sum:.2f}")
print(f"{'Average:':<20} {grade_average:.2f}")
print(f"{'-'*31}")
