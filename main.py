
import random
# from replit import clear
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO-2: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # clear()

    if guess in display:
        print(f"{guess} is already guessed !")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        # TODO-3: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was : {chosen_word}")


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])