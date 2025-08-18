print("This Game has a height requirments")
height = int(input("How tall are you in cm? "))
bill = 0
if height >= 120:
    print("Welcome")
    age = int(input("How old are you? "))
    if age <= 12:
        print("Child tickets are 5$ ")
        bill = 5
    elif age <= 18:
        print("Yougth tickets are 7$ ")
        bill = 7
    else:
        print("Adult tickets are 12$ ")
        bill = 12
    photo = input("Do you like to take photos for an extra 3$? Y for yes and N for no.")
   
    if photo == "y":
        bill += 3
    print(f"Your final bill is: ${bill}")
else:
    print("Sorry, you do not meet height requirement of the game")
