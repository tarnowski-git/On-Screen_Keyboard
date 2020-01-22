import tkinter as tk
from functools import partial


class Main_Application(tk.Frame):

    keys_list = [
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', "Backspace", '7', '8', '9', '-',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':', "Enter", '4', '5', '6', '+',
        'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', ')', "Shift", '1', '2', '3', '/',
        "Space"
    ]

    shift_list = [
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', "Backspace", '7', '8', '9', '-',
        'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', "Enter", '4', '5', '6', '+',
        'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', ')', "Shift", '1', '2', '3', '/',
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
        index = 0
        self.button = list(range(len(self.keys_list)))
        for key in self.keys_list:

            if var_col > 14:
                var_col = 0
                var_row = var_row + 1

            # partial takes care of function and argument instead of 'lambda'
            cmd = partial(self.button_command, key)

            self.button[index] = tk.Button(master, text=key, width=8, bg="black", fg="white", relief="raised",
                                           padx=2, pady=2, bd=2, command=cmd)

            # setup_layout
            if key != "Space":
                self.button[index].grid(row=var_row, column=var_col)
            else:
                self.button[index]['width'] = 40
                self.button[index].grid(
                    columnspan=40, row=var_row, column=var_col)

            var_col = var_col + 1

    def button_command(self, button):
        """Function for detecting pressed buttons."""

        if button == "Space":
            self.text_box.insert(tk.INSERT, ' ')
        elif button == "Enter":
            self.text_box.insert(tk.INSERT, '\n')
        elif button == "Tab":
            self.text_box.insert(tk.INSERT, '   ')
        elif button == "Backspace":
            # The delete method of the text widget takes two indexes,
            # and will delete the characters between those indexes
            self.text_box.delete("insert -1 chars", tk.INSERT)
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
