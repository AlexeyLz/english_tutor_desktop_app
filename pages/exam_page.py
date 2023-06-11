import tkinter as tk
from tkinter import messagebox

from styles import Colors, Font, Sizes
from texts import ExamPage
from user import User
from insert_lines import InsertLine, DoubleInsertLine
from pages.redirect import redirect_to_menu


def redirect(frame, frame_numbers, window):
    frame_numbers.destroy()
    redirect_to_menu(window, frame)


def end_exam_frame(frame_numbers, window, score):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    tk.Label(frame, text=User.name+', Great!\n'+'Your score: ' + str(score), font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)

    button = tk.Button(frame, font=Font.base_font, text='Go to menu', width=14, bg=Colors.button_color,
                       command=lambda: redirect(frame, frame_numbers, window))
    button.pack(pady=50)


def next_exam(frame, window, index, obj, frame_numbers, score, buttons):
    if obj.get_entry():
        buttons[index - 1].configure(bg=Colors.green)
        score += 1
    else:
        buttons[index - 1].configure(bg=Colors.red)

    try:
        frame.destroy()
    except:
        pass

    lines = ExamPage.lines
    answers = ExamPage.answers

    if index == len(answers):
        window.update()
        end_exam_frame(frame_numbers, window, score)
        return
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    data = lines[index].split(' ___ ')

    if len(data) == 2:
        obj = InsertLine(frame, data[0], data[1], answers[index])
    elif len(data) == 3:
        answers = answers[index].split('/')
        obj = DoubleInsertLine(frame, data[0], data[1], data[2], answers[0], answers[1])

    submit_button = tk.Button(frame, font=Font.base_font, text='Answer', width=9, bg=Colors.button_color, )
    submit_button.configure(
        command=lambda but=submit_button: next_exam(frame, window, index + 1, obj, frame_numbers, score, buttons))
    submit_button.pack(pady=50)


def exam_frame(window, frame):
    frame.destroy()

    lines = ExamPage.lines
    answers = ExamPage.answers

    frame_numbers = tk.Frame(window, width=Sizes.window_WIDTH, height=100, bg=Colors.main_color)
    frame_numbers.pack(pady = 50)
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()
    buttons = []
    for i in range(len(answers)):
        btn = tk.Button(frame_numbers, text=str(i + 1), font=Font.base_font, bg='grey', fg=Colors.white_color)
        btn.pack(side=tk.LEFT)
        buttons.append(btn)

    index = 0
    score = 0

    data = lines[index].split(' ___ ')
    if len(data) == 2:
        obj = InsertLine(frame, data[0], data[1], answers[index])
    elif len(data) == 3:
        answers = answers[index].split('/')
        obj = DoubleInsertLine(frame, data[0], data[1], data[2], answers[0], answers[1])

    submit_button = tk.Button(frame, font=Font.base_font, text='Answer', width=9, bg=Colors.button_color,
                              )
    submit_button.configure(
        command=lambda but=submit_button: next_exam(frame, window, index + 1, obj, frame_numbers, score, buttons))
    submit_button.pack(pady=50)
