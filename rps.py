import enum
import sys
import random


def rps(name="Player"):
    game_counts = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(enum.Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input(f"\n{name}, enter... \n1 for rock, \n2 for paper and, \n3 for scissors: \n")

        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, you must enter 1, 2 or 3")
            return play_rps()

        computer_choice = random.choice("123")

        player = int(player_choice)
        computer = int(computer_choice)

        print(f"\n{name} chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"\nPython chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if (
                (player == 1 and computer == 3)
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)
            ):
                player_wins += 1
                return f"🎉{name}  win!"
            elif player == computer:
                return "😲 It's a tie!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_counts
        game_counts += 1

        print(f"\nGame counts :{game_counts}.")
        print(f"\n{name}'s wins :{player_wins}.")
        print(f"\nPython wins :{python_wins}.")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or Q to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")

    return play_rps


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
    
    play = rps(args.name)
    play()
