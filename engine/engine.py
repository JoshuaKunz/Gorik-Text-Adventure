from utilities.console import console
from character.save_load import load


def start_game(character):
    while True:
        pass


def intro():
    console.print_green("Welcome to The Adventures of Gorik!")
    console.print_yellow("===================================")
    input("Press Enter to continue")
    console.clear()
    console.print_green("In this text-adventure you will be")
    console.print_green("challenged with monsters, puzzles, and quests.")
    console.print_green("Along the way you will level up, gain money,")
    console.print_green("and experience the long lost land of Akheim.")
    input("Press Enter to continue")
    console.clear()
