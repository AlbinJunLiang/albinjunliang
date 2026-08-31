from hangmanRandom import HangmanRandom

game = HangmanRandom(None, 2, ["FRUITS", "JAMAICA", "HELLO", "SAND"])


print(game)

while not game.is_guessed() and game.opportunities > 0:
    print(f"Currrently the hidden word is: {game.hidden_word}")
    character = input("Please enter a character:")

    ok = game.replace_words(character)
    if not ok:
        print(f"Invalid character, opportunities available: {game.opportunities}")  

if game.is_guessed():
    print("Word has been guessed: "+game.hidden_word)
else:
    print("Try it again :)")
