import tkinter as tk

root = tk.Tk()
root.title("auto map")
root.geometry("800x500")
root["bg"] = "#F0EAD6"

def action():
    text = entry.get()

entry = tk.Entry(root,font=("Arial Bold",50),width=5,)
entry.place(x=550,y=200)


title = tk.Label (root, text="welcome to auto map", font=("Arial Bold", 19),bg="#F0EAD6")
title.place(x=270,y= 20)



label = tk.Label(root,  text="information",font=("Arial Bold",20),width=40,height=2,bg="#F0EAD6")
label.place(x=300,y= 150)



button = tk.Button(root,text="start",font=("Arial Bold",12),width=20,height=2)
button.place(x=285,y =120)



root.mainloop()




