import tkinter as tk
from tkinter import ttk

class Interface(tk.Tk):
    def __init__ (self):
        '''
        Initialization of the interface
        '''
        super().__init__()
        self.geometry("500x500")
        self.title("Cosas chéveres!!!")
        self.columnconfigure(0, weight = 1)

        input = CodeInput(self)
        input.grid(row = 0, column = 0)

    def create_info_page(self, Data):
        self.data = DataPage(self, Data)
        self.data.grid(row = 1, column = 0)
        

class CodeInput(ttk.Frame):
    def __init__ (self, parent):
        '''
        Initialization of input template (button, entries and label)
        '''
        self.parent = parent
        super().__init__()
        self.label = ttk.Label(self, text = f"Enter ticker:\nEnter exchange code",
                               justify = "left")
        self.label.grid(row = 0, column = 0, sticky = "w", rowspan=2)
        #Creates a label asking for ticker and the exchange code

        self.ticker_entry = ttk.Entry(self)
        self.ticker_entry.grid(row = 0, column = 1, padx = 30)
        self.exchange_entry = ttk.Entry(self)
        self.exchange_entry.grid(row = 1, column = 1, padx = 30)
        #Creates two entry widgets: one for ticker and the other for the exchange code

        self.button = ttk.Button(self, text = "Search", command = self.get_codes)
        self.button.grid(row = 2, column = 0, columnspan = 2)
        #Creates button for searching

        self.missing_code = ttk.Label(text = "Please write both: Ticker and exchange")
        #Label that only appears if user doesn't write anything in the entries

    def get_codes(self):
        '''
        Getter for both entries.
        Creates a variable called codes which is a tuple with the following data:
        ("ticker", "exchange")
        both in uppercase
        it doesn't accept empty inputs
        '''
        self.missing_code.grid_remove()
        if self.ticker_entry.get() == "" or self.exchange_entry.get() == "":
            self.button.grid(row = 3, column = 0, columnspan = 2)
            self.missing_code.grid(row = 2, column = 0, columnspan = 2)
        else:
            codes = (self.ticker_entry.get().upper(),
                    self.exchange_entry.get().upper())
            
            Data = {'time': '13/06/2025 21:59:03', 'current_value': '$96.44', 'previous_close': '$99.04', 'day_range': '$96.44 - $98.55', 'year_range': '$72.68 - $101.74', 'market_cap': '20.32B USD', 'average_volume': '268.44K', 'primary_exchange': 'NYSE', 'ceo': 'Ian M. Craig García', 'founded': 'Oct 30, 1991', 'website': 'coca-colafemsa.com', 'employees': '118,683'}
            self.parent.create_info_page(Data)
            print(codes)

class DataPage(ttk.Frame):
    def __init__(self, parent, Data):
        super().__init__()
        self.data_label = ttk.Label(self, justify = "left", 
                                    text = f"""\n
                                    Time: {Data['time']}\n
                                    Current Value: {Data['current_value']}\n
                                    Previous close: {Data['previous_close']}\n
                                    Day Range: {Data['day_range']} \n
                                    Year Range: {Data['year_range']} \n
                                    Market cap: {Data['market_cap']} \n
                                    Average volume: {Data['average_volume']} \n
                                    Primary exchange: {Data['primary_exchange']} \n
                                    CEO: {Data['ceo']} \n
                                    Founded: {Data['founded']} \n
                                    Website: {Data['website']} \n
                                    Employees: {Data['employees']}""")
        self.data_label.grid(row = 0, column = 0, sticky = "w")

#{'time': '13/06/2025 21:59:03',
#'current_value': '$96.44',
#'previous_close': '$99.04',
#'day_range': '$96.44 - $98.55',
#'year_range': '$72.68 - $101.74',
#'market_cap': '20.32B USD',
#'average_volume': '268.44K',
#'primary_exchange': 'NYSE',
#'ceo': 'Ian M. Craig García',
#'founded': 'Oct 30, 1991',
#'website': 'coca-colafemsa.com',
#'employees': '118,683'}

def main():
    interface = Interface()
    interface.mainloop()

if __name__ == "__main__":
    main()