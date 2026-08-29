
# Guess a word
# take away an opportunity through failure
# set the matched words
# check  if the word has been guessed
# check if the player still has opportunities



def replace_words (word_to_guess = 'BANANA', current_guess = '_____', character = ''):

    if not containCharacter(word_to_guess, character):
        return current_guess
    else:
        current_guess = list(current_guess)

    for i in range(len(word_to_guess)):
        if word_to_guess[i].upper() == character.upper():
            current_guess[i] = word_to_guess[i].capitalize()

    return "".join(current_guess)


def is_guessed (word_to_guess, current_guess):
    return word_to_guess == current_guess

def containCharacter (word_to_guess, character):
    return character.upper() in word_to_guess

    
guessed_word = "______"
word_to_guess = "BANANA"
opportunities = 2

while not is_guessed('BANANA', guessed_word) and opportunities > 0:
    print(f"Currrently the hidden word is: {guessed_word}")
    character = input("Please enter a character:")
    if not containCharacter(word_to_guess, character):
        opportunities -=1
        print(f"Invalid character, opportunity avaible: {opportunities}")
    else:
        guessed_word = replace_words(word_to_guess,guessed_word, character)


print("Word has been guessed: "+guessed_word)
