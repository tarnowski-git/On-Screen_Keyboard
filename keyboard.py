import tkinter as tk


class Main_Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master



root = tk.Tk()
application = Main_Application(master=root)
application.mainloop()
