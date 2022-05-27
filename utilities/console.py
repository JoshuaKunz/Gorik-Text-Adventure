import os
from .colors import bcolors as color

class console:
    def clear():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def print_red(text):
        print("{}{}{}".format(color.RED, text, color.ENDC))

    def print_blue(text):
        print("{}{}{}".format(color.BLUE, text, color.ENDC))

    def print_green(text):
        print("{}{}{}".format(color.GREEN, text, color.ENDC))
    
    def print_yellow(text):
        print("{}{}{}".format(color.YELLOW, text, color.ENDC))

    def underline(text):
        return "{}{}{}".format(color.UNDERLINE, text, color.ENDC)
    
    def bold(text):
        return "{}{}{}".format(color.BOLD, text, color.ENDC)