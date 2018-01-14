import tkinter as tk
from tkinter import *
class Gui():
    def __init__(self, root):
        root.maxsize(width=1280, height=960)
        root.minsize(width=1280, height=960)
        
        self.root=root
        self.entry = tk.Entry(root)

        self.canvas=tk.Canvas(root, width=1280, height=720, background='white')
        self.canvas.grid(row=0,column=0)

        frame = Frame(self.root)
        frame.grid(row=1,column=0, sticky="n")

        self.create_widgets(frame)
        figure1=self.canvas.create_rectangle(80, 80, 120, 120, fill="blue")

        self.create_warmup(frame)
        self.create_quit(frame)

    def create_preview(self):
        self.canvas = tk.Canvas(self.master, width = 1280, height = 720,
                            bg = "black" )
            
    def create_widgets(self, frame):
        self.create_player_options(0, frame)
        self.create_player_options(1, frame)

    def create_player_options(self, number, frame):
        player_title = Label(frame, text="Player "+str(number+1)).grid(row=1,column=number*2, sticky="n")
        twitter_label = Label(frame, text="Twitter").grid(row=2,column=number*2, sticky="w")
        twitch_label = Label(frame, text="Twitch").grid(row=3,column=number*2, sticky="w")
        twitter = Entry(frame).grid(row = 2,column = number*2+1, padx = 10, pady = 5,sticky = E+W)
        twitch = Entry(frame).grid(row = 3,column = number*2+1, padx = 10, pady = 5,sticky = E)
        
    def create_warmup(self, frame):
        toggle_switch = tk.Button(frame, text = "Toggle Warmup")
        toggle_switch.grid(row = 3, column = 5)

    def toggle_warmup(self):
        # show warmup image
        pass
        
    def create_quit(self, frame):
        self.quit = Button(frame, text="QUIT", fg="red",
                              command=quit)
        self.quit.grid(row = 4, column = 5)
        
if __name__== '__main__':
    root=tk.Tk()
    gui=Gui(root)
    root.mainloop()
