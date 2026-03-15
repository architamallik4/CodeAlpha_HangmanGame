import random

WORDS = ["apple", "grape", "house", "tiger", "plant"]
MAX_WRONG_GUESSES = 6


def choose_word():
    return random.choice(WORDS)


def get_word_progress(secret_word, guessed_letters):
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    return " ".join(letters)


def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


def play_hangman():
    secret_word = choose_word()
    guessed_letters = []
    attempts_left = MAX_WRONG_GUESSES

    print("Welcome to Hangman!")

    while attempts_left > 0:
        print(f"Word: {get_word_progress(secret_word, guessed_letters)}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {' '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            if is_word_guessed(secret_word, guessed_letters):
                print(f"Word: {get_word_progress(secret_word, guessed_letters)}")
                print(f"You won! The word was: {secret_word}")
                return
        else:
            attempts_left -= 1

    print(f"You lost! The word was: {secret_word}")


play_hangman()
