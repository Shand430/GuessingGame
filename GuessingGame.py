import random

def play_game(limit):
    secret_number = random.randint(1, limit)
    print(f"Guess the number between 1 and {limit}.")

    while True:
        guess = int(input("Enter your guess: "))

        if guess > secret_number:
            print("Your guess is too high. Try again.")
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Congratulations! You guessed the number.")
            break

def main():
    while True:
        limit = int(input("Enter the upper limit for the guessing game: "))

        play_game(limit)

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

