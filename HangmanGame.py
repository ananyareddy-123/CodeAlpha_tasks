import random

# List of 5 predefined words
words = ["python", "github", "coding", "computer", "program"]

# Choose a random word
word = random.choice(words)

# Store letters the player has guessed
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

# Create the hidden word
display_word = ["_"] * len(word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while incorrect_guesses > 0 and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses left:", incorrect_guesses)

    guess = input("Guess a letter: ").lower()

    # Check that the input is one letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Good guess!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong guess!")
        incorrect_guesses -= 1

# Game result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over!")
    print("The word was:", word)
