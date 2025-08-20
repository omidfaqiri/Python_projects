
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


choice_1 = input('you\'r at the crossroad, where do you want to go. "Right" or "left".\n').lower()
if choice_1 == "Left":
    choice_2 = input('You\'ve to a lake, do you want to wait or swim ? \n').lower()
    if choice_2 == "Wait":
        choice_3 = input('You\'ve reached to a room with 3 doors. which door you choose? "Red", "Yellow" or "Blue".\n').lower()
        if choice_3 == "Yellow":
            print("you have found the treasure.")
        elif choice_3 == "Red":
            print(" the room is full of fire. Game over.")
        elif choice_3 == "Blue":
            print("you enter a room of beast. Game over")
        else:
            print("You got the wrong door. Game over")
    else:
        print("You got attached by an angry trout. Game over")
else:
    print("wrong turn, Game Over.")
