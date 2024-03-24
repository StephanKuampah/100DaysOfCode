import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


from art import logo
print(logo)

bid_list = []



def make_bid(name,bid):
    new_bid = {}
    new_bid["name"] = name
    new_bid["bid"] = bid
    bid_list.append(new_bid)


should_continue = True
while should_continue:
    highest_bid = 0
    highest_bidder = None
    for bid in bid_list:
        bid_value = bid['bid'] 
        if highest_bid < bid_value:
            highest_bid = bid_value
            highest_bidder = bid['name']
        
    name = input("What is your name?\n")
    bid = int(input(f"What is your bid?\n$"))
    make_bid(name=name, bid=bid)
    result = input("Are there any other bidders? 'yes' to bid again or 'no' to exit\n")
    if result == 'yes':
        clear_terminal()

    else:
        should_continue = False
        clear_terminal()
        print(f"{highest_bidder} is the highest bidder with ${highest_bid}")



        
    

