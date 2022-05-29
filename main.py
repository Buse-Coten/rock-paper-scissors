import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
invalid = """
_      ___ _______
|  _,-' _ `\______)
|~'    ' `\()
|       (____)
|      (_____)
|--.____(___)
"""

game_images = [rock, paper, scissors]
user = int(input("Which one do you choose?\nType 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user >= 3 or user < 0:
  print("You typed an invalid number. You lose!\n"+invalid)
else:
  print(game_images[user])
  
  computer = random.randint(0,2)
  print(f"Computer choose \n{computer}\n"+game_images[computer])
  
  if computer == 0 and user == 2:
    print("You lose!")
  elif computer == 2 and user == 0:
    print("You win!")
  elif computer > user:
    print("You lose!")
  elif user > computer:
    print("You win!")
  elif computer == user:
    print("It's a draw!")