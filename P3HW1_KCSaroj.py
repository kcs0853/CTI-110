# Saroj KC
# Oct 08, 2026
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades
Low_Grade = min(grades)
High_Grade = max(grades)
Total_sum = sum(grades)
Average = Total_sum / len(grades)

# Display results
print("\n------------Results------------")
print(f"{'Lowest Grade:':<18}{Low_Grade}")
print(f"{'Highest Grade:':<18}{High_Grade}")
print(f"{'Sum of Grades:':<18}{Total_sum}")
print(f"{'Average:':<18}{Average:.2f}")
print("---------------------------------")

# Determine letter grade for average
if Average >= 90:
    print('Your grade is: A')
elif Average >= 80:
    print('Your grade is: B')
elif Average >= 70:
    print('Your grade is: C')
elif Average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')