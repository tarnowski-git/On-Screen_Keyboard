import tkinter as tk
from functools import partial


class Main_Application(tk.Frame):
    """Main class of application"""

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
                # init variables
        self.master = master
        self.is_shift = False
        self.buttons_list = list(range(len(self.keys_list)))
        self.configure_gui()
        self.create_widgets()
        self.setup_layout()


    def configure_gui(self):
        """Setting general configurations of the application"""
        
        self.master.title("On-Screen Keyboard")
        self.master.resizable(0, 0)
        self.master.config(bg="sky blue")

    def create_widgets(self):
        """Creating the widgets of the application"""

        # create a place to wriring
        self.text_box = tk.Text(self.master, width=90, height=10, wrap=tk.WORD, font=("Arial", 15, "bold"))
        # create buttons
        index = 0
        for key in self.keys_list:

            # partial takes care of function and argument instead of 'lambda'
            cmd = partial(self.button_command, key)

            # assign new button to the list
            self.buttons_list[index] = tk.Button(self.master, text=key, width=8, bg="black", fg="white", relief="raised",
                                                 padx=2, pady=2, bd=2, command=cmd, font=("Arial", 9, "bold"))

            # for Space make the button wider
            if key == "Space":
                self.buttons_list[index]['width'] = 40

            # go to the next list item
            index += 1

    def setup_layout(self):
        """Setup grid system"""

        self.text_box.grid(row=0, column=0, columnspan=40, padx=10, pady=10)
        # setup the buttons
        var_row = 4
        var_col = 0
        for button in self.buttons_list:
            # after 15 columns, go to the next row
            if var_col > 14:
                var_col = 0
                var_row = var_row + 1

            # for Space make a 'columnspan' 
            if button['text'] != "Space":
                button.grid(row=var_row, column=var_col)
            else:
                button.grid(
                    columnspan=40, row=var_row, column=var_col)

            # go to the next column
            var_col += 1

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
            self.shift_keyboard()
            return None
        else:
            if self.is_shift == True:
                self.text_box.insert(tk.INSERT, button.capitalize())
            else:
                self.text_box.insert(tk.INSERT, button)
        # afer clicking anthing, a shift must gone
        self.is_shift = False
        self.shift_keyboard()

    def shift_keyboard(self):
        """Function to switch the letter case on the keyboard"""

        index = 0
        if self.is_shift == True:
            for button in self.buttons_list:
                button['text'] = self.shift_list[index]
                index += 1
        if self.is_shift == False:
            for button in self.buttons_list:
                button['text'] = self.keys_list[index]
                index += 1


# Start program
if __name__ == '__main__':
    root = tk.Tk()
    application = Main_Application(master=root)
    application.mainloop()
