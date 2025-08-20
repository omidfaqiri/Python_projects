print("Welcome to first Python pizza store")
bill = 0
pizza_size = input("What size pizza do you want? S for small, M for medium and L for large. ")
if pizza_size == "s":
    print("You have selected small size pizza for $15 ")
    bill = 15
    
    # Add pepperoni
    pepperoni = input("Do you want to add pepperoni for $2? (Y for yes and N for no)")
    if pepperoni == "y":
        bill += 2

        #Add cheese
    cheese = input("Do you want to add cheese with any size pize for $1? (Y for yes and N for no) ")
    if cheese == "y":
        bill += 1

elif pizza_size == "m":
    print("You have selected medium size pizza for $ 20 ")
    bill = 20
 # Add pepperoni
    pepperoni = input("Do you want to add pepperoni for $2? (Y for yes and N for no)")
    if pepperoni == "y":
        bill += 2

        #Add cheese
        cheese = input("Do you want to add cheese with any size pize for $1? (Y for yes and N for no) ")
    if cheese == "y":
        bill += 1

elif pizza_size == "l":
    print("You have selected large size pizza for $25 ")
    bill = 25

    # Add pepperoni
    pepperoni = input("Do you want to add pepperoni for $2? (Y for yes and N for no)")
    if pepperoni == "y":
        bill += 2

        #Add cheese
        cheese = input("Do you want to add cheese with any size pize for $1? (Y for yes and N for no) ")
    if cheese == "y":
        bill += 1
else:
    print("Please select correct size. S for small, M for medium and L for large. ")
print(f"Your final bill is ${bill}")
