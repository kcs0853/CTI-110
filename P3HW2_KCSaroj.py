# Saroj KC
# Oct 11, 2026
# Assignment Name: P3HW2 - Payroll Calculator
# This program calculates regular pay, overtime pay, and gross pay based on hours worked and pay rate using if/else logic.

"""
PSEUDOCODE:
1. Prompt user to enter employee's name (string)
2. Prompt user to enter hours worked (float)
3. Prompt user to enter employee's hourly pay rate (float)
4. Check if hours worked is greater than 40:
    a. If true:
        - Set overtime hours = hours worked minus 40
        - Calculate overtime pay = overtime hours * (pay rate * 1.5)
        - Calculate regular hours pay = 40 * pay rate
    b. If false (hours <= 40):
        - Set overtime hours = 0.0
        - Set overtime pay = 0.0
        - Calculate regular hours pay = hours worked * pay rate
5. Calculate gross pay = regular hours pay + overtime pay
6. Print employee name and structured layout
"""

# Get inputs from user
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

# Calculate overtime and regular pay
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    reg_pay = 40 * rate
else:
    overtime_hours = 0.0
    overtime_pay = 0.0
    reg_pay = hours * rate

# Calculate gross pay
gross_pay = reg_pay + overtime_pay

print("-" * 39)
print(f"Employee name: {name}")

# Table Headers
print(f'{"Hours Worked":<13} {"Pay Rate":<9} {"OverTime":<10} {"OverTime Pay":<15} {"Regular Pay":<14} {"Gross Pay"}')
print("-" * 80)
print(f"{hours:<13.1f} {rate:<9.1f} {overtime_hours:<10.1f} {overtime_pay:<15.2f} ${reg_pay:<13.2f} ${gross_pay:.2f}")