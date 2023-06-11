import tkinter as tk
from styles import Colors, Font, Sizes
from texts import StartPage
from user import User
from pages.menu_page import menu_frame

def go_to_menu(frame, name_input, window):
    name = name_input.get()
    User.name = name
    frame.destroy()
    menu_frame(window=window)




def main_frame(window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()
    tk.Label(frame, text=StartPage.hello_text, font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)
    tk.Label(frame, text=StartPage.name, font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=10)

    name_input = tk.Entry(frame, font=Font.base_font, width=15, justify=tk.CENTER)
    name_input.pack(pady=10)
    submit_button = tk.Button(frame, font=Font.base_font, text='Submit',bg = Colors.button_color, command=lambda: go_to_menu(frame, name_input, window))
    submit_button.pack(pady=30)
