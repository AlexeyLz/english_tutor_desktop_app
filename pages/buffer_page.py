import tkinter as tk

from pages import redirect
from styles import Colors, Font, Sizes
from texts import BufferPage
from pages.practice_insert import practice_insert_frame


def buffer_frame(window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    tk.Label(frame, text=BufferPage.well, font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)

    exam_button = tk.Button(frame, font=Font.base_font, text='Next task', bg=Colors.button_color, width=12,
                            command=lambda: practice_insert_frame(window, frame))
    exam_button.pack(pady=30)

    rule_button = tk.Button(frame, font=Font.base_font, text='Read rules', bg=Colors.button_color, width=12,
                            command=lambda: redirect.redirect_to_rule_page(window, frame))
    rule_button.pack(pady=30)
    practice_button = tk.Button(frame, font=Font.base_font, text='Menu', bg=Colors.button_color, width=12,
                                command=lambda: redirect.redirect_to_menu(window, frame))
    practice_button.pack(pady=30)
