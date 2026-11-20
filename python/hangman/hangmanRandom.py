from albin.python.hangman.hangmanPOO import Hangman
import random

class HangmanRandom (Hangman):

    def __init__ (self,  hidden_word, opportunities, hidden_words):
        self.__hidden_words = hidden_words
        super().__init__(hidden_word, self.__get_random_word(), opportunities)



    @property 
    def hidden_words(self):
        return self.__hidden_words
    
    @hidden_words.setter
    def hidden_words(self, new_hidden_words):
        self.__hidden_words = new_hidden_words

    def __get_random_word (self):
        if self.__hidden_words:
            length = len(self.hidden_words) - 1
            random_position = random.randint(1, length)
            return self.__hidden_words[random_position]
        else:
            return "TEST"
    


