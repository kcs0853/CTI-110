# Saroj KC
# September 15, 2026
# Assignment Name: P1HW2
# Description: A travel budget calculator that takes user inputs for budget, destination, and expenses, calculates total costs, and outputs the remaining balance.

print("This program calculates and displays travel expenses")
print()

# Get inputs from user
budget = int(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()

# Perform calculations
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

# Display results
print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accomodation: {hotel}")
print(f"Food: {food}")
print()
print(f"Remaining Balance: {remaining_balance}")
