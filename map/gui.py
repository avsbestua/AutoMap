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


def map_(prompt, var, map_var, size_mod, most_short_form_flag):  # Create threading for function auto_map
    if not prompt.strip():
        showerror("Error", "Write prompt for AI")
        return
    showinfo("AutoMap", "AutoMap was launched, wait a few minutes!")
    threading.Thread(target=auto_map.auto_map, args=(prompt, var, map_var, int(size_mod), most_short_form_flag), daemon=True).start()


class App:
    def __init__(self):
        bg_color = "#FFCF20" #background color
        fg_color = "#000000" #foreground/text color
        root = tk.Tk()
        root['bg'] = bg_color
        root.title("AutoMap")
        root.iconbitmap(r'resources/favicon.ico')
        root.geometry("600x380+500+200")
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

        most_short_form_var = tk.StringVar()
        most_short_form_var.set("none") # default no option selected
        most_least_check = tk.Radiobutton(root, text="Show most and least country", variable=most_short_form_var, bg=bg_color, fg=fg_color,
                                          font=("Consolas Bold", 15), value='most_least')
        most_least_check.pack()

        write_short_form_check = tk.Radiobutton(root, text="Write in short form", variable=most_short_form_var, bg=bg_color, fg=fg_color,
                                          font=("Consolas Bold", 15), value='short_form')
        write_short_form_check.pack()

        none_radiobutton = tk.Radiobutton(root, text="None of the above", variable=most_short_form_var, bg=bg_color, fg=fg_color,
                                          font=("Consolas Bold", 15), value='none')
        none_radiobutton.pack()

        button = tk.Button(root, text="Start AutoMap", font=("Consolas Bold", 25), bg='#FFC914', fg=fg_color,
                           command=lambda: map_(entry.get(), var, map_var, size_mod_entry.get(), most_short_form_var.get()))
        button.pack(pady=5)

        root.mainloop()
