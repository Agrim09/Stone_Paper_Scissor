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

import random
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, Type 1 for paper, Type 2 for scissors:"))
if user_choice>2 or user_choice<0:
  print("Invalid Option, Please choose again.")
else:
  print(game_images[user_choice])
 
  print("Computer Chose:")
  computer_choice=random.randint(0,2)
  print(game_images[computer_choice])
  
  if user_choice==0 and computer_choice==2:
    print("You won")
  elif computer_choice>user_choice:
    print("You lost")
  elif computer_choice==user_choice:
    print("Draw")
  else:
    print("You Won")
