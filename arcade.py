import sys
from rps import rps
from guess_number import guess_number


def arcade(name):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\nWelcome back to arcade menu, {name}!")

        playerchoice = input(
            '\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press "x" to exit the Arcade\n\n'
        )

        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter a valid choice (1, 2 or x)")
            return arcade(name)

        welcome_back = True

        if playerchoice == "1":
            play_rps = rps(name)
            play_rps()
        elif playerchoice == "2":
            play_guess_number = guess_number(name)
            play_guess_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")


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

    print(f"{args.name}, welcome to the Arcade!")
    arcade(args.name)