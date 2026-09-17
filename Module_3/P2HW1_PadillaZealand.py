# Zealand Padilla
# 9/17/2026
# P2HW1
# Trip Expense Calculator

print("This program calculates and displays travel expenses")

#Get Trip Details

budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas_cost = float(input("How much do you think you will spend on gas? "))
print()
lodging_cost = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food_cost = float(input("Last, how much do you need for food? "))
print()

#Calculate Travel Expenses & Summarize Trip Details

print("------------Travel Expenses------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'Fuel:':<20} ${gas_cost:.2f}")
print(f"{'Accomodation:':<20} ${lodging_cost:.2f}")
print(f"{'Food:':<20} ${food_cost:.2f}")
print("---------------------------------------")
print()
print(f"{'Remaining Balance:':<20} ${budget - gas_cost - lodging_cost - food_cost:.2f}")
