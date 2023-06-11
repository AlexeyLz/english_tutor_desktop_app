import tkinter as tk
from styles import Colors, Font, Sizes
from texts import RulePage
from pages.end_rule_page import end_rule_frame


def end_rules(frame, window, button):
    button.destroy()
    frame.destroy()
    end_rule_frame(window)


def third_rule_frame(frame, window, button):
    button.destroy()
    frame.destroy()
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()
    rule2 = tk.PhotoImage(file='media/rule_2.png').subsample(2)
    c = tk.Canvas(frame, width=606, height=364, bg='black')
    c.pack(pady=10)
    c.create_image(305, 184, image=rule2)
    c.image = rule2
    tk.Label(frame, text=RulePage.rule_third_text, font=Font.standard_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=30)

    next_button = tk.Button(window, font=Font.base_font, text='Next', width=9, bg=Colors.button_color, )
    next_button.configure(command=lambda: end_rules(frame, window, next_button))
    next_button.place(x=Sizes.window_WIDTH - 230, y=Sizes.window_HEIGHT - 80)


def second_rule_frame(frame, window, button):
    button.destroy()
    frame.destroy()
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    rule2 = tk.PhotoImage(file='media/table_rule.png')
    c = tk.Canvas(frame, width=560, height=658, bg='black')
    c.pack(pady=10)
    c.create_image(280, 330, image=rule2)
    c.image = rule2

    next_button = tk.Button(window, font=Font.base_font, text='Next', width=9, bg=Colors.button_color, )
    next_button.configure(command=lambda: third_rule_frame(frame, window, next_button))
    next_button.place(x=Sizes.window_WIDTH - 230, y=Sizes.window_HEIGHT - 80)


def rule_frame(window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()
    rule1 = tk.PhotoImage(file='media/rule_1.png')
    c = tk.Canvas(frame, width=606, height=364, bg='black')
    c.pack(pady=10)
    c.create_image(305, 184, image=rule1)
    c.image = rule1
    tk.Label(frame, text=RulePage.rule_first_text, font=Font.standard_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)

    next_button = tk.Button(window, font=Font.base_font, text='Next', width=9, bg=Colors.button_color, )
    next_button.configure(command=lambda: second_rule_frame(frame, window, next_button))
    next_button.place(x=Sizes.window_WIDTH - 230, y=Sizes.window_HEIGHT - 80)


