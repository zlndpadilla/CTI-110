# Zealand Padilla
# 9/16/2026
# P2LAB2
# Use dictionary to determine how much gas to travel a specified distance

# Create the dictionary - car names are keys and mpg are values

cars = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

print(cars.keys())
print()

# Get the selected car from user

selected_car = input("Enter a vehicle to see it's mpg: ")
print()

# Get and return the mpg associated with the selected_car

car_mpg = cars[selected_car]

print(f"The {selected_car} gets {car_mpg} mpg.")
print()

# Get the miles planned to drive and calculate gallons necessary

miles_planned = float(input(f"How many miles will you drive the {selected_car}? "))
print()

gallons_needed = miles_planned / car_mpg

# Return calculation

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the Prius {miles_planned} miles.")



