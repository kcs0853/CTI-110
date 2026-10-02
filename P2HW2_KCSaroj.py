# Saroj KC
# October 2, 2026
# P2HW2 - List
# A program that stores module test grades in a list and calculates the lowest, highest, sum, and average of those grades with aligned formatting.

# Step 1: Prompt for Module Grades using separate inputs
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Step 2: Store the elements in a descriptively named list
module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]

# Step 3: Perform calculations using list functions (No loops or if-statements)
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

# Step 4: Display formatted results to match the required structure exactly
print()
print("------------Results------------")

# Left-aligning the labels to 20 spaces ensures the numeric values align perfectly
print(f"{'Lowest Grade:':<20}{lowest_grade}")
print(f"{'Highest Grade:':<20}{highest_grade}")
print(f"{'Sum of Grades:':<20}{sum_of_grades}")
print(f"{'Average:':<20}{average_grade:.2f}")
print("----------------------------------------")