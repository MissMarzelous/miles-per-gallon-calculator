# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Miles Per Gallon Calculator
# DATE WRITTEN: 9/9/2020
# UPDATED:      2026 — fixed incorrect PURPOSE comment, added input validation,
#                      added division-by-zero guard, updated to f-strings
#
# PURPOSE: Calculate the fuel efficiency of a vehicle in miles per gallon (MPG)
#          given the number of gallons used and miles driven.
#
# BEFORE (original): Used toFixed() helper and string concatenation.
#                      
# AFTER  (improved): Correct PURPOSE comment. Uses f-strings and format() for
#                    aligned output. Guards against division by zero. Validates
#                    that numeric input is provided.

# ============================================================
# Declare Variables
# Initialize processed variable
miles_per_gallon = 0.0

# ============================================================
# Input Operations — collect driving data from the user

# Loop until valid numeric input is provided for gallons used
while True:
    try:
        print("How many gallons of gas were used? Enter a numeric value:")
        gallons_used = float(input())
        # Guard against division by zero
        if gallons_used <= 0:
            print("Gallons used must be greater than zero. Please try again.")
        else:
            break  # Valid input received, exit loop
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Loop until valid numeric input is provided for miles driven
while True:
    try:
        print("How many miles were driven? Enter a numeric value:")
        miles_driven = float(input())
        break  # Exit loop once a valid number is entered
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# ============================================================
# Calculate Miles Per Gallon
miles_per_gallon = miles_driven / gallons_used

# ============================================================
# Output Operations — display formatted fuel efficiency report
print("================================================================")
print("CAR MILEAGE INFORMATION")
print("================================================================")
print(f"     Gallons Used = {format(gallons_used,      '11,.2f')}")
print(f"     Miles Driven = {format(miles_driven,      '11,.2f')}")
print(f" Miles Per Gallon = {format(miles_per_gallon,  '11,.2f')}")
print("================================================================")

# END PROGRAM
