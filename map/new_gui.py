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


def map_(prompt, var, map_var, size_mod, most_short_form_flag, model):  # Create threading for function auto_map
    if not prompt.strip():
        showerror("Error", "Write prompt for AI")
        return
    showinfo("AutoMap", "AutoMap was launched, wait a few minutes!")
    threading.Thread(target=auto_map.auto_map, args=(prompt, var, map_var, int(size_mod), most_short_form_flag, model), daemon=True).start()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AutoMap")
        self.geometry("650x800+500+0")
        self.resizable(width=False, height=False)

        # Set background image
        self.bg_image = ctk.CTkImage(
            light_image=Image.open("resources/bg_gui.png"),
            dark_image=Image.open("resources/bg_gui.png"),
            size=(700, 850) # Розмір має збігатися з geometry
        )

        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.container = ctk.CTkFrame(self.bg_label, fg_color="transparent", bg_color="transparent")
        self.container.place(x=0, y=0, relwidth=1, relheight=1)

        tittle = ctk.CTkLabel(self.container, text="AutoMap", font=("Arial Rounded MT Bold", 64))
        tittle.pack(pady=(20, 10))



        self.mainloop()
