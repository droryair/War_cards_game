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

שתי פונקציות שימושיות:
random.shuffle
random.choice
"""
from game_cards.Player_Class import Player

amount_of_cards = 26
player_1_name = input("First player's name: ")
player_2_name = input("Second player's name: ")
new_game = CardGame(player_1_name, player_2_name, amount_of_cards)

for i in range(10):
    p1_card = new_game.player1.get_card()
    print(f"{new_game.player1.name}'s' card: {p1_card}")
    p2_card = new_game.player2.get_card()
    print(f"{new_game.player2.name}'s' card: {p2_card}")
    if p1_card > p2_card:
        new_game.player1.add_card(p1_card)
        new_game.player1.add_card(p2_card)
    else:
        new_game.player2.add_card(p1_card)
        new_game.player2.add_card(p2_card)
print(new_game.get_winner())

