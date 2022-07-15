#!/usr/bin/python3
# -----------------------------------------------------------------
# simple GUI text Editor.
#
#
#
# Author:N84.
#
# Create Date:Fri Jul 15 12:15:45 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------

from os import system
from os import name as OS_NAME
import tkinter
from tkinter.constants import END

# TO-DO:
# [1]- make sure to add line number, mean that user can they,
# know the line number.
# [2]- save or not save indicator, like the one in arduino IDE.
# [3]- make sure to add some useful info in the bottom label, like the,
# vscode show us the cursor position and the interpreter and etc...
# [4]- add settings page to control of the font size and the last open,
# files, and font color....etc.

# Setup the Defaults.
WIN_TITLE = "Text Editor"
WIN_HEIGHT = 600
WIN_WIDTH = 500
WIN_BG = "#2C3E50"
WIN_FG = "white"
WIN_FONT_FAMILY = "Ubuntu"

BTN_PROPERTIES = {
    "font": (WIN_FONT_FAMILY, 10, "bold"),
    "border": 0,
    "borderwidth": 0,
    "highlightbackground": "Black",
    "highlightthickness": 0,
    "bg": "#8E44AD",
    "activebackground": "#9E54BD",
    "fg": WIN_FG,
    "activeforeground": "white",
    "height": 1

}


def clear():
    """wipe terminal screen."""
    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for any os in the world.
        # system("your-command")
        pass


clear()


def main():
    pass


if __name__ == "__main__":
    main()
