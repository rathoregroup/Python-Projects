import random
from words import words
import string

def get_valid_word(words):
    word =  random.choice(words)
    
    while " " in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #getting user input
    lives = 6
    while len(word_letter) > 0 and lives > 0:
        # letters used

        print("You have", lives, "lives left and you have used these letter: ", " ".join(used_letters))
        
        word_list = [letter if letter in used_letters else "-" for letter in word]
        
        print("Current word: ", " ".join(word_list))
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives-1

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid Character. Please try again.")

    if lives==0:
        print("You died, sorry. The word was", word)
    else:
        print("You have guessed the", word, "correctly")

hangman()



    