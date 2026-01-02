# Copyright 2025-2026 Avsbest
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys

if sys.platform == 'win32':
    import threading
    import customtkinter as ctk
    from tkinter.messagebox import showinfo, showerror
    from auto_map.map import auto_map
    from PIL import Image, ImageTk
    from pathlib import Path
elif sys.platform == 'darwin':
    import threading
    import customtkinter as ctk
    from tkinter.messagebox import showinfo, showerror
    from . import auto_map
    from PIL import Image, ImageTk
    from pathlib import Path


def map_(prompt, mode, map, size_mod, optional_feature, model, font_name):  # Create threading for function auto_map
    if not prompt.strip():
        showerror("Error", "Write prompt for AI")
        return
    showinfo("AutoMap", "AutoMap was launched, wait a few minutes!")
    threading.Thread(target=auto_map.auto_map, args=(prompt, mode, map, int(size_mod), optional_feature, model, font_name), daemon=True).start()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AutoMap")
        self.geometry("480x630+650+60")
        #self.resizable(width=False, height=False)
        
        bg_color = '#B4D988'
        self.configure(fg_color=bg_color)       

        icon_image = Image.open("resources/othr/favicon.ico")
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.iconphoto(False, icon_photo)

        self.iconbitmap("resources/othr/favicon.ico")
        ctk.CTkLabel(self, text="AutoMap", font=("Kodchasan", 28), text_color='#000000').pack(pady=(10, 6))
        
        ctk.CTkLabel(self, text="Enter prompt for AI", font=("Arial Rounded MT Bold", 14), text_color='#000000').pack(pady=(8, 4))

        prompt_entry = ctk.CTkEntry(self, width=360, justify='center', height=26, font=("Arial Rounded MT Bold", 14))
        prompt_entry.insert(0, "How many bears are there in your country?")  # Default service prompt
        prompt_entry.pack(pady=(0, 10))

        ctk.CTkLabel(self, text="AutoMap mode", font=("Arial Rounded MT Bold", 16), text_color='#000000').pack(pady=(0, 4))

        mode_var = ctk.StringVar(value="txt")

        mode_frame = ctk.CTkFrame(self, bg_color=bg_color, fg_color='#343434', corner_radius=20)
        mode_frame.pack(pady=(0, 6))

        text_rd = ctk.CTkRadioButton(mode_frame, bg_color='#343434', text="Text", variable=mode_var, value="txt", font=("Arial Rounded MT Bold", 12), text_color="#FFFFFF")
        text_rd.pack(side='left', padx=8, pady=6)
        # @TODO Check values in function.py

        number_rd = ctk.CTkRadioButton(mode_frame, bg_color='#343434', text="Number", variable=mode_var, value="num", font=("Arial Rounded MT Bold", 12), text_color="#FFFFFF")
        number_rd.pack(side='left', padx=8, pady=6)

        ctk.CTkLabel(self, text="Map type", font=("Arial Rounded MT Bold", 14), text_color='#000000').pack(pady=(6, 4))

        map_mode_frame = ctk.CTkFrame(self, bg_color=bg_color, fg_color='#343434', corner_radius=20)
        map_mode_frame.pack(pady=(4, 12))

        map_var = ctk.StringVar(value="default")
        default_map_rd = ctk.CTkRadioButton(map_mode_frame, bg_color='#343434', text="Default", variable=map_var, value="default", font=("Arial Rounded MT Bold", 12), text_color="#FFFFFF")
        default_map_rd.pack(side='left', padx=8, pady=6)

        flag_map_rd = ctk.CTkRadioButton(map_mode_frame, bg_color='#343434', text="Flag", variable=map_var, value="flag", font=("Arial Rounded MT Bold", 12), text_color="#FFFFFF")
        flag_map_rd.pack(side='left', padx=8, pady=6)

        world_map_rd = ctk.CTkRadioButton(map_mode_frame, bg_color='#343434', text="World", variable=map_var, value="world", font=("Arial Rounded MT Bold", 12), text_color="#FFFFFF")
        world_map_rd.pack(side='left', padx=8, pady=6)

        ctk.CTkLabel(self, text="Global Size Modifier", font=("Arial Rounded MT Bold", 14), text_color='#000000').pack(pady=(6, 4))
        
        gsm_entry = ctk.CTkEntry(self, width=220, height=26, font=("Arial Rounded MT Bold", 14), justify='center')
        gsm_entry.insert(0, "15")  # Default size modifier
        gsm_entry.pack(pady=(0, 10))

        options_frame = ctk.CTkFrame(self, bg_color=bg_color, fg_color='#343434', corner_radius=18)
        options_frame.pack(pady=(0, 12))

        optional_feature_var = ctk.StringVar(value="none")

        none_rd = ctk.CTkRadioButton(options_frame, bg_color='#343434', text="No extra option", variable=optional_feature_var, value="none", font=("Arial Rounded MT Bold", 10), text_color="#FFFFFF")
        none_rd.pack(side='left', padx=6, pady=6) 

        most_least_rd = ctk.CTkRadioButton(options_frame, bg_color='#343434', text="Show most and least country", variable=optional_feature_var, value="most_least", font=("Arial Rounded MT Bold", 10), text_color="#FFFFFF")
        most_least_rd.pack(side='left', padx=6, pady=6)

        short_form_rd = ctk.CTkRadioButton(options_frame, bg_color='#343434', text="Write in short form", variable=optional_feature_var, value="short_form", font=("Arial Rounded MT Bold", 10), text_color="#FFFFFF")
        short_form_rd.pack(side='left', padx=6, pady=6)

        ctk.CTkLabel(self, text="Select AI Model", font=("Arial Rounded MT Bold", 14), text_color='#000000').pack(pady=(6, 4))
        
        ai_var = ctk.StringVar(value="gemma-3-27b-it")
        
        ai_model = ctk.CTkComboBox(self, width=220, height=26, font=("Arial Rounded MT Bold", 12), variable=ai_var, values=["gemma-3-27b-it", "gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3-flash"])
        ai_model.pack(pady=(0, 10))

        ctk.CTkLabel(self, text="Select Font", font=("Arial Rounded MT Bold", 14), text_color='#000000').pack(pady=(6, 4))

        font_var = ctk.StringVar(value=Path("DIN Condensed.ttf"))

        font_cb = ctk.CTkComboBox(self, width=220, height=26, font=("Arial Rounded MT Bold", 12), variable=font_var, values=[x.name for x in Path("resources/fonts").iterdir() if x.suffix == '.ttf'])
        font_cb.pack(pady=(0, 10))

        run_button = ctk.CTkButton(self, text="Run AutoMap", font=("Arial Rounded MT Bold", 22), fg_color='#343434', border_width=3, border_color="#FFFFFF", width=280, height=70, corner_radius=16,
                                   command=lambda: map_(prompt_entry.get(), mode_var.get(), map_var.get(), gsm_entry.get(), optional_feature_var.get(), ai_var.get(), font_var.get()))
        run_button.pack(pady=(6, 10))

        self.mainloop()
