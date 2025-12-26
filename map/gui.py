import sys

if sys.platform == 'win32':
    import threading
    import customtkinter as ctk
    from tkinter.messagebox import showinfo, showerror
    from auto_map.map import auto_map
    from PIL import Image, ImageTk
elif sys.platform == 'darwin':
    import threading
    import customtkinter as ctk
    from tkinter.messagebox import showinfo, showerror
    from . import auto_map
    from PIL import Image, ImageTk


def map_(prompt, mode, map, size_mod, optional_feature, model):  # Create threading for function auto_map
    if not prompt.strip():
        showerror("Error", "Write prompt for AI")
        return
    showinfo("AutoMap", "AutoMap was launched, wait a few minutes!")
    threading.Thread(target=auto_map.auto_map, args=(prompt, mode, map, int(size_mod), optional_feature, model), daemon=True).start()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AutoMap")
        self.geometry("550x790+500+0")
        self.resizable(width=False, height=False)
        
        bg_color = '#B4D988'
        self.configure(fg_color=bg_color)

        icon_image = Image.open("resources/favicon.ico")
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.iconphoto(False, icon_photo)

        self.iconbitmap("resources/favicon.ico")

        ctk.CTkLabel(self, text="AutoMap", font=("Kodchasan", 45), text_color='#000000').pack(pady=(20, 10))
        
        ctk.CTkLabel(self, text="Enter prompt for AI", font=("Arial Rounded MT Bold", 20), text_color='#000000').pack(pady=(20, 5))

        prompt_entry = ctk.CTkEntry(self, width=500, justify='center',height=40, font=("Arial Rounded MT Bold", 24))
        prompt_entry.insert(0, "How many bears are there in your country?")  # Default service prompt
        prompt_entry.pack(pady=(0, 20))

        ctk.CTkLabel(self, text="AutoMap mode", font=("Arial Rounded MT Bold", 24), text_color='#000000').pack(pady=(0, 5))

        mode_var = ctk.StringVar(value="txt")

        mode_frame = ctk.CTkFrame(self, bg_color=bg_color, fg_color='#343434', corner_radius=30)
        mode_frame.pack(pady=(0, 10))

        text_rd = ctk.CTkRadioButton(mode_frame, bg_color='#343434', text="Text", variable=mode_var, value="txt", font=("Arial Rounded MT Bold", 24), text_color="#FFFFFF")
        text_rd.pack(side='left', padx=20, pady=10)
        # @TODO Check values in function.py

        number_rd = ctk.CTkRadioButton(mode_frame, bg_color='#343434', text="Number", variable=mode_var, value="num", font=("Arial Rounded MT Bold", 24), text_color="#FFFFFF")
        number_rd.pack(side='left', padx=20, pady=10)

        ctk.CTkLabel(self, text="Map type", font=("Arial Rounded MT Bold", 20), text_color='#000000').pack(pady=(10, 5))

        map_mode_frame = ctk.CTkFrame(self, bg_color=bg_color, fg_color='#343434', corner_radius=30)
        map_mode_frame.pack(pady=(5, 20))

        map_var = ctk.StringVar(value="default")
        default_map_rd = ctk.CTkRadioButton(map_mode_frame, bg_color='#343434', text="Default", variable=map_var, value="default", font=("Arial Rounded MT Bold", 16), text_color="#FFFFFF")
        default_map_rd.pack(side='left', padx=20, pady=10)

        flag_map_rd = ctk.CTkRadioButton(map_mode_frame, bg_color='#343434', text="Flag", variable=map_var, value="flag", font=("Arial Rounded MT Bold", 16), text_color="#FFFFFF")
        flag_map_rd.pack(side='left', padx=20, pady=10)

        world_map_rd = ctk.CTkRadioButton(map_mode_frame, bg_color='#343434', text="World", variable=map_var, value="world", font=("Arial Rounded MT Bold", 16), text_color="#FFFFFF")
        world_map_rd.pack(side='left', padx=20, pady=10)

        ctk.CTkLabel(self, text="Global Size Modifier", font=("Arial Rounded MT Bold", 20), text_color='#000000').pack(pady=(10, 5))
        
        gsm_entry = ctk.CTkEntry(self, width=350, height=40, font=("Arial Rounded MT Bold", 20), justify='center')
        gsm_entry.insert(0, "15")  # Default size modifier
        gsm_entry.pack(pady=(0, 20))

        options_frame = ctk.CTkFrame(self, bg_color=bg_color, fg_color='#343434', corner_radius=30)
        options_frame.pack(pady=(0, 20))

        optional_feature_var = ctk.StringVar(value="none")

        none_rd = ctk.CTkRadioButton(options_frame, bg_color='#343434', text="No extra option", variable=optional_feature_var, value="none", font=("Arial Rounded MT Bold", 12), text_color="#FFFFFF")
        none_rd.pack(side='left', padx=10, pady=10) 

        most_least_rd = ctk.CTkRadioButton(options_frame, bg_color='#343434', text="Show most and least country", variable=optional_feature_var, value="most_least", font=("Arial Rounded MT Bold", 12), text_color="#FFFFFF")
        most_least_rd.pack(side='left', padx=10, pady=10)

        short_form_rd = ctk.CTkRadioButton(options_frame, bg_color='#343434', text="Write in short form", variable=optional_feature_var, value="short_form", font=("Arial Rounded MT Bold", 12), text_color="#FFFFFF")
        short_form_rd.pack(side='left', padx=10, pady=10)

        ctk.CTkLabel(self, text="Enter AI Model", font=("Arial Rounded MT Bold", 20), text_color='#000000').pack(pady=(10, 5))
        model_entry = ctk.CTkEntry(self, width=350, height=40, font=("Arial Rounded MT Bold", 20), justify='center')
        model_entry.insert(0, "tngtech/tng-r1t-chimera:free")  # Default model
        model_entry.pack(pady=(0, 20))

        run_button = ctk.CTkButton(self, text="Run AutoMap", font=("Arial Rounded MT Bold", 40), fg_color='#343434', border_width=5, border_color="#FFFFFF", width=400, height=130, corner_radius=20,
                                   command=lambda: map_(prompt_entry.get(), mode_var.get(), map_var.get(), gsm_entry.get(), optional_feature_var.get(), model_entry.get()))
        run_button.pack(pady=(10, 20))

        self.mainloop()
