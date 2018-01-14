import tkinter as tk
from tkinter import *
class Gui():
    def __init__(self, root):
        root.maxsize(width=1280, height=960)
        root.minsize(width=1280, height=960)
        
        self.root=root
        self.entry = tk.Entry(root)
        stvar=tk.StringVar()
        stvar.set("Player 1")

        self.canvas=tk.Canvas(root, width=1280, height=720, background='white')
        self.canvas.grid(row=0,column=0)

        frame = Frame(self.root)
        frame.grid(row=1,column=0, sticky="n")

        self.option=tk.OptionMenu(frame, stvar, "Player 1", "Player 2")
        label1=Label(frame, text="Figure").grid(row=1,column=0, sticky="nw")
        label2=Label(frame, text="X").grid(row=2,column=0, sticky="w")
        label3=Label(frame, text="Y").grid(row=3,column=0, sticky="w")
        self.option.grid(row=1,column=1,sticky="nwe")
        entry = Entry(frame).grid(row = 2,column = 1,sticky = E+ W)
        entry1 = Entry(frame).grid(row = 3,column = 1, sticky = E)
        Button1=Button(frame,text="Draw").grid(row = 4,column = 1, sticky = "we")
        figure1=self.canvas.create_rectangle(80, 80, 120, 120, fill="blue")

        # Grid.rowconfigure(self.root,0,weight=720)

    def create_preview(self):
        self.canvas = tk.Canvas(self.master, width = 1280, height = 720,
                            bg = "black" )
            
    def create_widgets(self):
        self.create_warmup()
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        
        
    def create_warmup(self):
        self.warmup_toggle = tk.Button(self)
        self.warmup_toggle["text"] = "Toggle Warmup"
        self.warmup_toggle["command"] = self.toggle_warmup()

    def toggle_warmup(self):
        pass
        # show warmup image
        
if __name__== '__main__':
    root=tk.Tk()
    gui=Gui(root)
    root.mainloop()
