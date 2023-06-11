import tkinter as tk
from styles import Colors, Font, Sizes
from texts import EndRulePage
from user import User
import pages.redirect as redirect


def end_rule_frame(window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()
    tk.Label(frame, text=User.name + EndRulePage.end_rule, font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)

    tk.Label(frame, text=EndRulePage.end_rule_lets, font=Font.standard_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)

    rule_button = tk.Button(frame, font=Font.base_font, text='Read again', bg=Colors.button_color, width=12,
                            command=lambda :redirect.redirect_to_rule_page(window, frame))
    rule_button.pack(pady=30)
    practice_button = tk.Button(frame, font=Font.base_font, text='Menu', bg=Colors.button_color, width=12,
                                command = lambda : redirect.redirect_to_menu(window, frame))
    practice_button.pack(pady=30)
    exam_button = tk.Button(frame, font=Font.base_font, text='Practice', bg=Colors.button_color, width=12,
                            command = lambda : redirect.redirect_to_practice(window, frame))
    exam_button.pack(pady=30)
