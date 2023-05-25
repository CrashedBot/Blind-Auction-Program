from art import logo
import os

isRemaining = True
auction_list = {}
highest_bid = 0

print(logo)

while isRemaining == True:
    name = input("What is your name? ")
    price = int(input("What's your bid? $"))

    auction_list[name] = price

    remaining_player = input("Is there another bidder? (yes/no)").lower()

    if remaining_player == "yes" :
        os.system("clear")

    elif remaining_player == "no":
        for key, value in auction_list.items():
            if value > highest_bid:
                highest_bid = value
                highest_bid_key = key

        isRemaining = False

        print(f"The hightest bid is by {highest_bid_key} of ${highest_bid}")       


