# Zealand Padilla
# 10/8/2026
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print()

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest , sum, and average for grades
lowest_grade = min(grades)
highest_grade = max(grades)
grade_sum = sum(grades)
grade_average = sum(grades) / len(grades)

# Determine letter grade for average and return results
print(f"{'-'*12}Results{'-'*12}")
print(f"{'Lowest Grade:':<20} {lowest_grade:.2f}")
print(f"{'Highest Grade:':<20} {highest_grade:.2f}")
print(f"{'Sum of Grades:':<20} {grade_sum:.2f}")
print(f"{'Average:':<20} {grade_average:.2f}")
print(f"{'-'*31}")
if grade_average >= 90:
    print("Your grade is: A")
elif grade_average >= 80:
    print("Your grade is: B")
elif grade_average >= 70:
    print("Your grade is: C")
elif grade_average >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")