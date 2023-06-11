import tkinter as tk
from styles import Colors, Font, Sizes
from texts import MenuPage
from user import User
from pages.rule_page import rule_frame
from pages.redirect import redirect_to_practice
from pages.exam_page import exam_frame

def open_rule(frame, window):
    frame.destroy()
    rule_frame(window)


def open_practice(frame, window):
    frame.destroy()
    rule_frame(window)


def menu_frame(window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()
    tk.Label(frame, text=User.name + MenuPage.choose, font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)

    rule_button = tk.Button(frame, font=Font.base_font, text='Rule', bg=Colors.button_color, width=9,
                            command=lambda: open_rule(frame, window))
    rule_button.pack(pady=30)
    practice_button = tk.Button(frame, font=Font.base_font, text='Practice', bg=Colors.button_color, width=9,
                                command=lambda: redirect_to_practice(window, frame))
    practice_button.pack(pady=30)
    exam_button = tk.Button(frame, font=Font.base_font, text='Exam', bg=Colors.button_color, width=9,
                            command = lambda: exam_frame(window, frame))
    exam_button.pack(pady=30)
