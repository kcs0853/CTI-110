# KC Saroj
# October 2, 2026
# P2HW1 - Travel Budget Calculator
# A program that takes travel budget inputs and displays a neatly formatted summary table with aligned columns.

print("This program calculates and displays travel expenses")
print() 
    
# User inputs
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
    
# Financial math
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses
    
# Formatted display output
print()
print("------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${hotel:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("----------------------------------------")
print()
print(f"{'Remaining Balance:':}${remaining_balance:.2f}")