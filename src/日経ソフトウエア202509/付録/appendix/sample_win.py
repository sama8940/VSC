import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

root = tk.Tk()
root.title("My App")

label = tk.Label(root, text="Hello, Windows App!")
label.pack()

button = tk.Button(root, text="Click me!", command=lambda: print("Button clicked!"))
button.pack()

root.mainloop()


