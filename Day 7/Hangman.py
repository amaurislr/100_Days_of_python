#this is hangman game
import random
from random import randint

import Hangman_word
import Hagman_ASCII


random_word = random.choice(Hangman_word.word_list)


placeholder = ""
word_lenght = len(random_word)

for position in range (word_lenght):
    placeholder += "_"
print(placeholder)

live = 6
game_over = False
correct_letter = []

while not game_over:

    user_choose = input("Guess the word: ").lower()
    user_try = int

    display = ""
    for letter in random_word:
        if letter == user_choose:
            display += letter
            correct_letter.append(user_choose)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)
    print(f"{live} / 6 lives left")

    if user_choose not in correct_letter:
        live -= 1
        if live == 0:
            game_over = True
            print("You lose. GameOver")

    if "_" not in display:
      print("You win")

    print(Hagman_ASCII.HANGMAN[live])

