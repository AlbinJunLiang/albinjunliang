
# Guess a word
# take away an opportunity through failure
# set the matched words
# check  if the word has been guessed
# check if the player still has opportunities



def replace_words (word_to_guess = 'BANANA', current_guess = '_____', character = ''):

    current_guess = list(current_guess)
    if character.upper() not in word_to_guess:
        return
    
    for i in range(len(word_to_guess)):
        if word_to_guess[i].upper() == character.upper():
            current_guess[i] = word_to_guess[i].capitalize()

    return "".join(current_guess)



guessed_word = replace_words('BANANA', '______','A')
print(guessed_word)

guessed_word = replace_words('BANANA',guessed_word,'b')

print(guessed_word)

guessed_word = replace_words('BANANA',guessed_word,'f')



print(guessed_word)
    




""""
// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler
using System;

public class HelloWorld
{

    static string guess (string a, string b , string c){

    var ouput = b.ToCharArray();
    for(int i = 0; i < a.Length; i++)
    {
        if(a[i].ToString() == c)
        {
               ouput[i] = a[i];
        }
        
    }
return string.Join("", ouput); ;
    }
    public static void Main(string[] args)
    {

        string texto = "CACA";
       texto = guess(texto,"____", "C");
        Console.WriteLine (texto);


       texto = guess("CACA", texto, "A");
        Console.WriteLine (texto);
  

    }
}
"""