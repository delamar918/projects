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

print("Let's play rock, paper, scissors!")
player_choice = int(input("Type 0 for rock, 1 for paper, or 2 for scissors\n"))
if player_choice > 2 or player_choice < 0:
    print("You typed an invalid number! You lost!")
else:
    if player_choice == 0:
        print("Your choice was rock")
        print(rock)
    elif player_choice == 1:
        print("Your choice was paper")
        print(paper)
    elif player_choice == 2:
        print("Your choice was scissors")
        print(scissors)
    
    computer_choice = random.randint(0,2)
    
    if computer_choice == 0:
        print("Computer chose rock")
        print(rock)
    elif computer_choice == 1:
        print("Computer chose paper")
        print(paper)
    elif computer_choice == 2:
        print("Computer chose scissors")
        print(scissors)
    
    
    if player_choice == 0 and computer_choice == 2:
        print("You won!")
    elif player_choice == 2 and computer_choice == 1:
        print("You won!")
    elif player_choice == 1 and computer_choice == 0:
        print("You won!")
    elif player_choice == computer_choice:
        print("It's a draw.")
    else:
        print("You lost.")
