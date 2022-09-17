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

from defaults import *
from tools import Tools
import tkinter
from tkinter.constants import END
import tkinter.filedialog as file_dialog
from time import sleep as delay
# TO-DO:
# [1]- make sure to add line number, mean that user can they,
# know the line number.
# [2]- save or not save indicator, like the one in arduino IDE.
# [3]- make sure to add some useful info in the bottom label, like the,
# vscode show us the cursor position and the interpreter and etc...
# [4]- add settings page to control of the font size and the last open,
# files, and font color....etc.
# [5]- separate the program into group of files (constants, tools, ..., etc)
# [6]- add animation for all editor components.


Tools.clear()


class Tab:
    """file tab for showing the file name, and with the current tab indicator"""

    all_tabs = []

    def __init__(self, master: tkinter.Tk, tab_text="Untitled"):

        self.master = master

        # create the the Tab main Frame.
        self.tab = tkinter.Frame(
            master, **TAB_PROPERTIES)

        # create the var to store the tab title content inside of it.
        self.tab_text = tkinter.StringVar(master=self.tab)
        self.tab_text.set(tab_text)

        # create the tab title.
        self.tab_text_label = tkinter.Label(
            self.tab, textvariable=self.tab_text, **TAB_TEXT_PROPERTIES)

        # create the save indicator.
        self.tab_save_indicator = tkinter.Label(
            self.tab, text=TAB_SAVE_INDICATOR_CHARACTER, **TAB_SAVE_INDICATOR_PROPERTIES)

        # get the required width to print the text on the label,
        # so we can center the title.
        text_required_width = self.tab_text_label.winfo_reqwidth()

        self.tab_text_label.place(x=abs(text_required_width-260)//2, y=11)

        # create Tab Indicator Frame for showing the current tab.
        self.tab_indicator = tkinter.Frame(
            master, ** TAB_INDICATOR_PROPERTIES)

        Tab.all_tabs.append(self)

    def place(self, x: int, y: int):
        """place the tab with its own indicator on the window,
        in specific coordinates.
        return True if everything go fine else it will raise an Error."""

        self.tab.place(x=x, y=y)
        self.tab_indicator.place(x=x, y=y-1)
        self.tab_save_indicator.place(x=5, y=1)

        return True

    def show_save_indicator(self):
        """show the save indicator for the tab,
        when the user edit the file or do any thing in the file."""
        self.tab_save_indicator.place(x=5, y=1)

        return None

    def hide_save_indicator(self):
        """hide the save indicator when the user save the file,
        or you can say save the changes."""
        self.tab_save_indicator.place_forget()

        return None

    def set_title(self, title: str):
        """change the tab title"""

        self.tab_text.set(title)

        return None

    def animation(self):
        """create animation for the tab indicator,
        when the user click on it."""

        for width in range(1, 261):
            self.tab_indicator.configure(width=width)
            self.master.update()
            delay(3e-4)

        return True

    def __repr__(self):

        return f"Tab({self.master}, '{self.file_name}')"


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

        # create the Tab title.
        tab = Tab(self)
        tab.place(228, 7)

        # create The main Text widget for edit and save our text.
        text_edit = tkinter.Text(self, **TEXT_EDIT_PROPERTIES)
        text_edit.place(x=0, y=48)

        # create empty file.
        initial_file = File(text_edit, tab)

        # create the main buttons.
        save_btn = tkinter.Button(
            self, text="Save", command=initial_file.save, **BTN_PROPERTIES)
        save_btn.place(x=3, y=12)

        save_as_btn = tkinter.Button(
            self, text="Save As", command=initial_file.save_as, **BTN_PROPERTIES)
        save_as_btn.place(x=58, y=12)

        open_btn = tkinter.Button(
            self, text="Open", command=initial_file.open, **BTN_PROPERTIES)
        open_btn.place(x=132, y=12)

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


class File:
    """to open/save/save_as files."""

    file_save_path = None

    def __init__(self, text_edit: tkinter.Text, tab: Tab):
        self.text_edit = text_edit
        self.tab = tab

    def __repr__(self):
        return f"File({self.text_edit}, {self.tab})"

    def open(self):
        """
        open any file.
        return True if everything go fine other wise False"""

        open_path_from_dialog = file_dialog.askopenfilename(title="Open")

        # guard conditions.
        if not isinstance(open_path_from_dialog, str):
            # that happen when the user click on the cancel,
            # button on the dialog.
            # in this case end everything.
            return False

        File.file_save_path = open_path_from_dialog

        # now get the file name from the file path,
        # for set it for the tab title.
        file_name = File.file_save_path.split('/')[-1]

        # set the title and hide the save indicator.
        self.tab.set_title(file_name)
        self.tab.hide_save_indicator()

        with open(File.file_save_path, "r") as file:
            file_data = file.readlines()

        # concatenate all the string on the file_data list.
        text_data = "".join(file_data)

        # before we insert anything we must insure we,
        # clear the Text on the Widget before.
        self.text_edit.delete("1.0", END)

        # now we will insert the string in Text widget.
        self.text_edit.insert(END, text_data)

        return True

    def save(self):
        """
        save the current file,
        this will update the save path and update,
        the file name on the tab, and save our file.

        return True if everything go fine otherwise return False.
        """

        # first checkout if we have save-path or not,
        # if we have save the file directly , if not,
        # ask the users about the file save path they,
        # want.
        if File.file_save_path is None:
            # there's no file-save path.

            File.file_save_path = file_dialog.asksaveasfilename(
                title="Save", initialfile=self.tab.tab_text.get()
            )

        # now get the file name from the file path,
        # for set it for the tab title.
        file_name = File.file_save_path.split('/')[-1]
        self.tab.set_title(file_name)

        with open(File.file_save_path, "w") as file:
            file.writelines(self.text_edit.get("1.0", END))

        # now remove the save indicator.
        self.tab.hide_save_indicator()

        return True

    def save_as(self):
        """
        using this the user can select new save path,
        or change the file name and this also will update,
        the file-save path and also the file name on the tab.
        return True if everything go fine otherwise False"""

        save_as_path_from_dialog = file_dialog.asksaveasfilename(
            title="Save As",
            initialfile=self.tab.tab_text.get()
        )
        # now get the file name from the file path,
        # for set it for the tab title.
        file_name = File.file_save_path.split('/')[-1]
        self.tab.set_title(file_name)

        with open(File.file_save_path, "w") as file:
            file.writelines(
                self.text_edit.get("1.0", END)
            )

        # now remove the save indicator.
        self.tab.hide_save_indicator()

        return None


def main():
    """"""
    # main_window()
    app = App()
    app.start_app()


if __name__ == "__main__":
    main()
