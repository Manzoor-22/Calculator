import tkinter as tk
from forex_python import CurrencyRates

currencies = ['INR', 'USD', 'CAD', 'AUD', 'JPY', 'NZD', 'PHP']

class Converter:
    def __init__(self):
        self.root = tk.TK()
        self.root.title('Currency Converter')
        self.root.geometry('500x500')

        self.from_var = tk.StringVar(self.root)
        self.from_var.set('INR')
        self.from_menu = tk.OptionMenu(self.root, self.from_var)
