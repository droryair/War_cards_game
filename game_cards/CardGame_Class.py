"""
Class CardGame - This is the class that manage the game between two players
Constructor init : gets the names of the players --> Two players in the game
                    and gets the number of the card for each player --> 10<= number of cards <=26

"""
# --------------------------
# importing all the classes
# --------------------------
import random
from game_cards.Card_class import Card
from game_cards.DeckOfCards_Class import DeckOfCards
from game_cards.Player_Class import Player

# initializing a counter for the amount of times the 'new_game' function is called.
counter_new_game = 0


class CardGame:

    def __init__(self, player_name1, player_name2, num_of_cards):
        self.player1 = Player(player_name1, num_of_cards)
        self.player2 = Player(player_name2, num_of_cards)
        self.new_game()

    # creating the game's deck, the players, and their deck
    def new_game(self):
        """
        "functionality: creating the game's deck, the players, and their deck.
        :return: None
        """
        # checking the functions' counter to make sure it's not being called in the middle of the game.
        global counter_new_game
        counter_new_game += 1
        if counter_new_game > 1:
            raise SystemError("The Function 'new_game' was called in the middle of a game!!")

        # initializing a deck of cards and shuffling it
        main_deck = DeckOfCards()
        main_deck.cards_shuffle()

        # now we randomize which player gets cards first
        if random.randint(1, 2) == 1:
            self.player1.set_hand(main_deck)
            self.player2.set_hand(main_deck)
        else:
            self.player2.set_hand(main_deck)
            self.player1.set_hand(main_deck)

    # returns the player with the longest deck, or none in case of a tie.
    def get_winner(self):
        """
        :functionality: comparing between the length of the players' decks.
        :return: The winning player, or None (in case of a tie).
        """
        global counter_new_game
        counter_new_game = 0
        if len(self.player1.deck) > len(self.player2.deck):
            return self.player1
        elif len(self.player2.deck) > len(self.player1.deck):
            return self.player2
        else:
            return None


