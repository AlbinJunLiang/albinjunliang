from abc import ABC, abstractmethod

# using strategy pattern design

class ReverseStrategy (ABC):
    @abstractmethod
    def reverse_string (self, word):
        pass

class ReverseStringSlicing (ReverseStrategy):
    def reverse_string (self, word):
        return word[::-1]

class ReverseTraditional ():
    def reverse_string (self, word):
        ouput = ""
        for i in range(len(word)):
            ouput += word[(len(word)-1)-i]
        return ouput 

class ReverseNative ():
    def reverse_string (self, word):
        characters =  reversed(list(word))
        return "".join(characters)


class Reverse:
    def __init__(self, strategy: ReverseStrategy):
        # El contexto recibe la estrategia inicial
        self.__strategy = strategy

    def change(self, new_strategy: ReverseStrategy):
        # Permite cambiar de estrategia en tiempo de ejecución
        self.__strategy = new_strategy

    def do(self, word):
        # Delega la tarea a la estrategia actual
        return self.__strategy.reverse_string(word)


print(ReverseStringSlicing().reverse_string("reconocer"))

print(ReverseTraditional().reverse_string("RECONOCED"))


print(ReverseNative().reverse_string("RECONOCED"))


test = Reverse(ReverseStringSlicing())
print(test.do("55552"))  # Salida: Pagando $150 con Tarjeta de Crédito.