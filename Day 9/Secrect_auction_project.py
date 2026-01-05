from importlib.resources import open_text

import action_acsii

#print acsii art
print(f"{action_acsii.auction_acsii_art}")

bids = {}

continues = ""

# that's the input to save the valor of name of the person is bid and how many that person bid

def find_highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidders in bidding_dictionary:
        bid_amount = bidding_dictionary[bidders]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidders

        print(f"the highest bridder {winner} and the price {highest_bid}")

while continues != "no":

    name = input("What's your name: ")
    bid_price = int(input("What's the bid price: "))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    continues = other_bidders

    bids[name] = bid_price

    if other_bidders == "no":
        find_highest_bid(bids)









