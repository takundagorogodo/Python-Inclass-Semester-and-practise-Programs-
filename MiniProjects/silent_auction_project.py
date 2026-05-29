import os

def find_winner(bidder_details):
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder

    print(f"\nAll bidder details: {bidder_details}")
    print(f"\nThe winner is {winner} with a bid price of {highest_bid}")

bidders_data = {}
end_of_bidding = False

while not end_of_bidding:
    name = input("Enter name of the bidder: ")
    bid_price = int(input("Enter the bid price: "))

    bidders_data[name] = bid_price

    more_bidders = input("Are there more bidders? Type 'yes' or 'no': ").lower()

    if more_bidders == 'no':
        end_of_bidding = True
        find_winner(bidders_data)
    elif more_bidders == 'yes':
        os.system('cls')  # clears the screen on Windows
