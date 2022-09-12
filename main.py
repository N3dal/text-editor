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
# [5]- separate the program into group of files (constants, tools, ..., etc)

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

# create save path so when we click on the save,
# button the program save the file directly.
# 'None' indicate that there's no file save path,
# so we will ask the user to select path and then save it,
# in this variable to use it again later.
file_save_path = None


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

    return None


clear()


def start_app(root: tkinter.Tk, **app_start_options):
    """start the main loop for the program.
    program start-up so put any thing here,
    if you want it to start with program start-up."""

    if "tab_file_name" in app_start_options:
        # create the default name for the file on the tab,
        # when the file is not saved, or when we create new file.
        app_start_options["tab_file_name"].set("Untitled")

    root.mainloop()


class App(tkinter.Tk):
    """the main window for the Text Editor."""

    def __init__(self):
        super().__init__()

        self.title(WIN_TITLE)

        # setup the size and the position.
        self.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

        # make the window un-resizable.
        self.resizable(False, False)

        # change the background color.
        self.configure(bg=WIN_BG)

        # create our special variable, that we will use it,
        # for storing the tab file name.
        file_name = tkinter.StringVar()

        # create The main Text widget for edit and save our text.
        text_edit = tkinter.Text(self, **TEXT_EDIT_PROPERTIES)
        text_edit.place(x=0, y=48)

        # create the main buttons.
        save_btn = tkinter.Button(
            self, text="Save", command=lambda: save_click(file_name, text_edit), **BTN_PROPERTIES)
        save_btn.place(x=3, y=12)

        save_as_btn = tkinter.Button(
            self, text="Save As", command=lambda: save_as_click(file_name, text_edit), **BTN_PROPERTIES)
        save_as_btn.place(x=58, y=12)

        open_btn = tkinter.Button(
            self, text="Open", command=lambda: open_click(file_name, text_edit), **BTN_PROPERTIES)
        open_btn.place(x=132, y=12)

        # create Tab label to show the file name.
        tab = tkinter.Label(self, textvariable=file_name, **TAB_PROPERTIES)
        tab.place(x=228, y=7)

        # create bottom frame.
        bottom_frame = tkinter.Frame(self, **BOTTOM_FRAME_PROPERTIES)
        bottom_frame.place(x=0, y=565)

    def start_app(self, **options):
        """
        start the main loop for the program.
        program start-up so put any thing here,
        if you want it to start with program start-up.
        """

        if "tab_file_name" in options:
            # create the default name for the file on the tab,
            # when the file is not saved, or when we create new file.
            options["tab_file_name"].set("Untitled")

        self.mainloop()


def open_click(file_name: tkinter.StringVar, text_edit: tkinter.Text):
    """btn event when we click on the open button."""

    global file_save_path

    open_path_from_dialog = file_dialog.askopenfilename(title="Open")
    print(open_path_from_dialog)

    # guard conditions.
    if type(open_path_from_dialog) != str:
        # that happen when the user click on the cancel,
        # button on the dialog.
        # in this case end everything.
        return None

    file_save_path = open_path_from_dialog

    # get the file name, and set also.
    file_name.set(file_save_path.split('/')[-1])

    with open(file_save_path, "r") as file:
        file_data = file.readlines()

    # concatenate all the string on the file_data list.
    text_data = "".join(file_data)

    # before we insert anything we must insure we,
    # clear the Text on the Widget before.
    text_edit.delete("1.0", END)

    # now we will insert the string in Text widget.
    text_edit.insert(END, text_data)


def save_as_click(file_name: tkinter.StringVar, text_edit: tkinter.Text):
    """btn event when we click on the save-as button.
    using this the user can select new save path,
    or change the file name and this also will update,
    the file-save path and also the file name on the tab."""

    global file_save_path

    save_as_path_from_dialog = file_dialog.asksaveasfilename(
        title="Save As", initialfile=file_name.get())

    # get the file name, and set also.
    file_name.set(file_save_path.split('/')[-1])

    with open(file_save_path, "w") as file:
        file.writelines(text_edit.get("1.0", END))


def save_click(file_name: tkinter.StringVar, text_edit: tkinter.Text):
    """btn event when we click on the save button.
    this will update the save path and update,
    the file name on the tab, and save our file."""

    global file_save_path

    # first checkout if we have save-path or not,
    # if we have save the file directly , if not,
    # ask the users about the file save path they,
    # want.
    if file_save_path is None:
        # there's no file-save path.

        file_save_path = file_dialog.asksaveasfilename(
            title="Save", initialfile=file_name.get()
        )

    # get the file name, and set also.
    file_name.set(file_save_path.split('/')[-1])

    with open(file_save_path, "w") as file:
        file.writelines(text_edit.get("1.0", END))


def main():
    """"""
    # main_window()
    app = App()
    app.start_app()


if __name__ == "__main__":
    main()
