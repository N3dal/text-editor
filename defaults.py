
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
