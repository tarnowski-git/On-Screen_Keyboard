import tkinter as tk
from functools import partial


class Main_Application(tk.Frame):

    BUTTONS = [
        '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', "Backspace", '*',
        'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', '7', '8', '9',
        "CapsLock", 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "Enter", '4', '5', '6',
        "Shift", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', "Shift", '1', '2', '3',
        "Space"
    ]

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("On-Screen Keyboard")
        self.master.resizable(0, 0)
        self.master.config(bg="sky blue")
        self.text_box = tk.Text(master, width=90, height=10, wrap=tk.WORD)
        self.text_box.grid(row=0, column=0, columnspan=40, padx=10, pady=10)

        var_row = 4
        var_col = 0
        for button in self.BUTTONS:

            # partial takes care of function and argument
            cmd = partial(self.button_command, button)

            if button != "Space":
                tk.Button(master, text=button, width=8, bg="black", fg="white",
                          command=cmd).grid(row=var_row, column=var_col)
            else:
                tk.Button(master, text=button, width=40, bg="black", fg="white", command=cmd).grid(
                    columnspan=40, row=var_row, column=var_col)

            if var_col > 14:
                var_col = 0
                var_row = var_row + 1

            var_col = var_col + 1

    def button_command(self, button):
        print("What Iam pressed?: " + button)
        return


root = tk.Tk()
application = Main_Application(master=root)
application.mainloop()
