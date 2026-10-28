# Saroj KC
# Oct 27, 2026
# Assignment Name: P4HW2 - Salary Calculator
# This program calculates payroll information for multiple employees and displays summary totals when finished.

"""
PSEUDOCODE:

1. Initialize totals and employee counter.
2. Ask for employee name.
3. While name is not "Done":
    - Input hours worked and pay rate.
    - Calculate regular pay, overtime pay, and gross pay.
    - Display employee payroll information.
    - Add values to running totals.
    - Increase employee counter.
    - Ask for next employee name.
4. Display total employees, overtime pay, regular pay, and gross pay.
"""

# Initialize totals
employee_count = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Get first employee name
name = input('Enter employee\'s name or "Done" to terminate: ')

# Process employee payroll information
while name != "Done":

    hours = float(input(f"How many hours did {name} work? "))
    rate = float(input(f"What is {name}'s pay rate? "))

    # Calculate pay
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
    else:
        overtime_hours = 0.0
        overtime_pay = 0.0
        regular_pay = hours * rate

    gross_pay = regular_pay + overtime_pay

    # Display employee payroll information
    print()
    print(f"Employee name:    {name}")
    print()
    print("Hours Worked   Pay Rate    OverTime    OverTime Pay      RegHour Pay      Gross Pay")
    print("------------------------------------------------------------------------------------")
    print(f"{hours:<14.1f}{rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<17.2f}${regular_pay:<14.2f}${gross_pay:.2f}")
    print()

    # Update totals
    employee_count += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Ask for next employee
    name = input('Enter employee\'s name or "Done" to terminate: ')

# Display summary totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")