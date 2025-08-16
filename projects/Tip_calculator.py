# tip calculator

print("Welcome to Tip calculator")
total_bill = float(input("what was the total bill ?"))
tip = int(input("How much tip would you like to give ? 10, 12 or 15 ?"))
split_bill = int(input("How many people to split the bill ?"))
tip_as_percent = tip / 100
total_tip_amount = total_bill * tip_as_percent
total = total_bill + total_tip_amount
bill_per_person = round(total / split_bill , 2)

print(f"Each person should pay {bill_per_person} $")

