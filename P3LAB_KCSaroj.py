# Saroj KC
# Oct 10, 2026
# P3LAB
# This program allows the user to enter a money (float) value with two places after the decimal. 

# Get value from user
change = float(input("Enter an amount of money as a float: $"))

print(f"Your change amount is: ${change:.2f}")

change = int(round(change * 100))

# Check if there is no change at all
if change == 0:
    print("No change is needed.")
    exit()

# Determine how many coins are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change

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
