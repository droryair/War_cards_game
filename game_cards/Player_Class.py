"""
מחלקה Player- שחקן
מאפייני המחלקה:
player_name,
player_deck
player_cards_amount
מספר הקלפים ייקבע בעת התחלת משחק חדש, ויהיה 26 כברירת מחדל.
ניתן יהיה להגדיר שמספר הקלפים יהיה שונה בהתאם למה שייקבע בתחילת המשחק.
בכל מקרה, מספר הקלפים לשחקן לא יכול להיות כבוה מ- 26 ולא נמוך מ- 10.

מתודות המחלקה:
__init__
תקבל את שם השחקן ואת מספר הקלפים שיש לחלק לשחקן
(ברירת מחדל- 26. אם התקבל מספר גבוה מ- 26 או נמוך מ- 10, המספר יהיה 26.)
המתודה תאתחל את חבילת הקלפים של השחקן כרשימה ריקה.

set_hand
מקבלת חבילת קלפים של המשחק (מסוג DeckOfCards)
ומחלקת מתוכה קלפים אקראיים עבור השחקן, עפ"י מספר הקלפים שאמור השחקן לקבל.
יש להשתמש במתודה deal_one ששולפת קלף מהחבילה של המשחק. המתודה לא מחזירה כלום.

get_card
שולפת קלף אקראי מהחבילה של השחקן. המתודה תחזיר את הקלף ששלפה.

add_card
מתודה שמקבלת קלף ומוסיפה אותו לחבילת הקלפים של השחקן. לא מחזירה כלום.

הערות המפתחת:
שם שחקן- עניין בעייתי כי יכולים להיות שני שחקנים עם אותו השם. להוסיף מספר ששחקן (id)?
 V  לקרוא על random.choice
"""
import random
from game_cards.DeckOfCards_Class import DeckOfCards
from game_cards.Cards_class import Card


class Player:
    # initiates the player's name, his deck (empty list) and the amount of cards he starts the game with (between 10 and 26).
    # !!!שם שחקן- עניין בעייתי כי יכולים להיות שני שחקנים עם אותו השם. להוסיף מספר ששחקן (id)? !!!
    def __init__(self, player_name='Player', player_cards_amount=26):
        """
        :param player_name: the player's name (default: 'Player')
        :param player_cards_amount: amount of cards to start the game (between 10 and 26, default: 26).
        """
        # checking for valid numbers of cards for the player (valid amount: 10 < amount < 26)
        if player_cards_amount > 26 or player_cards_amount < 10:
            self.cards_amount = 26
        else:
            self.cards_amount = player_cards_amount

        self.name = player_name
        self.deck = []  # player's deck will include instances of the 'Card' class.

    def __str__(self):
        return f"player: {self.name}, deck(max:{self.cards_amount}): {self.deck}"

    def __repr__(self):
        return f"|player: {self.name}, deck(max:{self.cards_amount}): {self.deck}| \n"

    # fills the player's deck ('self.deck') with random cards, according to the specified amount ('self.cards_amount')
    def set_hand(self, deck_of_cards: DeckOfCards):
        """
        :param deck_of_cards: a variable of type 'DeckOfCards' class.
        :functionality: fills the player's deck ('self.deck') with random cards, according to the specified amount ('self.cards_amount')
        :return: None
        """
        # checking the type of the variable deck_of_cards
        if type(deck_of_cards) != DeckOfCards:
            raise TypeError(f"deck_of_cards is not of type DeckOfCards!")

        for i in range(self.cards_amount):
            # adding to 'self.deck' a random card from 'deck_of_cards', using the method 'deal_one' from the 'Card' class.
            self.deck.append(deck_of_cards.deal_one())

    # deletes one random card from the player's deck (self.deck) and returns it.
    def get_card(self):
        """
        :functionality: deletes a random card from the player's deck ('self.deck'').
        :return: the deleted card.
        """
        return self.deck.pop(self.deck.index(random.choice(self.deck)))

    # receives a variable of type 'Card' class, and adds it to the player's deck ('self.deck')
    def add_card(self, card: Card):
        """
        :param card: a variable of type 'Card' class.
        :functionality: adds the card to the player's deck ('self.deck').
        :return: None
        """
        # checking the type of the variable card
        if type(card) != Card:
            raise TypeError(f"{card} is not of type Card!")

        self.deck.append(card)
