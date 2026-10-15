# Zealand Padilla
# 10/8/2026
# P3HW2
# This program takes employee information (hours worked, pay rate, and name)

# Get employee's name, hours worked, and pay rate
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))

print(f"{'-' * 120}")

# Calculate pay
reg_pay = pay * hours
ot_hours = hours - 40
if ot_hours > 0:
    ot_pay = ot_hours * pay * 1.5
    gross_pay = reg_pay + ot_pay
else:
    ot_pay = 0
    gross_pay = reg_pay
    ot_hours = 0


# Return results
print(f"Employee name: {name}")
print()
print(f"{'Hours Worked':^18} {'Pay Rate':^18} {'Overtime':^18} {'Overtime Pay':^18}  {'RegHour Pay':^18}  {'Gross Pay':^18}")
print(f"{'-' * 120}")
print(f"{hours:^18} {pay:^18} {ot_hours:^18} {ot_pay:^18} {reg_pay:^18} {gross_pay:^18}")
