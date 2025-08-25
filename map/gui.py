import threading
import tkinter as tk
from tkinter.messagebox import showinfo, showerror
from auto_map.map import auto_map


def map_(entry_get, var, map_var):  # Create threading for function auto_map
    if not entry_get.strip():
        showerror("Error", "Write prompt for AI")
        return
    showinfo("AutoMap", "AutoMap was launched, wait a few minutes!")
    threading.Thread(target=auto_map.auto_map, args=(entry_get, var, map_var), daemon=True).start()


class App:
    def __init__(self):
        root = tk.Tk()
        root['bg'] = '#BCED09'
        root.title("AutoMap")
        root.geometry("450x250+500+200")
        root.resizable(width=False, height=False)

        tk.Label(root, text="Welcome to AutoMap", font=("Aptos Semibold", 25), bg='#BCED09').pack()

        entry = tk.Entry(root, font=("Aptos Bold", 25))
        entry.pack(pady=5)

        var = tk.StringVar()
        var.set("txt")

        rd_frame_mode = tk.Frame(root)  # Frame for radio buttons
        rd_frame_mode.pack()

        rd1 = tk.Radiobutton(rd_frame_mode, text="Text mode", variable=var, value="txt", bg="#BCED09",
                             font=("Aptos Semibold", 15))
        rd1.pack(side='left')

        rd2 = tk.Radiobutton(rd_frame_mode, text="Number mode", variable=var, value="num", bg="#BCED09",
                             font=("Aptos Semibold", 15))
        rd2.pack()

        map_var = tk.StringVar()  # Map variable
        map_var.set("default")
        rd_frame_map = tk.Frame(root)
        rd_frame_map.pack()

        rd_def_map = tk.Radiobutton(rd_frame_map, text="Default map", variable=map_var, value="default", bg="#BCED09",
                                    font=("Aptos Semibold", 15))
        rd_def_map.pack(side='left')

        rd_flag_map = tk.Radiobutton(rd_frame_map, text="Flag map", variable=map_var, value='flag', bg="#BCED09",
                                     font=("Aptos Semibold", 15))
        rd_flag_map.pack(side='left')

        rd_world_map = tk.Radiobutton(rd_frame_map, text="World map", variable=map_var, value='world', bg="#BCED09",
                                     font=("Aptos Semibold", 15))

        rd_world_map.pack(side='left')

        button = tk.Button(root, text="Start AutoMap", font=("Aptos Bold", 25), bg='#F0CF65',
                           command=lambda: map_(entry.get(), var, map_var))
        button.pack(pady=5)

        root.mainloop()
