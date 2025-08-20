rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [rock, paper, scissors]

import random
user_input = int(input("choose a number from 0 to 2. 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if user_input >= 0 and user_input < 3:
    print(game_images[user_input])
computer_input = random.randint(0,2)
print("computer choose ")
print(game_images[computer_input])
if computer_input == 0 and user_input == 2:
    print("You loose!")
elif user_input >= 3 or user_input < 0:
    print("invalid number, you loose!")
elif computer_input > user_input:
    print("You loose!")
elif computer_input == user_input:
    print("It's a draw!")
elif computer_input == 2 and user_input == 0:
    print("You win!")
elif user_input > computer_input:
    print("You win!")
