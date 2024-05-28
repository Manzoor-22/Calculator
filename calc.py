import tkinter as tk
from currency_converter import CurrencyConverter

currencies = ['INR', 'USD', 'CAD', 'AUD', 'JPY', 'NZD', 'PHP']

class Converter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Currency Converter')
        self.window.geometry('200x180')
        

        self.from_var = tk.StringVar(self.window)
        self.from_var.set('EUR')
        self.from_menu = tk.OptionMenu(self.window, self.from_var, *currencies)
        self.from_menu.pack(pady=1)

        self.to_var = tk.StringVar(self.window)
        self.to_var.set('USD')
        self.to_menu = tk.OptionMenu(self.window, self.to_var, *currencies)
        self.to_menu.pack(pady=1)

        self.amount_label = tk.Label(self.window, text="Amount = ")
        self.amount_label.pack(pady=1)

        self.amount_entry = tk.Entry(self.window)
        self.amount_entry.pack(pady=1)

        self.convert_button = tk.Button(self.window, text='Convert', command=self.convert_currency)
        self.convert_button.pack(pady=1)

        self.result_label = tk.Label(self.window, text='')
        self.result_label.pack(pady=1)

        self.window.mainloop()

    def convert_currency(self):
        try:
            from_cur = self.from_var.get()
            to_cur = self.to_var.get()
            amount = float(self.amount_entry.get())

            rateobj = CurrencyConverter()

            rate = rateobj.convert(amount, from_cur, to_cur)
            converted = amount * rate

            self.result_label.config(text=rate)

        except ValueError:
            self.result_label.config(text='Please enter valid number')


if __name__ == '__main__':
    Converter()
