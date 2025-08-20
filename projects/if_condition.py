# print("Height requirment riding in rollercoaster. ")
# height = int(input("what is your height? "))
# if height >= 120:
#     age = int(input("How old are you?" ))
#     if age <= 12:
#         print("Pay 5$ ")
#     elif 12 < age <= 18:
#         print("Pay 7$") 
#     elif age >18:
#         print("Pay 12$")
#     print(" select your seat")
# else:
#     print("you does not meet the heigh requirment")


# weight = 85
# height = 1.85
 
# bmi = weight / (height ** 2)
 
# if bmi >= 25:
#     print("overweight")
# elif bmi >= 18.5:
#     print("normal weight")
# else:
#     print("underweight")




print("Height requirement to ride rollercoaster")

height = int(input("How tall are you? "))
if height >= 120:
    print("Welcome")
    age = int(input("How old are you? "))
    
    bill = 0
    if age <= 12:
     print(f"Child tickets are 5$")    
     bill = 5

    elif age <= 18:
     print("Youth tickets are 7$")
     bill = 7
    else:
     print("Adult tickets are  12$")
     bill = 12
    photo = input("Would you like to take photos it costs extra 3$. Y for Yes and N for No.")
    if photo == "y":
        bill += 3
    print(f"Your final bill is: ${bill} ")
else:
    print("Sorry, you do not meet the height requirement")