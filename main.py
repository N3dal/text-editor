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
import tkinter.filedialog as file_dialog

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

TEXT_EDIT_PROPERTIES = {
    "font": (WIN_FONT_FAMILY, 10),
    "border": 0,
    "bd": 0,
    "borderwidth": 0,
    "highlightbackground": "Black",
    "highlightthickness": 0,
    "highlightcolor": "black",
    "bg": "#34495E",
    "fg": WIN_FG,
    "height": 32

}

TAB_PROPERTIES = {
    "font": (WIN_FONT_FAMILY, 8),
    "border": 0,
    "bd": 0,
    "borderwidth": 0,
    "highlightbackground": "Black",
    "highlightthickness": 0,
    "highlightcolor": "black",
    "bg": "#34495E",
    "fg": WIN_FG,
    "padx": 10,
    "anchor": "center",
    "width": 40,
    "height": 3

}

BOTTOM_FRAME_PROPERTIES = {
    "bg": "#9E54BD",
    "width": 500,
    "height": 35
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


def start_app(root: tkinter.Tk, **app_start_options):
    """start the main loop for the program.
    program start-up so put any thing here,
    if you want it to start with program start-up."""

    if "tab_file_name" in app_start_options:
        # create the default name for the files.
        kwargs["tab_file_name"].set("Untitled")

    root.mainloop()


def main_window():
    """the main window for the Text Editor."""

    root = tkinter.Tk()

    root.title(WIN_TITLE)

    # setup the size and the position.
    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

    # make the window un-resizable.
    root.resizable(False, False)

    # change the background color.
    root.configure(bg=WIN_BG)

    # create The main Text widget for edit and save our text.
    text_edit = tkinter.Text(root, **TEXT_EDIT_PROPERTIES)
    text_edit.place(x=0, y=48)

    # create the main buttons.
    save_btn = tkinter.Button(
        root, text="Save", command=None, **BTN_PROPERTIES)
    save_btn.place(x=3, y=12)

    save_as_btn = tkinter.Button(
        root, text="Save As", command=None, **BTN_PROPERTIES)
    save_as_btn.place(x=58, y=12)

    open_btn = tkinter.Button(
        root, text="Open", command=None, **BTN_PROPERTIES)
    open_btn.place(x=132, y=12)

    # create our special variable, that we will use it,
    # for storing the tab file name.
    file_name = tkinter.StringVar()

    # create Tab label to show the file name.
    tab = tkinter.Label(root, textvariable=file_name, **TAB_PROPERTIES)
    tab.place(x=228, y=7)

    # create bottom frame.
    bottom_frame = tkinter.Frame(root, **BOTTOM_FRAME_PROPERTIES)
    bottom_frame.place(x=0, y=565)

    start_app(root, tab_file_name=file_name)


def main():
    """"""
    main_window()


if __name__ == "__main__":
    main()
