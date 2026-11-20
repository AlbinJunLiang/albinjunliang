class Hangman:

    def __init__(self, hidden_word, word_to_guess, opportunities):
        self.__hidden_word = hidden_word if hidden_word else self.__generate_hidden_word(word_to_guess)
        self.__word_to_guess = word_to_guess
        self.__opportunities = opportunities

    def __generate_hidden_word(self, word):
        return "_" * len(word)


    def containCharacter (self, character):
        return character.upper() in self.__word_to_guess.upper()

    def replace_words(self, character=''):
            # Si la letra no está en la palabra
   
            if not self.containCharacter(character):
                self.opportunities -= 1  # Corregido: restamos 1 correctamente
                return False  # Indicamos que falló
                        
            # Si la letra SÍ está, convertimos a lista para poder modificarla
            hidden_list = list(self.__hidden_word)

            for i in range(len(self.__word_to_guess)):
                if self.__word_to_guess[i].upper() == character.upper():
                    hidden_list[i] = self.__word_to_guess[i]

            # Volvemos a unir la lista en el string privado
            self.__hidden_word = "".join(hidden_list)
            return True  # Indicamos que acertó

        
    def is_guessed (self):
        return self.__word_to_guess == self.__hidden_word


    @property
    def opportunities(self):
        return self.__opportunities

    @opportunities.setter
    def opportunities(self, new_opportunities):
        if new_opportunities < 0 :
            print("Error: yo can not set negative opportunities.")
        elif self.opportunities > 0:
            self.__opportunities = new_opportunities


    @property
    def word_to_guess (self):
        return self.__word_to_guess

    @word_to_guess.setter
    def word_to_guess(self, new_word_to_guess):
        self.__word_to_guess = new_word_to_guess
        self.__hidden_word = self.__generate_hidden_word(new_word_to_guess)

    @property
    def hidden_word (self):
        return self.__hidden_word

    @hidden_word.setter
    def hidden_word(self, new_hidden_word):
        self.__hidden_word = new_hidden_word

    def __str__(self):
            return f"Palabra oculta: {self.__hidden_word} | Vidas restantes: {self.__opportunities}"



