"""
- class description-
The class Deck of cards represents a list that each cell is an object of Card.
There are 4 suits to the cards, and each suit has 13 cards.-->total of 52 cards.
A deck of cards is a list of 52 Cards. --> This is the feature(constructor) of the class
"""
import random
from game_cards.Card_class import Card

"""
--init--
we will have 2 loops: The external loop runs on the suit of the card:
Diamond,spade,heart,club
The internal loop runs on the value of the card:1-13 
"""


class DeckOfCards:

    def __init__(self):
        self.deck = []  # creating an empty list
        for i in range(1, 5):  # Building the deck
            for x in range(1, 14):
                new_card = Card(x, i)
                self.deck.append(new_card)

    def cards_shuffle(self):  # This method reorganize the Deck randomly
        if len(self.deck) == 0:  # Checks if the list of the cards is not empty
            raise ValueError("The List Deck of Cards is empty")

        random.shuffle(self.deck)

    def deal_one(self):  # This method pulls of a random card from the deck
        if len(self.deck) == 0:  # Checks if the list of the cards is not empty
            raise ValueError("The List Deck of Cards is empty")

        if type(random.choice(self.deck)) != Card:  # Checks if the type of the cell in the deck is Card
            raise TypeError("The type of the cell is not Card")

        return self.deck.pop(self.deck.index(random.choice(self.deck)))

    def __repr__(self):  # This method prints the deck
        return f"List of Cards : {self.deck}"



