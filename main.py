import random

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

choices = [rock, paper, scissors]

while True:
  player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. -1 to Quit.\n"))
  
  computer_choice = random.randint(0, 2)

  if player_choice == -1:
    break

  print(choices[player_choice])
  print("Computer chose:")
  print(choices[computer_choice])

  if player_choice == computer_choice:
    print("You tie")
  elif player_choice == 0:
    if computer_choice == 1:
      print("You lose")
    else:
      print("You win")
  elif player_choice == 1:
    if computer_choice == 0:
      print("You win")
    else:
      print("You lose")
  else:
    if computer_choice == 1:
      print("You win")
    else:
      print("You lose")