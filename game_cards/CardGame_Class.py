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
        # Checks the if the type of the names is string
        if type(player_name1) != str or type(player_name2) != str:
            raise TypeError("The names of the players should be string type!!!")

        # Checks if the type of the number of cards is integer
        if type(num_of_cards) != int:
            raise TypeError("The number of cards to each player should be int type!!!")

        # Checks if the number of cards is eligible
        if num_of_cards < 10 or num_of_cards > 26 or num_of_cards < 0:
            raise ValueError("The number of cards is illegal 10<=num of cards<=26")

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
        if len(self.player1.deck) > len(self.player2.deck):
            return self.player1
        elif len(self.player2.deck) > len(self.player1.deck):
            return self.player2
        else:
            return None


if __name__ == '__main__':
    new_cardgame = CardGame('a', 'b', 23)
    print(counter_new_game)
    new_cardgame.new_game()
    print(counter_new_game)
    new_cardgame.new_game()
    print(counter_new_game)
