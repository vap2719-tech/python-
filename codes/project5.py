import os
print("****WELCOME TO THE SILENT AUCTION****")
def find_winner(bidder_details):
    highest_bid=0
    winner=''
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(f"here is the list of the bidders:{bidder_details}")        
    print(f"the winner is {winner} with a bid price is {highest_bid}")





bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("enter what is your name?:\n")
    price=int(input("enter what is your bid price:?\n"))
    bidder_data[name]=price
    more_bidders=input("are there more bidder? type 'yes' or 'no' \n")
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders == 'yes':
        os.system('cls')