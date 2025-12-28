auction = {}

def highest_bid(bid):
    find = max(bid.values())
    for key in bid:
        if bid[key] == find:
            print("Winner", key, "With bid", bid[key])

morebids = input("Enter 'yes' if more bidders, 'no' if none remaining: ")
while morebids.lower() == 'yes':
    user_name = input("Enter the name of the bidder: ")
    user_price = int(input("Enter the bid price of the user: "))
    auction[user_name] = user_price
    morebids = input("Enter 'yes' if more bidders, 'no' if none remaining: ")
    print("\n" * 50)


highest_bid(auction)