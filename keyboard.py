import tkinter as tk
from functools import partial


class Main_Application(tk.Frame):

    BUTTONS = [
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', "Backspace", '7', '8', '9', '-',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "Enter", '4', '5', '6', '+',
        "Shift", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', "Shift", '1', '2', '3', '/',
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
        self.is_shift = False

        var_row = 4
        var_col = 0
        for button in self.BUTTONS:

            if var_col > 14:
                var_col = 0
                var_row = var_row + 1

            # partial takes care of function and argument instead of 'lambda'
            cmd = partial(self.button_command, button)

            if button != "Space":
                btn = tk.Button(master, text=button, width=8,
                                bg="black", fg="white", relief="raised", command=cmd)
                btn.grid(row=var_row, column=var_col)
            else:
                tk.Button(master, text=button, width=40, bg="black", fg="white", command=cmd).grid(
                    columnspan=40, row=var_row, column=var_col)

            var_col = var_col + 1

    def button_command(self, button):
        if button == "Space":
            self.text_box.insert(tk.INSERT, ' ')
        elif button == "Enter":
            self.text_box.insert(tk.INSERT, '\n')
        elif button == "Tab":
            self.text_box.insert(tk.INSERT, '   ')
        elif button == "Backspace":
            self.text_box.delete(tk.INSERT, tk.END)
        elif button == "Shift":
            self.is_shift = True
            return None
        else:
            if self.is_shift == True:
                self.text_box.insert(tk.INSERT, button.capitalize())

            else:
                self.text_box.insert(tk.INSERT, button)
        # afer clicking anthing, a shift must gone
        self.is_shift = False


root = tk.Tk()
application = Main_Application(master=root)
application.mainloop()
