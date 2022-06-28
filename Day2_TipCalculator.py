print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
tip = float(input("How much tip would you like to give? 10%, 12%, 15%, 20%? "))
people = float(input("How many people will split the bill? "))

cost = round(bill * (1+(tip/100))/people, 2)
print(f"Each person should pay {cost}")

