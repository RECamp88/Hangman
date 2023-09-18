import random
import hangman_art
import hangman_words

import os 
def clear():
    os.system('cls')

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6 
already_guessed = []

#Testing code
print(f'The chosen word is: {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    
    if guess in already_guessed:
        print(f"You have already guessed: {guess}")
    else: already_guessed.append(guess)
    
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.") 
            
    print(f"{' '.join(display)}")
   
    if "_" not in display:
        end_of_game = True
        print("You Win!")
       
    print(hangman_art.stages[lives])
