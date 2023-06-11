import tkinter as tk

from styles import Colors, Font, Sizes


class InsertLine:
    def __init__(self, frame, text1, text2, answer):
        self.answer = answer
        self.line_frame = tk.Frame(frame, width=Sizes.window_WIDTH, height=100, bg=Colors.main_color)
        self.line_frame.pack(anchor = tk.NW)
        tk.Label(self.line_frame, text=text1, font=Font.standard_font,
                 bg=Colors.main_color,
                 fg=Colors.text_color).pack(side=tk.LEFT, padx=30)
        self.entry = tk.Entry(self.line_frame, font=Font.standard_font, width=5, justify = tk.CENTER)
        self.entry.pack(side=tk.LEFT, padx=30)
        tk.Label(self.line_frame, text=text2, font=Font.standard_font,
                 bg=Colors.main_color,
                 fg=Colors.text_color).pack(side=tk.LEFT, padx=30)

    def get_entry(self):
        return self.entry.get() == self.answer


class DoubleInsertLine:
    def __init__(self, frame, text1, text2, text3, answer1, answer2):
        self.answer1 = answer1
        self.answer2 = answer2
        self.line_frame = tk.Frame(frame, width=Sizes.window_WIDTH, height=100, bg=Colors.main_color)
        self.line_frame.pack()
        tk.Label(self.line_frame, text=text1, font=Font.standard_font,
                 bg=Colors.main_color,
                 fg=Colors.text_color).pack(side=tk.LEFT, padx=30)
        self.entry1 = tk.Entry(self.line_frame, font=Font.standard_font, width=5,justify = tk.CENTER)
        self.entry1.pack(side=tk.LEFT, padx=30)
        tk.Label(self.line_frame, text=text2, font=Font.standard_font,
                 bg=Colors.main_color,
                 fg=Colors.text_color).pack(side=tk.LEFT, padx=30)
        self.entry2 = tk.Entry(self.line_frame, font=Font.standard_font, width=5,justify = tk.CENTER)
        self.entry2.pack(side=tk.LEFT, padx=30)
        tk.Label(self.line_frame, text=text3, font=Font.standard_font,
                 bg=Colors.main_color,
                 fg=Colors.text_color).pack(side=tk.LEFT, padx=30)

    def get_entry(self):
        return self.entry1.get() == self.answer1 and self.entry2.get() == self.answer2