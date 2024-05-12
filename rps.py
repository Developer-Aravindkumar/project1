import random
rock='''
     ______
---'   ____)
      (_____)
      (______)
      (_____)
---.__(__)
'''
paper='''
    ______
---'  ____)____
         ______)__
         _________)
        ________)
---'_________)
'''
scissors='''
    ________
---'   _____)___
           _____)
         _________)
      (______)
---.__(_____)
'''
images=[rock,paper,scissors]
user_choice=int(input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
if user_choice >=3 or user_choice <0:
    print("you typed an INVALID NUMBER, you lose!")
else:
    print(images[user_choice])
    computer_choice=random.randint(0,2)
    print("Computer chose:")
    print(images[computer_choice])
    if user_choice==0 and computer_choice==2:
        print("You won!")
    elif computer_choice==0 and user_choice==2:
        print("You lose")
    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice >computer_choice:
        print("You won")
    elif computer_choice== user_choice:
        print("It's a draw")
    else:
        print("the end")


