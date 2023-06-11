def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


class Sizes:
    window_WIDTH = 1000
    window_HEIGHT = 800


class Colors:
    main_color = '#ebdeff'
    white_color = 'white'
    text_color = 'black'
    button_color = '#ac98ff'
    green = '#AFE1AF'
    red = '#FF5733'


class Font:
    font_name = 'Terminal'
    base_font = ("Terminal", 25)
    standard_font = ('', 15)
    little_font = ('', 10)
