#1. Welcome Message
print() # only for ease of reading

print("Welcome to Jim Morton's Coffee!!")

print()

#2. Prompt User to enter number of Cups
while True:
    try:
        numberOfCoffees = int(input("How many coffee's would you like? (Please enter a digit): "))
        print()
        break
    except ValueError:
        print ("Oops! That was not a valid digit.  Please try again...")
        print()

#3. Calculate cost of order
costOfCoffee = 1.25 # if price changes, alter here.
tax = 1.15 # tax rate is 15%
preTax = int(numberOfCoffees) * costOfCoffee # each coffee costs $1.25
totalPrice = preTax * tax #adding sales tax of 15%

#4. Output to user
print("Ok, you said you'd like " + str(numberOfCoffees) + " coffee(s).")
print("So the pre-tax cost of this order is going to be: $%.2f" % preTax)
print("Your total price for your order (including tax) will be: $%.2f" % totalPrice)

print() # ease of reading