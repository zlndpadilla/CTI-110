# Zealand Padilla
# 10/6/2026
# P3LAB
# Calculate the most efficient way to divide money

# Get the amount of money from user
money_amount = float(input("Enter the amount of money as a float: $"))

# Round the value to an integer
money_amount = round(money_amount * 100)

# Determine amounts of currency needed
num_dollars = money_amount // 100
money_amount = money_amount - (num_dollars * 100)

num_quarters = money_amount // 25
money_amount = money_amount - (num_quarters * 25)

num_dimes = money_amount // 10
money_amount = money_amount - (num_dimes * 10)

num_nickels = money_amount // 5
money_amount = money_amount - (num_nickels * 5)

num_pennies = money_amount

# Print the results
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
    else:
        print(f"{num_nickels} Nickels")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")

