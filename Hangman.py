import random
from colorama import init

def main():
    # Initialize colorama for colored output
    init()

    # Welcome message
    welcome = [
        '\033[1;37mWelcome to \033[1;4m\033[1;31mHangman\033[0m\033[1;37m! You must try to guess the given word',
        'letter by letter before you run out of your ten attempts.',
        'A correct guess does not use up your attempts. \033[1;33m\033[1mGood luck!\033[0m'
    ]

    for line in welcome:
        print(line)

    # Hangman stages (ASCII art)
    hangman_stages = [
        """
         ------
         |    |
              |
              |
              |
              |
        --------""",
        """
         ------
         |    |
         O    |
              |
              |
              |
        --------""",
        """
         ------
         |    |
         O    |
         |    |
              |
              |
        --------""",
        """
         ------
         |    |
         O    |
        /|    |
              |
              |
        --------""",
        """
         ------
         |    |
         O    |
        /|\\   |
              |
              |
        --------""",
        """
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
        --------""",
        """
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
        --------"""
    ]

    # Setting up the play_again loop
    play_again = True

    while play_again:
        # Set up the game loop
        words = ["hangman", "random", "intern", "codealpha", "clothing",
                 "computer", "python", "program", "glasses", "programming",
                 "science", "internship", "friends", "coding", "biology",
                 "algebra", "university", "science", "guesses", "attempts"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None  # Will hold the player's guess
        guessed_letters = []  # A list of letters guessed so far
        word_guessed = ["-" for _ in chosen_word]  # Create an unguessed, blank version of the word
        attempts = 6  # Number of incorrect guesses allowed

        while attempts > 0 and "-" in word_guessed:
            print(hangman_stages[6 - attempts])  # Display hangman stage based on remaining attempts
            print(f"\033[1;31m\nAttempts Remaining: {attempts}")
            print("\033[1;34mWord: " + "".join(word_guessed))

            try:
                player_guess = str(input("\033[1;37m\nType in a letter: ")).lower()
            except Exception as e:
                print("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess.isalpha():  # Check if input is a letter
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1:  # Check if input is only one letter
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters:  # Check if letter hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    continue

            guessed_letters.append(player_guess)

            if player_guess in chosen_word:
                for index, letter in enumerate(chosen_word):
                    if player_guess == letter:
                        word_guessed[index] = player_guess  # Replace blanks with correct guesses
            else:
                attempts -= 1

        if "-" not in word_guessed:  # No blanks remaining
            print("\n\033[1;4m\033[1;32mCongratulations\033[0m\033[1;37m! You guessed the word: {}".format(chosen_word))
        else:  # Loop must have ended because attempts reached 0
            print(hangman_stages[-1])  # Display final hangman stage (fully built)
            print("\n\033[1;4m\033[1;31mYou lose\033[0m\033[1;37m! The word was: {}".format(chosen_word))

        print("\nWould you like to play again?")
        response = input("> ").lower()
        if response not in ("yes", "y", "yeah", "yep", "1", "ok"):
            play_again = False

if __name__ == "__main__":
    main()