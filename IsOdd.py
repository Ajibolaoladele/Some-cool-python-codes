"""
DetermineIfOdd Function
"""

# Determines if odd using modulo
def isOdd(num):
    if (num % 2 == 0):
        return "even"
    if (num % 2 != 0):
        return "odd"

# Gather input numbers from user
firstNum = int(input("Please enter a number: "))
secondNum = int(input("Please enter a number: "))
thirdNum = int(input("Please enter a number: "))

# Output results to user
print("\nThe first number is " + isOdd(firstNum))
print("The second number is " + isOdd(secondNum))
print("The third number is " + isOdd(thirdNum))


