import random
import time

# creates a deck
card_categories = ['Hearts','Diamonds','Clubs','Spades']
cards_list = ['Ace','2','3','4','5','6','7','8','9','10','Jack','King','Queen']
deck = [(card, category) for category in card_categories for card in cards_list]

points = 0

# how to get the value of cards
def card_value(card):
    if card[0] in ['Jack','Queen','King']:
        return 10
    elif card[0] == "Ace":
        return 11
    else:
        return int(card[0])

random.shuffle(deck)

# defines the game. The player is given a card, and is told to guess if the value of their current card is higher or lower than the next.

def game(current_card, next_card):
    current_value = card_value(current_card)
    next_value = card_value(next_card)
    print(f"The current card is {current_card}, which has a value of {current_value}.")
    time.sleep(2)
    guess = input("\nDo you think the value of the next card is higher, lower or equal to the current card? ").lower()
    guess_options = ["higher", "lower", "equal"]

    while guess not in guess_options:
        guess = input("\nThat isn't an option! Do you think the value of the next card is higher, lower or equal to the current card? ").lower()

    if guess == "lower":
        if current_value > next_value:
            print(f"\nYou got it correct! {next_card} is lower in value than {current_card}.")
            return True
        else:
            print(f"\nYou got it wrong! {next_card} is higher in value than {current_card}.")
            print("Game Over!")
            return False
    elif guess == "higher":
        if current_value < next_value:
            print(f"\nYou got it correct! {next_card} is higher in value than {current_card}.")
            return True
        else:
            print(f"\nYou got it wrong! {next_card} is lower in value than {current_card}.")
            print("Game Over!")
            return False
    elif guess == "equal":
        if current_value == next_value:
            print(f"\nYou got it correct! {current_card} is equal to {next_card}.")
            return True
        else:
            print(f"\nYou got it wrong! {current_card} isn't equal to {next_card}.")
            print("Game Over!")
            return False

# program to interact with the user

print("Welcome to Higher or Lower!")
time.sleep(1)
play =input("Do you know how to play? (y/n): ").lower()
play_options = ["y", "n"]

while play not in play_options:
    run_again = input("Sorry, that isn't an option! Do you know how to play? (y/n): ").lower()

time.sleep(1)

# game explanation
if play == "n":
    print("Higher or Lower is a guessing game using cards.")
    time.sleep(2)
    print("Cards all have  value from 1 to 11.")
    time.sleep(2)
    print("Aces are worth 11, Kings, Queens and Jacks are worth 10, and the rest of the values are based on the cards number.")
    time.sleep(3)
    print("You will be given a card and told to guess if you think the next card is higher or lower.")
    time.sleep(2)
    print("The game will end if you guess wrong!\n")
    time.sleep(3)

win = True

# whilst the player guess is correct, the game will continue to run. When wrong, the game will end.
# 1 point is added for every correct guess

while win:
    if len(deck) == 0:
        print("The deck is empty. You win!")
        break
    current = deck.pop(0)
    upcoming = deck.pop(0)
    win = game(current, upcoming)
    if win:
        points += 1

time.sleep(1)
print(f"You finished the game with {points} points and {len(deck)} cards remaining.")
