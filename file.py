"""
for control over the files.
"""

import tkinter.filedialog as file_dialog
from tkinter.constants import END


class File:
    """to open/save/save_as files."""

    file_save_path = None

    def __init__(self, text_edit, tab):
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
        file_name = save_as_path_from_dialog.split('/')[-1]
        self.tab.set_title(file_name)

        with open(save_as_path_from_dialog, "w") as file:
            file.writelines(
                self.text_edit.get("1.0", END)
            )

        # now remove the save indicator.
        self.tab.hide_save_indicator()

        return None
