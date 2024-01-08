import random

def play_game(limit):
    # Generate a random number within the range
    secret_number = random.randint(1, limit)
    print(f"Guess the number between 1 and {limit}.")

    while True:
        # Get the user's guess
        guess = int(input("Enter your guess: "))

        # Compare the guess to the secret number
        if guess > secret_number:
            print("Your guess is too high. Try again.")
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Congratulations! You guessed the number.")
            break

def main():
    while True:
        # Prompt the user for a limit
        limit = int(input("Enter the upper limit for the guessing game: "))

        # Play the game
        play_game(limit)

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    main()

