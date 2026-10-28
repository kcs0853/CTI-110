# Name: Saroj KC
# Date: 10/27/2026
# Assignment: P4LAB2
# Description: Generates a multiplication table for a user-entered integer and allows the user to run the program multiple times.

# Pseudocode:
# 1. Start a while loop to repeat the program.
# 2. Ask the user to enter an integer.
# 3. If the integer is negative:
#       Display an error message.
# 4. Otherwise:
#       Use a for loop to display the multiplication
#       table from 1 through 12.
# 5. Ask the user if they want to run the program again.
# 6. If the user enters "yes", repeat the program.
# 7. If the user enters "no", end the program.
# 8. Display an exit message.

run_again = "yes"

while run_again.lower() == "yes":

    number = int(input("Enter an integer: "))

    if number >= 0:

        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")

    else:
        print("This program does not handle negative values")

    run_again = input("\nWould you like to run the program again? ")

print("\nExiting program...")