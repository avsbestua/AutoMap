import sys

if sys.platform == 'win32':
    import threading
    import tkinter as tk
    from tkinter.messagebox import showinfo, showerror
    from auto_map.map import auto_map
elif sys.platform == 'darwin':
    import threading
    import tkinter as tk
    from tkinter.messagebox import showinfo, showerror
    from . import auto_map


def map_(entry_get, var, map_var, size_mod, most_least_flag):  # Create threading for function auto_map
    if not entry_get.strip():
        showerror("Error", "Write prompt for AI")
        return
    showinfo("AutoMap", "AutoMap was launched, wait a few minutes!")
    threading.Thread(target=auto_map.auto_map, args=(entry_get, var, map_var, int(size_mod), most_least_flag), daemon=True).start()


class App:
    def __init__(self):
        bg_color = '#E4572E' #background color
        fg_color = '#2E282A' #foreground/text color
        root = tk.Tk()
        root['bg'] = bg_color
        root.title("AutoMap")
        root.iconbitmap(r'resources/favicon.ico')
        root.geometry("600x280+500+200")
        root.resizable(width=False, height=False)

        tk.Label(root, text="Welcome to AutoMap!", font=("Consolas Bold", 25), bg=bg_color, fg=fg_color).pack()

        entry = tk.Entry(root, font=("Consolas Bold", 25))
        entry.pack(pady=5)

        var = tk.StringVar()
        var.set("txt") # AutoMap mode variable (text/number)

        rd_frame_mode = tk.Frame(root)  # Frame for radio buttons
        rd_frame_mode.pack()

        rd1 = tk.Radiobutton(rd_frame_mode, text="Text mode", variable=var, value="txt", bg=bg_color, fg=fg_color,
                             font=("Consolas Bold", 15))
        rd1.pack(side='left')

        rd2 = tk.Radiobutton(rd_frame_mode, text="Number mode", variable=var, value="num", bg=bg_color, fg=fg_color,
                             font=("Consolas Bold", 15))
        rd2.pack()

        map_var = tk.StringVar()  # Map variable (default/flag/world)
        map_var.set("default") # default map by default
        rd_frame_map = tk.Frame(root) # Frame for map radio buttons
        rd_frame_map.pack()

        rd_def_map = tk.Radiobutton(rd_frame_map, text="Default map", variable=map_var, value="default", bg=bg_color, fg=fg_color,
                                    font=("Consolas Bold", 15))
        rd_def_map.pack(side='left')

        rd_flag_map = tk.Radiobutton(rd_frame_map, text="Flag map", variable=map_var, value='flag', bg=bg_color, fg=fg_color,
                                     font=("Consolas Bold", 15))
        rd_flag_map.pack(side='left')

        rd_world_map = tk.Radiobutton(rd_frame_map, text="World map", variable=map_var, value='world', bg=bg_color, fg=fg_color,
                                     font=("Consolas Bold", 15))

        rd_world_map.pack(side='left')

        tk.Label(root, text="Enter Global Size Modifier and check the most-least checkbox", font=("Consolas Bold", 17), bg=bg_color, fg=fg_color).pack()

        size_mod_entry = tk.Entry(root, font=("Consolas Bold", 20))
        size_mod_entry.pack(pady=5)
        size_mod_entry.insert(0, 15)

        most_least_var = tk.BooleanVar()
        most_least_check = tk.Checkbutton(root, text="Show most and least country", variable=most_least_var, bg=bg_color, fg=fg_color,
                                          font=("Consolas Bold", 15), onvalue=True, offvalue=False)
        most_least_check.pack()

        button = tk.Button(root, text="Start AutoMap", font=("Consolas Bold", 25), bg='#FFC914', fg=fg_color,
                           command=lambda: map_(entry.get(), var, map_var, size_mod_entry.get(), most_least_var.get()))
        button.pack(pady=5)

        root.mainloop()
