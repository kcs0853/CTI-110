# Saroj KC
# October 2, 2026
# P2LAB2 - Vehicle MPG Calculator
# Using dictionaries

cars = { 
    "Camaro" : 18.21, 
    "Prius": 52.36,
    "Model S": 110.0,
    "Silverado": 26.0
}

# Get keys from the dictionary
car_keys = list(cars.keys())

print(car_keys)

print(*car_keys, sep = ", ")

# Get a car feom user
car_name = input("Enter a car name: ")

# Get mpg for the given car
car_mpg = cars[car_name]

print(f"The MPG for {car_name} gets {car_mpg} miles per gallon.")

#Get miles from user
miles_driven = float(input(f"How many miles will you drive your {car_name}? "))

#Calculate
gallons_needed = miles_driven / car_mpg

#Display the results
print(f"You will need {gallons_needed:.2f} gallons of gas to drive {miles_driven} miles in the {car_name}.")