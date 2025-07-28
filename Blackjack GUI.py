import tkinter as tk
import random

# links ranks and values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

# booleans for playing and chips running out
playing = True
chips_ran_out = False

# empty function for when buttons aren't needed
def none():
    pass

# window configuration

window = tk.Tk()
window.geometry("527x400")
window.config(padx=10, pady=10)
window.title("Welcome to BlackJack!")

# label to display the game outcome
bottom_frm = tk.Frame(height=6, width=72)
game_status = tk.Label(master=bottom_frm, text="You're currently betting chips. Finish doing so before playing.", bg="white", justify="center", height=5, width=58, relief="raised")
button_frame = tk.Frame(master=bottom_frm)
yes_button = tk.Button(master=button_frame, height=2, width=12, bg="white", text="")
no_button = tk.Button(master=button_frame, height=2, width=12, bg="white", text="")

# labels for player and dealer cards
player_cards_lbl = tk.Label(text="player cards will appear here.", height=15, width=34, padx=5, pady=5, relief="raised", bg="white")
player_total_lbl = tk.Label(text="Player Total: 0", height=1, width=34, padx=5, pady=5, relief="raised", bg="white")

dealer_cards_lbl = tk.Label(text="dealer cards will appear here.", height=15,width=34,  padx=5, pady=5, relief="raised", bg="white")
dealer_total_lbl = tk.Label(text="Dealer Total: 0", height=1,width=34, padx=5, pady=5, relief="raised", bg="white")


bottom_frm.grid(row=6, column = 0, columnspan=2, pady=4)
game_status.pack(side=tk.LEFT, padx=2, pady=2)
button_frame.pack(side=tk.RIGHT)
yes_button.pack(side=tk.TOP, padx=2, pady=2)
no_button.pack(side=tk.BOTTOM)

player_cards_lbl.grid(row=1, column=0, rowspan=2, sticky="w", padx=2, pady=2)
player_total_lbl.grid(row=2, column=0, sticky="sw", padx=2, pady=2)

dealer_cards_lbl.grid(row=1, column=1, rowspan=2, sticky="w", padx=2, pady=2)
dealer_total_lbl.grid(row=2, column=1, sticky="sw", padx=2, pady=2)

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

# prints info
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
# creates the deck
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

# shuffles the deck
    def shuffle(self):
      random.shuffle(self.deck)

    def __str__(self):
        for card in self.deck:
            print(card)
            print("\n")

# deals one card
    def deal(self):
        return self.deck.pop()


class Hand:
# the hand of the player/ computer
    def __init__(self):
        self.cards = []
        self.value = 0

