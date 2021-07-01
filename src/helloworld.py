import tkinter as tk

def copy():
    copied["text"] = entry.get()

window = tk.Tk()
window.title("Hello World!")
window.geometry("800x640")
window.columnconfigure((0,2), weight=1)
window.columnconfigure(1, weight=3)

frame = tk.Frame(master=window)
frame.grid(row=0, column=1)
frame.columnconfigure(0, weight=3)
frame.columnconfigure(1, weight=1)

greeting = tk.Label(master=frame, text="Hello, Tkinter")
greeting.grid(row=0, column=0, columnspan=2)

entry = tk.Entry(master=frame)
entry.grid(row=1, column=0)

click = tk.Button(master=frame, text="Click Here", command=copy)
click.grid(row=1, column=1)

copied = tk.Label(master=frame)
copied.grid(row=2, column=0, columnspan=2)

window.mainloop()