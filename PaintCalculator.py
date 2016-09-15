#This program calculates the number of gallons
# of paint required to paint a rectangular room
# Advised by salesperson each gallon covers 150sqf

# math functions for rounding
import math

print()
# import information about the room
roomWidth = input("What is the width of the room in feet? (Enter a digit): " )

roomLength = input("What is the length of the room in feet? (Enter a digit): ")

roomHeight = input("What is the height of the room in feet? (Enter a digit): ")

shortWallArea = int(roomWidth) * int(roomHeight)
longWallArea = int(roomLength) * int(roomHeight)

totalSquareFootage = (shortWallArea + longWallArea)*2

# each gallon of paint covers 150 square feet
gallonsOfPaint = math.ceil(totalSquareFootage/150)

print()
print("Each gallon of paint covers 150 square feet of wall.")
print("The total number of gallons of paint required will be: " ,gallonsOfPaint)

print()
