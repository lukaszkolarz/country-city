import Gui as g
import tkinter as tk

root = tk.Tk()
window = g.Gui(root)
root.mainloop()

if window.country != "":
    print(window.country)
