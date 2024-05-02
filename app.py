import random
import string
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Screen
        self.title('Password Generator')
        self.geometry('560x300')
        self.resizable(False, False)

        # Heading
        n = ttk.Style()
        n.configure('PG.Label', font=('Helvetica', 18, 'bold'))
        title = ttk.Label(self, text='PASSWORD GENERATOR', style='PG.Label')
        title.place(relx=0.24, rely=0.02)

        # Variables
        self.lowerLetters = list(string.ascii_lowercase)
        self.upperLetters = list(string.ascii_uppercase)
        self.numbers = list(string.digits)
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '?', '@']
        self.password = []

        # TKINTER Field Variables
        self.unum_letters = StringVar()
        self.lnum_letters = StringVar()
        self.num_digits = StringVar()
        self.num_symbols = StringVar()

        # Frames Content
        self.password_specification()

        # run
        self.mainloop()

    def password_specification(self):
        universal_font = ('Arial', 12)

        # UPPER LETTER ENTRY FIELD
        ttk.Label(self, text="How many uppercase letters would you like? ",
                  font=universal_font,
                  wraplength=260).place(relx=0.11, rely=0.18)
        upper_letter_entry = ttk.Entry(self,
                                       textvariable=self.unum_letters,
                                       width=15,
                                       justify=CENTER,
                                       font=universal_font)
        upper_letter_entry.focus_force()
        upper_letter_entry.place(relx=0.6, rely=0.18)

        # LOWER LETTER ENTRY FIELD
        ttk.Label(self, text="How many lowercase letters would you like? ",
                  font=universal_font,
                  wraplength=260).place(relx=0.11, rely=0.32)
        upper_letter_entry = ttk.Entry(self,
                                       textvariable=self.lnum_letters,
                                       width=15,
                                       justify=CENTER,
                                       font=universal_font)
        upper_letter_entry.focus_force()
        upper_letter_entry.place(relx=0.6, rely=0.32)

        # DIGITS ENTRY FIELD
        ttk.Label(self, text="How many numbers would you like? ",
                  font=universal_font,
                  wraplength=260).place(relx=0.11, rely=0.46)
        upper_letter_entry = ttk.Entry(self,
                                       textvariable=self.num_digits,
                                       width=15,
                                       justify=CENTER,
                                       font=universal_font)
        upper_letter_entry.focus_force()
        upper_letter_entry.place(relx=0.6, rely=0.46)

        # SYMBOL ENTRY FIELD
        ttk.Label(self, text="How many symbols would you like? ",
                  font=universal_font,
                  wraplength=260).place(relx=0.11, rely=0.6)
        upper_letter_entry = ttk.Entry(self,
                                       textvariable=self.num_symbols,
                                       width=15,
                                       justify=CENTER,
                                       font=universal_font)
        upper_letter_entry.focus_force()
        upper_letter_entry.place(relx=0.6, rely=0.6)

        s = ttk.Style()
        s.configure('my.TButton', font=('Arial', 12), background='#fff')
        btn_calculate = ttk.Button(self, text="Generate", style='my.TButton', cursor='hand2', width=45,
                                   command=self.generate_password)
        btn_calculate.place(relx=0.12, rely=0.78)

    def get_lowercase(self, num_letters):
        for _ in range(0, num_letters):
            self.password.append(random.choice(self.lowerLetters))

    def get_uppercase(self, num_letters):
        for _ in range(0, num_letters):
            self.password.append(random.choice(self.upperLetters))

    def get_digits(self, num_digits):
        for _ in range(0, num_digits):
            self.password.append(random.choice(self.numbers))

    def get_symbols(self, num_symbols):
        for _ in range(0, num_symbols):
            self.password.append(random.choice(self.symbols))

    def toplevel(self, final_password):
        pop = Toplevel(self)
        pop.title("Generated Password")
        pop.geometry('300x100')

        pop_label = ttk.Label(pop, text='Here is your desired password: ', font=('helvetica', 12), foreground='black')
        pop_label.pack(pady=10)

        generated_pw = ttk.Label(pop, text=final_password, background='lightblue', foreground='#000')
        generated_pw.config(anchor=CENTER)
        generated_pw.pack()

    def generate_password(self):
        try:
            upper_chars = int(self.unum_letters.get())
            low_chars = int(self.lnum_letters.get())
            digit_chars = int(self.num_digits.get())
            symbol_chars = int(self.num_symbols.get())

            print(f"{upper_chars}-{low_chars}-{digit_chars}-{symbol_chars}")

        except ValueError:
            messagebox.showerror('Error', 'Enter valid numbers')


app = App()
