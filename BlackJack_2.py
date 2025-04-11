import random
# links ranks and values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

# prints info
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

# shuffles the deck
    def shuffle(self):
      random.shuffle(self.deck)

# deals a card
    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_cards(self, card):
        self.cards.append(card)
        self.value += values[card.rank]


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0
    #    self.total = earnings

    def win_bet(self):
        self.total += self.bet
        return self.total

    def lose_bet(self):
        self.total -= self.bet
        return self.total


def take_bet(chip):
    chip.bet = int(input("How many chips would you like to bet? "))

    while chip.bet > chip.total:
        print(f"Sorry, your bet can't exceed {chip.total} chips.")
        chip.bet = int(input("How many chips would you like to bet? "))



def hit(deck_cards, hand):
    hand.add_cards(deck_cards.deal())

def hit_or_stand(deck_cards, hand):
    global playing
    h_s = input("Would you like to hit or stand? (h/s): ")

    while True:
        if h_s == 'h':
            hit(deck_cards, hand)
        elif h_s == 's':
            print("Player stands. The dealer will now play.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("(hidden)")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(chips):
    global earnings
    print("Player busts!")
    chips.lose_bet()
    earnings = chips.lose_bet()

def player_wins(chips):
    global earnings
    print("Player wins!")
    chips.win_bet()
    earnings = chips.win_bet()

def dealer_busts(chips):
    global earnings
    print("Dealer busts!")
    chips.win_bet()
    earnings = chips.win_bet()

def dealer_wins(chips):
    global earnings
    print("Dealer wins!")
    chips.lose_bet()
    earnings = chips.lose_bet()

def draw():
    print("It's a draw!!")





while True:
    print("Welcome to Blackjack!")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())

    player_bet = Chips()
    take_bet(player_bet)
    earnings = Chips()

    while playing:


        show_some(player_hand, dealer_hand)
        hit_or_stand(deck, player_hand)

    if player_hand.value > 21:
        player_busts(player_bet)

        print(f"You currently have {earnings} chips left.")

        new_game = input("Would you like to play again? (y/n): ").lower()

        if new_game == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break

    else:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

    show_all(player_hand, dealer_hand)

    if dealer_hand.value > 21:
        dealer_busts(player_bet)

    elif dealer_hand.value > player_hand.value:
        dealer_wins(player_bet)


    elif dealer_hand.value < player_hand.value:
        player_wins(player_bet)

    else:
        draw()


    print(f"You currently have {earnings} chips left.")

    new_game = input("Would you like to play again? (y/n): ").lower()

    if new_game == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break

