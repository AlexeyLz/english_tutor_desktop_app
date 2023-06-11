import tkinter as tk
from tkinter import messagebox

from pages.rule_page import rule_frame
from pages.menu_page import menu_frame
from pages import redirect
from styles import Colors, Font, Sizes
from texts import PracticeInsertPage
from insert_lines import InsertLine, DoubleInsertLine


def end_task(window, frame, questions):
    for question in questions:
        if not question.get_entry():
            messagebox.showinfo("Error", "Incorrect answer!")
            return
    messagebox.showinfo("Good!", "Good!\nTest passed!")
    frame.destroy()
    menu_frame(window)


def go_back_to_insert_practice(window, back_window):
    frames = window.winfo_children()
    for i in frames:
        i.destroy()
    practice_insert_frame(window, back_window)


def to_menu(window, frame):
    frame.destroy()
    back_window = tk.Toplevel(window)
    back_window['bg'] = Colors.main_color
    back_window.geometry('500x200')
    tk.Button(back_window, bg=Colors.button_color, text='GO BACK TO PRACTICE', font=Font.base_font,
              command=lambda: go_back_to_insert_practice(window, back_window)).pack(pady=50)

    rule_frame(window)


def practice_insert_frame(window, frame):
    frame.destroy()
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()
    questions = []
    lines = PracticeInsertPage.lines
    for i in range(len(lines)):
        parts = lines[i].split(' ___ ')
        obj = InsertLine(frame, parts[0], parts[1], PracticeInsertPage.answers[i])
        questions.append(obj)
    double_question = 'I play basketball ___ Tuesday and ___ Friday.'.split(' ___ ')
    double_answer = ['on', 'on']
    obj = DoubleInsertLine(frame, double_question[0], double_question[1], double_question[2], double_answer[0],
                           double_answer[1])
    questions.append(obj)
    exam_button = tk.Button(frame, font=Font.base_font, text='Finish', bg=Colors.button_color, width=12,
                            command=lambda: end_task(window, frame, questions))
    exam_button.pack(pady=30)

    rule_button = tk.Button(frame, font=Font.base_font, text='Read the rule', bg=Colors.button_color, width=12,
                            command=lambda: to_menu(window, frame))
    rule_button.pack(pady=30)
    practice_button = tk.Button(frame, font=Font.base_font, text='Menu', bg=Colors.button_color, width=12,
                                command=lambda: redirect.redirect_to_menu(window, frame))
    practice_button.pack(pady=30)
