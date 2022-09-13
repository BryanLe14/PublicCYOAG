"""
Allows various globals to be imported and used.

Great for dev purposes, horrible for actual applications.
"""
import os

width = os.get_terminal_size()[0]
height = os.get_terminal_size()[1]

width2 = width / 2
height2 = height / 2

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
