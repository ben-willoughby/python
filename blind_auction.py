more = "yes"
price = {}
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
while more == "yes":
# Ask the user for input

    name = input("What is your name?: ")
    bid = int(input("What's your bid: $"))

    # Save data into dictionary {name: price}

    price[name] = bid

    # Ask if new bids need to be added

    more = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()

    print("\n" * 100)

# Compare bids in dictionary

top_bid = max(price.values())
top_bidder = max(price, key=price.get)

print(f"The winner is {top_bidder} with a bid of ${top_bid}")