# adds cards to hand and gets the total
    def add_cards(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def clear(self):
        self.cards = []
        self.value = 0


class Chips:
# the starting number of chips is 100.
# the bet is set to 0.
    def __init__(self):
        self.total = 100
        self.bet = 0

# if the bet is won, adds the bet to total
    def win_bet(self):
        self.total += self.bet
        return self.total

# if the bet is lost, takes the bet away from the total
    def lose_bet(self):
        self.total -= self.bet
        return self.total

# prints the information in the right format
    def __str__(self):
        return str(self.total)

# creates a deck and shuffles it
deck = Deck()
deck.shuffle()

# creates player and dealer hands
player_hand = Hand()
dealer_hand = Hand()

# creates player chips
player_chips = Chips()

# asks the player how many chips they want to bet
# if the bet is greater than the total, an error message is printed

def take_bet():
    global chips_bet_prompt, chips_bet, bet_button, player_chips, hit_button, game_status

    # if the player chips is a number string, converts it to an integer
    if chips_bet.get().isdigit():
        player_chips.bet = int(chips_bet.get())

    # error messages relating to wrong inputs
    if chips_bet.get() == "":
        chips_bet_prompt.config(text="Enter a value!")

    elif chips_bet.get().isalpha():
        chips_bet_prompt.config(text="Enter a number!")

    # error messages for impossible values
    if player_chips.bet <= 0:
        chips_bet_prompt.config(text=f"Chips must be greater than 0!")

    elif player_chips.bet > player_chips.total:
        chips_bet_prompt.config(text=f"Chips cannot exceed {player_chips.total}!")

    # if all other criteria are met, chips bet can no longer be entered. Lets the hit button start working
    elif player_chips.bet > 0:
        chips_bet_prompt.config(text=f"{player_chips.bet} chips bet!")
        bet_button.config(command=none, text="Entered!")
        hit_button.config(command=player_hit)
        game_status.config(text="You've bet chips. You can now start playing.")


# label for viewing total chips
# entry box for betting chips
chips_frame = tk.Frame(bg="white")
chips_bet_prompt = tk.Label(bg="white", text="How many chips would you like to bet?", master=chips_frame, width=34, relief="raised")
chips_bet = tk.Entry(master=chips_frame, width=27)
bet_button = tk.Button(command= take_bet,master= chips_frame, bg="white", relief="raised", text="Enter!", width= 10)

chips_frame.grid(row=3, column=1, sticky="n", padx=2, pady=2)

chips_bet_prompt.pack()
chips_bet.pack(side=tk.LEFT)
bet_button.pack(side=tk.RIGHT)

total_chips_lbl = tk.Label()

# the dealer already playing starts as false
dealer_played = False

# defines 'hit'. this adds 1 card to the hand
def player_hit(deck_cards=deck, hand=player_hand):
    global player_cards_lbl, player_total_lbl
    stand_button.config(command=stand)
    current_hand = hand.cards

    hand_value = hand.value

    new_card = deck_cards.deal()
    new_card_value = 0

    hand.add_cards(new_card)

    new_hand = ""

    if hand_value > 21:
        game_status.config(text="You've busted! You cant hit anymore.")
    else:
        game_status.config(text="You are playing.")
        for card in current_hand:
            new_hand += str(card)
            new_hand += "\n"

            hand_value += new_card_value

        player_cards_lbl.config(text=new_hand)
        player_total_lbl.config(text=f"Player Total: {hand.value}")

def stand():
    global game_status, hit_button, player_total_lbl, player_hand, dealer_played
    game_status.config(text="Player stands, the dealer will now play.")
    hit_button.config(command=none)
    hand_value = player_hand.value
    # if the player busts, they lose chips and the dealer doesn't play.
    if hand_value > 21:
        player_chips.lose_bet()
        game_status.config(text=f"Player busts! The dealer wins.\nChips total: {player_chips.total}\nContinue playing?")
        dealer_cards_lbl.config(text="The dealer did not play.")
        button_config()
    else:
        dealer_hit()

def dealer_hit(deck_cards=deck, hand=dealer_hand):
    global dealer_total_lbl, dealer_cards_lbl, game_status, dealer_played, player_chips
    hand_value = hand.value

    new_hand = ""
    if dealer_played:
        pass
    else:
        while hand_value < 17:

            new_card = deck_cards.deal()
            hand.add_cards(new_card)
            new_card_value = new_card.value

            hand_value += new_card_value

            new_hand += str(new_card)
            new_hand += "\n"

            dealer_cards_lbl.config(text=new_hand)
            dealer_total_lbl.config(text=f"Dealer Total: {hand.value}")

        if dealer_hand.value > 21:
            player_chips.win_bet()
            game_status.config(
                text=f"Dealer busts! The player wins.\nChips total: {player_chips.total}\nContinue playing?")

        elif dealer_hand.value == player_hand.value:
            game_status.config(text=f"It's a draw!!\nChips total: {player_chips.total}\nContinue playing?")

        elif player_hand.value < dealer_hand.value:
            player_chips.lose_bet()
            game_status.config(text=f"Dealer wins!\nChips total: {player_chips.total}\nContinue playing?")

        elif dealer_hand.value < player_hand.value:
            player_chips.win_bet()
            game_status.config(text=f"Player wins!\nChips total: {player_chips.total}\nContinue playing?")

        button_config()

# buttons to hit and stand
hit_stand_frame = tk.Frame(width=34, height=2)
hit_button = tk.Button(command = none, master=hit_stand_frame, text="Hit!", width=16, height=2, padx=1, bg="white")
stand_button  = tk.Button(command=none, master=hit_stand_frame, text="Stand!", width=16, height=2, padx=1, bg="white")

hit_stand_frame.grid(row=3, column=0, sticky="w", padx=2, pady=2)
hit_button.pack(side=tk.LEFT, padx=2, pady=2)
stand_button.pack(side=tk.RIGHT)

# different outcomes and a function to check the outcome

def button_config():
    yes_button.config(text="Yes", command=reset)
    no_button.config(text="No", command=confirm_exit)

# function to reset
# clears all the hands and labels and restarts
# if the player has no chips, the function ends
def reset():
    global deck, player_hand, player_chips, dealer_hand, chips_ran_out, chips_bet_prompt
    if player_chips.total <= 0:
        game_status.config(text="You have no chips left to bet.")
        chips_ran_out = True
        confirm_exit()
    else:
        chips_bet_prompt.config(text="How many chips would you like to bet?")
        game_status.config(text="You're currently betting chips. Finish doing so before playing.")
        yes_button.config(text="")
        no_button.config(text="")
        bet_button.config(command=take_bet,text="Enter!", )

        deck = Deck()
        deck.shuffle()
        player_hand.clear()
        dealer_hand.clear()
        player_chips.bet = 0

        player_cards_lbl.config(text="player cards will appear here.")
        player_total_lbl.config(text="Player Total: 0")
        dealer_cards_lbl.config(text="dealer cards will appear here.")
        dealer_total_lbl.config(text="Dealer Total: 0")

def leave():
    window.destroy()

confirm_button = tk.Button(command= leave,master=button_frame ,height = 5, width=12, bg="white", text="Okay!")

def confirm_exit():
    global chips_ran_out
    no_button.destroy()
    yes_button.destroy()
    confirm_button.pack(side=tk.RIGHT)
    if chips_ran_out:
        game_status.config(text="You ran out of chips.\nThanks for playing! Press the button to exit.")
    else:
        game_status.config(text="Thanks for playing! Press the button to exit.")

window.mainloop()