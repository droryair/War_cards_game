"""
הגדירו מחלקה בשם
Cards
המייצגת קלף במשחק קלפים.
לקלף יש מאפיינים:
ערך- value
וסמל - suit
הסמל קובע את סוג הקלף.
הערך 1-13, כאשר המספרים מייצגים:
1-  Ace
11- Jack
12- Queen
13- King

הקלף בעל הערך הגבוה ביותר הוא Ace.

"""


class Card:
    def __init__(self, value, suit):
        # checking for valid value and suit (range and type).
        if value < 1 or value > 13:
            raise ValueError(f"Card's value is out of range. Valid range: 1-13. value given: {value}")
        elif type(value) != int:
            raise TypeError(f"Card's value is out of type 'int'.The type received:{type(value)}")
        if suit < 1 or suit > 4:
            raise ValueError(f"Card's suit is out of range. Valid range: 1-4. value given: {suit}")
        elif type(suit) != int:
            raise TypeError(f"Card's suit is out of type 'int'.The type received:{type(suit)}")

        # initializing value and suit.
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value}:{self.suit}"

    def __repr__(self):
        return f"{self.value}:{self.suit}"

    # compares between two cards, and returns boolean value.
    # also raising exceptions when 'other' is not of type 'Card' .
    def __gt__(self, other):
        """
        :param other: another instance of class 'Card'.
        :return: boolean value for whether the first card (self) is greater than the second (other)
        """
        # checking the type of 'other'.
        if type(other) != Card:
            raise TypeError("Got an object not from 'Card' type.")

        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            # taking care of possible incident: two identical cards.
            elif self.suit == other.suit:
                raise ValueError("Got two identical cards. How can it be??")
        return False


