import tkinter as tk
from tkinter import ttk
from resources.Docs import CreatePDF

class Interface(tk.Tk):
    def __init__ (self):
        '''
        Initialization of the interface
        '''
        super().__init__()
        self.geometry("700x500")
        self.title("Cosas chéveres!!!")
        self.columnconfigure((0, 1), weight = 1, minsize = 350)
        self.rowconfigure(0, weight = 1)

        input = CodeInput(self)
        input.grid(row = 0, column = 0, sticky = "nsew")

        compare = CodeInput(self)
        compare.grid(row = 0, column = 1, sticky = "nsew")

class CodeInput(ttk.Frame):
    def __init__ (self, parent):
        '''
        Initialization of input template (button, entries and label)
        Receives parent Interface and a bool to verify if it's the
        search or the compare button 
        '''
        self.parent = parent
        super().__init__()
        self.columnconfigure(0, weight = 1)
        self.label = ttk.Label(self, text = f"Enter ticker:\nEnter exchange code",
                               justify = "left")
        self.label.grid(row = 0, column = 0, sticky = "we", padx = 5, rowspan=2)
        #Creates a label asking for ticker and the exchange code

        self.ticker_entry = ttk.Entry(self)
        self.ticker_entry.grid(row = 0, column = 1, padx = 30)
        self.exchange_entry = ttk.Entry(self)
        self.exchange_entry.grid(row = 1, column = 1, padx = 30)
        #Creates two entry widgets: one for ticker and the other for the exchange code

        self.button = ttk.Button(self, text = "Search", command = self._process_data)
        self.button.grid(row = 2, column = 0, columnspan = 2)
        #Creates button for searching

        self.missing_code = ttk.Label(self, text = "Please write both: Ticker and exchange")
        #Label that only appears if user doesn't write anything in the entries

    def get_codes(self):
        '''
        Getter for both entries.
        Creates a variable called codes which is a tuple with the following data:
        ("ticker", "exchange")
        Both in uppercase.
        It doesn't accept empty inputs.
        '''
        self.missing_code.grid_remove()
        if self.ticker_entry.get() == "" or self.exchange_entry.get() == "":
            self.button.grid_remove()
            self.button.grid(row = 3, column = 0, columnspan = 2)
            self.missing_code.grid(row = 2, column = 0, columnspan = 2)
            return None
        else:
            codes = (self.ticker_entry.get().upper(),
                    self.exchange_entry.get().upper())
            print(codes)
            return codes
        
    def _process_data(self):
        codes = self.get_codes()
        #data = FUNCIÓN_DE_JORGE(codes)
        #Calls scraper function and gives the action codes
        data = {
        'stock_name': 'COCA-COLA FEMSA',
        'time': '13/06/2025 21:59:03',
        'current_value': '$96.44',
        'previous_close': '$99.04',
        'day_range': '$96.44 - $98.55',
        'year_range': '$72.68 - $101.74',
        'market_cap': '20.32B USD',
        'average_volume': '268.44K',
        'primary_exchange': 'NYSE',
        'ceo': 'Ian M. Craig García',
        'founded': 'Oct 30, 1991',
        'website': 'coca-colafemsa.com',
        'employees': '118,683'
        }
        if data == None:
            pass            #QUIEN RAISEA EL ERROR?????????????????????????????????????????????
        #Verifies the data received
        self.create_info_page(data)
        #Calls the function that shows the data received

    def create_info_page(self, data):
        '''
        Creates an instance of a DataPage object
        Showing the info of the action that the user looked for
        '''
        self.data_page = DataPage(self, data)

class DataPage(ttk.Frame):
    def __init__(self, parent, Data):
        '''
        Receives a dictionary of the data collected and shows it in the GUI
        '''
        super().__init__()
        self.grid(row = 4, column = parent.grid_info()["column"], sticky = "nsew")
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.data_label = ttk.Label(self, justify = "left",
                                    text = f"""\n
                                    Stock name: {Data['stock_name']}
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
        self.data_label.grid(row = 0, column = 0, sticky = "nsew")
        self.clear_button = ttk.Button(self, text = "Clear",
                                       command = self.clear_page)
        self.clear_button.grid(row = 1, column = 0, sticky = "e")
        self.pdf_create = CreatePDF(Data)
        self.pdf_button = ttk.Button(self, text = "Download PDF",
                                     command = self.pdf_create.to_pdf)
        self.pdf_button.grid(row = 1, column = 1, sticky = "nsew")

    def clear_page(self):
        for w in self.winfo_children():
            w.destroy()

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