# Zealand Padilla
# 9/15/2026
# P1HW2
# Trip Expense Calculator

print("This program calculates and displays travel expenses")

#Get Trip Details

budget = int(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas_cost = int(input("How much do you think you will spend on gas? "))
print()
lodging_cost = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food_cost = int(input("Last, how much do you need for food? "))
print()

#Calculate Travel Expenses & Summarize Trip Details

print("------------Travel Expenses------------")
print("Location: ", destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas_cost)
print("Accomodation: ", lodging_cost)
print("Food: ", food_cost)
print()
print("Remaining Balance: ", budget - gas_cost - lodging_cost - food_cost)
