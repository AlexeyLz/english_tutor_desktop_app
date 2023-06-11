import tkinter as tk
from styles import center, Colors, Sizes
import pages



window = tk.Tk()
window.title('English Tutor')
window.iconbitmap("media/icon.ico")
window.geometry(f'{Sizes.window_WIDTH}x{Sizes.window_HEIGHT}')
window.configure(bg = Colors.main_color )
window.resizable(False, False)
center(window)

pages.main_frame(window)




window.mainloop()
