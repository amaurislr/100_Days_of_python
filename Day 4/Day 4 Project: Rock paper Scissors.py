#In this day the final project is about design a rock, paper and scissors game
import random

print("Welcome to the Rock, Paper and Scissors game")

items_game = ["Rock", "Paper", "Scissors"]

computer_random_pick = random.randint(a=0, b=2)


user_pick = int(input("choose one of the options ? type 0 for Rock, type 1 Paper and type 2 for Scissors: "))


print (f"The user has pick: {items_game[user_pick]}")

if user_pick == 0:
    # Rock
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif user_pick == 1:
    # Paper
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)


elif user_pick == 2:

    # Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

#this code is for random pick by the computer
print (f"The computer has pick: {items_game[computer_random_pick]}")

if computer_random_pick == 0:
    print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)

elif computer_random_pick == 1:
    print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

elif computer_random_pick == 2:

    # Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

#this part of code is the condition for the user win

if user_pick == 0 and computer_random_pick == 2:
    print("You win!")
elif user_pick == 1 and computer_random_pick == 0:
    print("You win!")
elif user_pick == 2 and computer_random_pick == 1:
    print("You win!")

#this part of code it's the user and computer have a draw
elif user_pick == computer_random_pick:
    print("This is a draw. repeat the pick")

#this part is for decide the user lose

else:
    print ("You Lose. Try again :)")
