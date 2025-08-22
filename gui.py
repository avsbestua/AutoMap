import threading
import tkinter as tk
from auto_map import auto_map
import threading
from tkinter.messagebox import showinfo

def map_(self): #Create threading for funtcion auto_map
    showinfo("AutoMap", "AutoMap was launched, wait a few minutes!")
    threading.Thread(target=auto_map, args=(self.entry.get(),), daemon=True).start()

class App:
    def __init__(self):
        root = tk.Tk()
        root['bg'] = '#BCED09'
        root.title("AutoMap")
        root.geometry("450x200+500+200")
        root.resizable(width=False, height=True)

        tk.Label(root, text="Welcome to AutoMap", font=("Aptos Semibold", 25), bg='#BCED09').pack()

        self.entry = tk.Entry(root, font=("Aptos Bold", 25))
        self.entry.pack(pady=5)

        button = tk.Button(root, text="Start AutoMap", font=("Aptos Bold", 25), bg='#F0CF65', command=lambda: map_(self))
        button.pack(pady=5)

        root.mainloop()