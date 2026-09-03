"""
GenericDice.py

Purpose:
Generate a generic dice rolling game that allows the user to roll
dice with 4, 6, 8, 10, 12, or 20 sides.

Author:
Troy Kobryn

Course:
CSC6301

Date:
September 3, 2026
"""

import random


def RollDice(desiredNumberOfSides: int) -> int:
    """
    Simulates rolling a die with the requested number of sides.

    Arguments:
        desiredNumberOfSides (int): The number of sides on the die.
            Valid values are 4, 6, 8, 10, 12, or 20.

    Returns:
        int: A random number between 1 and the requested number of sides.
    """
    return random.randint(1, desiredNumberOfSides)


def main():
    """
    Runs the Generic Dice Roller Game.

    The user selects a valid die size, rolls the die, and chooses
    whether to roll again.

    Returns:
        None
    """
    valid_sides = [4, 6, 8, 10, 12, 20]

    print("Generic Dice Roller Game")

    while True:
        try:
            desired_sides = int(input(
                "\nWhat size dice would you like to roll? "
                "(4, 6, 8, 10, 12, or 20): "
            ))

            if desired_sides not in valid_sides:
                print("Error: That is not a valid dice size")
                continue

            result = RollDice(desired_sides)
            print(f"You rolled a d{desired_sides} and got: {result}")

            again = input(
                "Would you like to roll again? (y/n): "
            ).lower()

            if again == "y":
                continue
            elif again == "n":
                print("Game over")
                break
            else:
                print("Error: Please enter only 'y' or 'n'.")

        except ValueError:
            print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()
