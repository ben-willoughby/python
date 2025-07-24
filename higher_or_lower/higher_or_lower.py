import art
import random
import game_data

score = 0
lost = False

compare_a = random.choice(game_data.data)

compare_b = random.choice(game_data.data)

print(art.logo)

while not lost:

    print(f"Compare A: {compare_a.get("name")}, a {compare_a.get("description")}, from {compare_a.get("country")}")
    print(art.vs)

    if compare_a == compare_b:
        compare_b = random.choice(game_data.data)

    print(f"Against B: {compare_b.get("name")}, a {compare_b.get("description")}, from {compare_b.get("country")}")

    answer = input("Who has more followers? Type 'A' or 'B': ")

    # work out correct answer
    if compare_a.get("follower_count") > compare_b.get("follower_count"):
        correct_answer = "a"
    else:
        correct_answer = "b"

    # work out if user is correct
    if answer.lower() != correct_answer:
        lost = True
        print("\n" * 100)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        compare_a = compare_b
        score += 1
        print("\n" * 100)
        print(art.logo)
        print(f"You're right! Current score: {score}.")
