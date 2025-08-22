import threading
import tkinter as tk
from auto_map import auto_map
import threading
from tkinter.messagebox import showinfo, showerror


def map_(entry_get, var): #Create threading for funtcion auto_map
    if not entry_get.strip():
        showerror("Error", "Write prompt for AI")
        return
    showinfo("AutoMap", "AutoMap was launched, wait a few minutes!")
    threading.Thread(target=auto_map, args=(entry_get, var), daemon=True).start()

class App:
    def __init__(self):
        root = tk.Tk()
        root['bg'] = '#BCED09'
        root.title("AutoMap")
        root.geometry("450x200+500+200")
        root.resizable(width=False, height=True)

        tk.Label(root, text="Welcome to AutoMap", font=("Aptos Semibold", 25), bg='#BCED09').pack()

        entry = tk.Entry(root, font=("Aptos Bold", 25))
        entry.pack(pady=5)

        var = tk.StringVar()
        var.set("txt")

        rd_frame = tk.Frame(root) #Frame for radio buttons
        rd_frame.pack()

        rd1 = tk.Radiobutton(rd_frame, text="Text mode", variable=var, value="txt", bg="#BCED09", font=("Aptos Semibold", 15))
        rd1.pack(side='left')

        rd2 = tk.Radiobutton(rd_frame, text="Number mode", variable=var, value="num", bg="#BCED09", font=("Aptos Semibold", 15))
        rd2.pack()

        button = tk.Button(root, text="Start AutoMap", font=("Aptos Bold", 25), bg='#F0CF65', command=lambda: map_(entry.get(), var))
        button.pack(pady=5)

        root.mainloop()