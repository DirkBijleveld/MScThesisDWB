import sys

from software.src.commands import COMMANDS_DICT, arguments_to_dict, register
from software.src.commands.defection import defection
from software.src.commands.intermediary import intermediary
from software.src.commands.clean import clean
from software.src.commands.prep import prep
from software.src.commands.regression import regression

# Register commands
register("intermediary", intermediary)
register("clean", clean)
register("defection", defection)
register("prep", prep)
register("regression", regression)


def main(args: list[str]) -> None:
    print("Initializing...")
    print("Dirk Bijleveld MSc Political Science Thesis Software, 2023.")
    print("Please see readme.txt for more information.")
    print("#" * 30, end="\n\n")

    if len(args) == 0:
        print("Please specify a command.")
        return

    command = args[0]
    if command not in COMMANDS_DICT.keys():
        print("Invalid command.")
        return

    kwarguments = arguments_to_dict(args[1:])

    print(f"Executing command {command} with arguments: {kwarguments}.")

    COMMANDS_DICT[command](**kwarguments)


if __name__ == "__main__":
    main(sys.argv[1:])
