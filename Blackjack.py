import random
card_categories = ['Hearts','Diamonds','Clubs','Spades']
cards_list = ['Ace','2','3','4','5','6','7','8','9','10','Jack','King','Queen']
deck = [(card, category) for category in card_categories for card in cards_list]

def card_value(card):
    if card[0] in ['Jack','Queen','King']:
        return 10
    elif card[0] == "Ace":
        return 11
    else:
        return int(card[0])

random.shuffle(deck)
player_card = [deck.pop(), deck.pop()]
dealer_card = [deck.pop(), deck.pop()]
while True:
    player_score = sum(card_value(card) for card in player_card)
    dealer_score = sum(card_value(card) for card in dealer_card)
    print(f"Player has the cards {player_card}.")
    print(f"Player has the score {player_score}.")
    print("\n")
    choice = input("type play to request another card, type stop to stop - ").lower()
    if choice == "play":
        new_card = deck.pop()
        player_card.append(new_card)
    elif choice == "stop":
        break
    else:
        print("Invalid choice. Please try again.")
        continue


while dealer_score < 17:
    new_card = deck.pop()
    dealer_card.append(new_card)
    dealer_score += card_value(new_card)

if dealer_score > 21:
    print(f"Dealer has the cards {dealer_card}.")
    print(f"Dealer has the score {dealer_score}.")
    print(f"Player has the cards {player_card}.")
    print(f"Player has the score {player_score}.")
    print("Player wins! (The dealers score exceeds 21)")


if player_score > 21:
    print(f"Dealer has the cards {dealer_card}.")
    print(f"Dealer has the score {dealer_score}.")
    print(f"Player has the cards {player_card}.")
    print(f"Player has the score {player_score}.")
    print("Dealer wins! (The players score exceeds 21)")

elif dealer_score > player_score:
    print(f"Dealer has the cards {dealer_card}.")
    print(f"Dealer has the score {dealer_score}.")
    print(f"Player has the cards {player_card}.")
    print(f"Player has the score {player_score}.")
    print("Dealer wins! (The dealers score is higher than the players)")

elif player_score > dealer_score:
    print(f"Dealer has the cards {dealer_card}.")
    print(f"Dealer has the score {dealer_score}.")
    print(f"Player has the cards {player_card}.")
    print(f"Player has the score {player_score}.")
    print("PLayer wins! (The players score is higher than the dealers)")

else:
    print(f"Dealer has the cards {dealer_card}.")
    print(f"Dealer has the score {dealer_score}.")
    print(f"Player has the cards {player_card}.")
    print(f"Player has the score {player_score}.")
    print("Its a tie.")

