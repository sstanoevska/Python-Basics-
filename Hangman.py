import random
from hangman_words import word_list
from hangman_art import logo,stages
#from hangman_art import stages

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(logo)
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"You have {lives} left! Be careful!")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            print(f"Correct! The letter {guess} is in the word!")
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word! You lose a life :(")
        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"You lose! The word was {chosen_word}. Better luck next time!")

    if "_" not in display:
        game_over = True
        print("Congratulations! You win!")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])
