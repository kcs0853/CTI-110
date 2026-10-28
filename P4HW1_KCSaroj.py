# Saroj KC
# October 27, 2026
# P4HW1
# This program collects test scores from the user, validates the scores, drops the lowest score, calculates the average of the remaining scores, and displays the corresponding letter grade.

# PSEUDOCODE
# Ask user how many scores they want to enter
# Create an empty list to store scores
# Use a loop to collect the scores
# Validate each score is between 0 and 100
# If invalid, repeatedly ask for a valid score
# Add valid scores to the list
# Find the lowest score
# Remove the lowest score from the list
# Calculate the average of the remaining scores
# Determine the letter grade based on the average
# Display results

# Ask user for the number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Create list to store entered scores
score_list = []

# Collect scores
for i in range(1, num_scores + 1):

    score = float(input(f"\nEnter score #{i}: "))

    # Validate score
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))

    # Add valid score to list
    score_list.append(score)

# Find lowest score
lowest_score = min(score_list)

# Create modified list by removing lowest score
modified_list = score_list.copy()
modified_list.remove(lowest_score)

# Calculate average
average = sum(modified_list) / len(modified_list)

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n")
print("--------------Results--------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {modified_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------")