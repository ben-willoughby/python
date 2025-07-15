import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while play == "y":
    print("\n" * 100)
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    your_score = your_cards[0] + your_cards[1]
    computer_score = computer_cards[0] + computer_cards[1]

    print(f"Your cards: {your_cards}, current score: {your_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    another_card = ""

    print(f"Test score: {your_score}")

    if your_score == 21 and len(your_cards) == 2:
        your_score = 0
        print("Win with a Blackjack 😎")
    else:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    while your_score !=0 and your_score < 22 and another_card == "y":
        your_cards.append(random.choice(cards))
        your_score += your_cards[-1]
        print(f"Your cards: {your_cards}, current score: {your_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if your_score < 22:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    while computer_score <= 17 and your_score != 0:
        computer_cards.append(random.choice(cards))
        computer_score += computer_cards[-1]


    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    total_cards = len(your_cards)

    # Win/lose conditions
    if your_score != 0:
        if your_score == computer_score:
            print("Draw 🙃")
        elif your_score <= 21 and computer_score > 21:
            print("Opponent went over. You win 😁")
        # elif your_score > 21 and computer_score == your_score:
        #     print("")
        elif your_score > 21:
            print("You went over. You lose 😭")
        elif your_score < 21:
            your_distance_from_blackjack = 21 - your_score
            computer_distance_from_blackjack = 21 - computer_score
            if your_distance_from_blackjack < computer_distance_from_blackjack:
                print("You win 😃")
            elif your_distance_from_blackjack > computer_distance_from_blackjack:
                print("You lose 😤")
            else:
                print("Draw 🙃")

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()