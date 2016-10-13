"""
Wage Calculator
Intro to Programming
In-Class Challenge
Brad Penney
"""

# Declare & Initialize Variables
regularHours = 0
regularEarnings = 0
overtimeHours = 0
overtimeEarnings = 0
totalEarnings = 0

# Program Introduction
print("\nWelcome to the Wage Calulator! \n")

# Get Input, Declare & Initialize Necessary Variables
hoursWorked = float(input("Please enter how many hours you worked in the past week.  Please enter a digit: "))
perHourRate = float(input("Please enter how much you make per hour in a dollar amount (digits): $"))

# Determine if User Worked Overtime
if (hoursWorked > 40):
    overtimeHours = hoursWorked - 40
    regularHours = 40
else:
    regularHours = hoursWorked

# Calculate Earnings
regularEarnings = regularHours * perHourRate
overtimeEarnings = overtimeHours * perHourRate * 1.5 # Earnings for overtime are X1.5
totalEarnings = regularEarnings + overtimeEarnings

# Output Earnings to User
print("\nYour overtime earnings are: ${:.2f}".format(overtimeEarnings))
print("Your regular earnings are: ${:.2f}".format(regularEarnings))
print("\nYour total earnings are: ${:.2f}".format(totalEarnings))