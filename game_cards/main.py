"""
- main -
התוכנית הראשית תקלוט שמות שחקנים ותתחיל משחק חדש עם 26 קלפים לכל שחקן.
בתחילת המשחק, התוכנית תדפיס עבוד על שחקן את שמו ואת הקלפים שקיבל.

המשך התוכנית הראשית- ביצוע משחק:
א) לאחר אתחול המשחק, התוכנית תשחק 10 סיבובים של משחק מלחמה.
ב) בכל סיבוב כל שחקן זורק קלף אקראי אחד מהחפיסה שלו.
ג) השחקן עם הקלף הגבוה זוכה, ואוסף אליו את שני הקלפים שנזרקו.
ד) הדפיסו את הקלפים שנזרקו בכל סיבוב, ואת הסוכה בסיבוב.

בתום המחשק, יודפסו פרטי השחקן שניצח במשחק. במקרה של תיקו- תודפס הודעה בהתאם.

"""

from game_cards.CardGame_Class import CardGame

# creating a dictionary to convert cards numbers to values names, for printing purposes.
val_dict = {
    13: 'King',
    12: 'Queen',
    11: 'Jack',
    1: 'Ace'
}

# creating a dictionary to convert numbers to suit names ,for printing purposes.
suit_dict = {
    1: 'Diamond',
    2: 'Spade',
    3: 'Heart',
    4: 'Club'
}





# gathering initial data (players' names, players' decks size)
amount_of_cards = 26
player_1_name = input("First player's name: ")
player_2_name = input("Second player's name: ")
new_game = CardGame(player_1_name, player_2_name, amount_of_cards)

# generating 10 rounds of the game
for i in range(10):
    # generating cards for both players
    p1_card = new_game.player1.get_card()
    p2_card = new_game.player2.get_card()

    # converting card numbers to names for printing purposes
    p1_card_name = ''
    if p1_card.value in val_dict:
        p1_card_name += val_dict[p1_card.value]
    else:
        p1_card_name += str(p1_card.value)
    p1_card_name += f" of {suit_dict[p1_card.suit]} "

    p2_card_name = ''
    if p2_card.value in val_dict:
        p2_card_name += val_dict[p2_card.value]
    else:
        p2_card_name += str(p2_card.value)
    p2_card_name += f" of {suit_dict[p2_card.suit]} "

    # printing the players' cards
    print(f"{new_game.player1.name}: {p1_card_name} ")
    print(f"{new_game.player2.name}: {p2_card_name} ")

    # comparing between the two cards, to determine who wins the round
    if p1_card > p2_card:
        new_game.player1.add_card(p1_card)
        new_game.player1.add_card(p2_card)
    else:
        new_game.player2.add_card(p1_card)
        new_game.player2.add_card(p2_card)

print(f"The winner is: {new_game.get_winner()}")
