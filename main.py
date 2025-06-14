import tkinter as tk
from tkinter import ttk

class Interface(tk.Tk):
    def __init__ (self):
        super().__init__()
        self.geometry("500x500")
        self.title("titulo bonito!!!")
        self.columnconfigure(0, weight=1)

        input_ticker = Input(self, "ticker")
        input_ticker.grid(row = 0, column = 0)

class Input(ttk.Frame):
    def __init__ (self, parent, label): 
        super().__init__()
        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=1, padx=30) 
        self.label = ttk.Label(self, text=f"Enter {label}:", anchor="w")
        self.label.grid(row=0, column=0, sticky="w")


def main():
    inteface = Interface()
    inteface.mainloop()

if __name__ == "__main__":
    main()