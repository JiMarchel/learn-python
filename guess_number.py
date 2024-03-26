import random
import sys


def guess_number(name="Player"):
    games_counts = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal games_counts
        computer_thinks = random.randint(1, 3)

        player_choices = input(
            f"\n{name}, I'm thinking of a number between 1 and 3.Guess what it is!\n"
        )

        if player_choices not in ["1", "2", "3"]:
            print("\nYou must enter 1, 2 or 3.\n")
            return play_guess_number()

        if int(player_choices) == computer_thinks:
            print(f"You guessed right! The number was {computer_thinks}.\n")
            player_wins += 1
        else:
            print(f"Sorry {name}, the number was {computer_thinks}.\n")

        games_counts += 1
        print(f"Game count : {games_counts}\n")
        print(f"{name}'s wins : {player_wins}\n")
        print(f"Your winning percentage : {player_wins/games_counts*100:.2f}%\n")

        print(f"Play again, {name}?\n")

        while True:
            play_again = input("Y for Yes or Q to Quit\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return

    return play_guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personalized game experienced."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    play = guess_number(args.name)
    play()
