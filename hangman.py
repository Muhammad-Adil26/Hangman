import random
from words import words
import string

def get_valid_word(words): # gets a valid word without a space or a dash from the list of words
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper() # makes the word that is randomly picked uppercase
    word_letters = set(word) # list of all the letters in the word
    used_letters = set() # list of all the letters we have used
    lives = 9 # How many errors you are allowed

    while len(word_letters) > 0 and lives > 0:
        print('Lives left:', lives)
        print('Used letters:', ' '.join(used_letters)) # prints all the letters you have used
        word_list = [letter if letter in used_letters else '-' for letter in word] # every letter in the word is a dash until you guess correctly
        print('Current word:', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        
        if len(user_letter) != 1 or user_letter not in string.ascii_uppercase: # if the input isnt a letter or if its longer than 1 letter, it gives an error
            print("Invalid input. Please enter a single letter.")
            continue

        if user_letter in used_letters:
            print("You have already used that letter.")
        else:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("This letter is not in the word.")
                
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!')

if __name__ == "__main__":
    hangman()
