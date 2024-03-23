import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


from art import logo
print(logo)

bid_list = []
highest_bid = 0
highest_bidder = None

def make_bid(name,bid):
    new_bid = {}
    new_bid["name"] = name
    new_bid["bid"] = bid
    bid_list.append(new_bid)
    print(bid_list)
    for bid in bid_list:
        bid_value = bid['bid'] 
        if highest_bid < bid_value:
            highest_bid = bid_value
            highest_bidder = highest_bid['name']
    print(f"{highest_bidder} is the highest bidder with {highest_bid}")





name = input("What is your name?\n")
bid = int(input(f"What is your bid?\n$"))
make_bid(name=name, bid=bid)