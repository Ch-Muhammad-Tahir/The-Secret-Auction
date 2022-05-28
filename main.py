from replit import clear
from art import logo
print(logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    # Value store in Dictionary
    # {"Tahir":100,"Ayesha",80}
    # Hello World
    for bidder in bids:
        bid_amount = int(bids[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is Your Name?")
    bid_price = input("What is Your bid? $")
    bids[name] = bid_price
    check = input("Are The any other bidders? Type 'YES' or 'NO'.").lower()
    if check == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif check == "yes":
        clear()
