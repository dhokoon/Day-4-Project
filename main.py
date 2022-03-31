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

#Write your code below this line 👇
images = [rock, paper, scissors]
#Greeting user and choice
user_input = int(input("Which one do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n "))

if user_pick >= 3 or user_input < 0:
  print("You typed an invalid number, you lose!")
else:
print(images[user_input])

computer_pick = random.randint(0, 2)
print(f"Computer chose {computer_pick}")
print(images[computer_pick])

  if user_input == 0 and computer_pick == 2:
    print("You win!")
  elif computer_pick == 0 and user_input == 2:
    print("You lose.")
  elif computer_pick > user_input:
    print("You lose.")
  elif user_input > computer_pick:
    print("You win!")
  elif computer_pick == user_input:
    print("It's a draw.")