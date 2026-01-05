import random
import Blackjack_acssi

#print(Blackjack_acssi.black_jack_art)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_hand():
    card = random.choice(cards)
    return card

def win_or_loose_rules():
    if sum(user_hand) == sum(cpu_hand):
        print(f"Your final hand is: {cpu_hand} Your final score is: {sum(user_hand)} \n it's a draw")
    elif sum(user_hand) > sum(cpu_hand):
        print(f"Your final hand is: {cpu_hand} Your final score is: {sum(user_hand)} \nYou win")
    else:
        print(f"Your final hand is {user_hand} Your final score is: {sum(user_hand)} You Loose")

cpu_hand = []
user_hand = []

for hand in range(2):
    cpu_hand.append(random_hand())
    user_hand.append(random_hand())

sum_cpu_hand = sum(cpu_hand)
sum_user_hand = sum(user_hand)

print( f"Your cards: {user_hand}, your current score: {sum_cpu_hand}")



add_card = True

while add_card:
    ask_draw_card = input("Do you want to add another card? (Y/N): ").lower()
    if ask_draw_card == "y":
        cpu_hand.append(random_hand())
        user_hand.append(random_hand())
        print(sum_cpu_hand)
        if sum_cpu_hand > 21:
            print(f"Your final hand is: {cpu_hand} Your final score is: {sum_cpu_hand} \nYou loose😒")
            add_card = False
