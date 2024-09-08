import random
from hangman_words import word_list
from hangman_art import stages

lives = len(stages) - 1  # Maximum lives based on stages

# Choose a random word from the word list

chosen_word = random.choice(word_list)  # Randomly picks a word like "horse"

game_over = False
# Initialize guessed letters and display placeholder
guessed_letters = []                    # Stores correct guesses
placeholder = ["_"] * len(chosen_word)   # Starts with a list of underscores, one for each letter in the word

# Main loop for guessing letters
while not game_over:  # Continue while the game is not over
    print(f" {lives} Lives Left")
    guess = input("Guess a letter: ").lower()  # User inputs a letter, converted to lowercase

    if guess in guessed_letters:
        print(f"You already guessed {guess}. Try again!")
        continue
    
    guessed_letters.append(guess)

    if guess in chosen_word:             # Check if the guessed letter is in the word
        print("Right!")
        # Update the placeholder with the correct guessed letter
        for index, letter in enumerate(chosen_word):  # Loop through the word to find where the guessed letter appears
            if letter == guess:
                placeholder[index] = letter           # Replace the underscore with the guessed letter in the correct position
    else:
        print("Wrong!")
        lives -= 1
        print(stages[lives])  # Show the corresponding hangman stage

    # Check if the player won or lost
    if "_" not in placeholder:  # All letters guessed correctly
        game_over = True
        print(f"You win! The word was: {chosen_word}")
    
    if lives == 0:  # No more lives left
        game_over = True
        print(f"You lost! The word was: {chosen_word}")
    
    # Display the current state of the word (letters guessed correctly and underscores) 
    print(" ".join(placeholder))  