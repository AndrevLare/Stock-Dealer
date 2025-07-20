import tkinter as tk
from tkinter import filedialog
from resources.Scrap import Scraper


from types import SimpleNamespace   #LUEGO SE BORRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


import ttkbootstrap as ttk

big_title = ("Bookman Old Style", 42)
title = ("Bookman Old Style", 30)
subtitle = ("Courier New", 18, "bold")
body = ("Courier New", 14, "normal")

class Interface(tk.Tk):
    def __init__ (self):
        '''
        Initialization of the interface
        '''
        super().__init__()
        self.style = ttk.Style(theme = "darkly")
        self.minsize(width = 100, height = 700)
        self.geometry("1920x1080")
        self.title("Stock dealer 🐛")
        self.rowconfigure(1, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.heading = Heading(self)
        self.heading.grid(row = 0, column = 0, sticky = "wen")

        self.main_page = MainPage(self)
        self.main_page.grid(row = 1, column = 0, sticky = "new")




class Heading(ttk.Frame):
    def __init__ (self, parent):
        '''
        Initialization of frame Heading
        Contains: Title, Icon(?????????), Backgroung and Search instance
        Its present in every page
        Initialization of frame Heading
        Contains: Title, Icon(?????????), Backgroung and Search instance
        Its present in every page
        '''
        super().__init__(parent, bootstyle = "primary", height = 100)
        super().__init__(parent, bootstyle = "primary", height = 100)
        self.parent = parent
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.grid_propagate(False)
        self.title = ttk.Label(self,
                               text = "Stock-Dealer 🐛",
                               font = big_title,
                               bootstyle = "inverse-primary")
        self.title.grid(row = 0, column = 0, sticky = "w")
        self.search = Search(self)
        self.search.grid(row = 0, column = 1, sticky = "e")

class Search(ttk.Frame):
    def __init__(self, parent):
        '''
        Initialization of Search
        Contains: label, entry and button
        Button calls the create_stock_page() function
        '''
        super().__init__(parent, bootstyle = "primary")
        self.parent = parent
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.label = ttk.Label(self,
                               text = "Enter the ticker code you are looking for",
                               font = subtitle,
                               style = "inverse-primary",
                               wraplength = 350)
        self.label.grid(row = 0, column = 0, sticky = "ensw", rowspan = 2)
        self.input = ttk.Entry(self)
        self.input.grid(row = 0, column = 1, sticky = "nesw", padx = 5)
        self.button = ttk.Button(self, text = "Search",
                                 command = self.__create_stock_page,
                                 bootstyle = "secondary")
        self.button.grid(row = 1, column = 1, sticky = "nesw", padx = 5)

    def __create_stock_page(self):
        self.parent.parent.main_page.destroy()
        ticker = self.input.get()
        #data = FUNCION JORGEEEEEEEEEEEEEEEEEEE(ticker)
        data = None
        self.parent.parent.stock_page = StockPage(self.parent.parent, data)
        self.parent.parent.stock_page.grid(row = 1, column = 0, sticky = "nsew")

class MainPage(ttk.Frame):
    def __init__ (self, parent):
        '''
        Intitialization of main page
        '''
        super().__init__(parent)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0, 1, 2), weight = 1)
        scraper = Scraper()

        # data = scraper.winners_losers_actives()

        data = SimpleNamespace(winners = [{'ticker': 'CINGW', 'price': '0.099', 'change_amount': '0.0554', 'change_percentage': '127.0642%', 'volume': '415351'}, {'ticker': 'BZAIW', 'price': '0.849', 'change_amount': '0.439', 'change_percentage': '107.0732%', 'volume': '2915272'}, {'ticker': 'TELO', 'price': '2.28', 'change_amount': '1.07', 'change_percentage': '88.4298%', 'volume': '135814141'}, {'ticker': 'ZOOZW', 'price': '0.068', 'change_amount': '0.0287', 'change_percentage': '73.028%', 'volume': '1182'}, {'ticker': 'ABPWW', 'price': '0.0385', 'change_amount': '0.016', 'change_percentage': '71.1111%', 'volume': '40'}, {'ticker': 'PGYWW', 'price': '0.2905', 'change_amount': '0.1195', 'change_percentage': '69.883%', 'volume': '593682'}, {'ticker': 'IXHL', 'price': '0.61', 'change_amount': '0.2399', 'change_percentage': '64.8203%', 'volume': '472831869'}, {'ticker': 'SES+', 'price': '0.1932', 'change_amount': '0.0732', 'change_percentage': '61.0%', 'volume': '81354'}, {'ticker': 'CYCC', 'price': '13.07', 'change_amount': '4.84', 'change_percentage': '58.8092%', 'volume': '22187995'}, {'ticker': 'BZAI', 'price': '4.81', 'change_amount': '1.78', 'change_percentage': '58.7459%', 'volume': '73057516'}, {'ticker': 'LSBPW', 'price': '0.0399', 'change_amount': '0.0143', 'change_percentage': '55.8594%', 'volume': '400'}, {'ticker': 'BDMDW', 'price': '0.0998', 'change_amount': '0.0348', 'change_percentage': '53.5385%', 'volume': '15314'}, {'ticker': 'XPON', 'price': '1.58', 'change_amount': '0.54', 'change_percentage': '51.9231%', 'volume': '53819112'}, {'ticker': 'CDTTW', 'price': '0.013', 'change_amount': '0.0044', 'change_percentage': '51.1628%', 'volume': '22461'}, {'ticker': 'LMFA', 'price': '3.23', 'change_amount': '1.01', 'change_percentage': '45.4955%', 'volume': '16964388'}, {'ticker': 'STEM', 'price': '13.47', 'change_amount': '4.2', 'change_percentage': '45.3074%', 'volume': '3737223'}, {'ticker': 'JFBRW', 'price': '0.0253', 'change_amount': '0.0076', 'change_percentage': '42.9379%', 'volume': '2500'}, {'ticker': 'EUDAW', 'price': '0.1297', 'change_amount': '0.0386', 'change_percentage': '42.371%', 'volume': '1602'}, {'ticker': 'CMBM', 'price': '0.9567', 'change_amount': '0.2817', 'change_percentage': '41.7333%', 'volume': '2414335'}, {'ticker': 'CAPTW', 'price': '0.06', 'change_amount': '0.0172', 'change_percentage': '40.1869%', 'volume': '628'}],
                               losers = [{'ticker': 'PTNM', 'price': '2.13', 'change_amount': '-4.48', 'change_percentage': '-67.7761%', 'volume': '4560831'}, {'ticker': 'YHC', 'price': '2.38', 'change_amount': '-4.19', 'change_percentage': '-63.7747%', 'volume': '9726691'}, {'ticker': 'SVREW', 'price': '0.023', 'change_amount': '-0.0274', 'change_percentage': '-54.3651%', 'volume': '13'}, {'ticker': 'AP+', 'price': '0.0113', 'change_amount': '-0.0111', 'change_percentage': '-49.5536%', 'volume': '9631'}, {'ticker': 'PETWW', 'price': '0.0045', 'change_amount': '-0.0038', 'change_percentage': '-45.7831%', 'volume': '956416'}, {'ticker': 'MJID', 'price': '3.3', 'change_amount': '-2.7', 'change_percentage': '-45.0%', 'volume': '4701520'}, {'ticker': 'KMRK', 'price': '2.45', 'change_amount': '-2.0', 'change_percentage': '-44.9438%', 'volume': '12818421'}, {'ticker': 'RANGR', 'price': '0.1201', 'change_amount': '-0.0899', 'change_percentage': '-42.8095%', 'volume': '830'}, {'ticker': 'RELIW', 'price': '0.0276', 'change_amount': '-0.0206', 'change_percentage': '-42.7386%', 'volume': '550'}, {'ticker': 'SVIIR', 'price': '0.0879', 'change_amount': '-0.062', 'change_percentage': '-41.3609%', 'volume': '5201'}, {'ticker': 'NAK', 'price': '1.015', 'change_amount': '-0.615', 'change_percentage': '-37.7301%', 'volume': '127165978'}, {'ticker': 'COLAR', 'price': '0.143', 'change_amount': '-0.086', 'change_percentage': '-37.5546%', 'volume': '100'}, {'ticker': 'ECXWW', 'price': '0.0511', 'change_amount': '-0.0289', 'change_percentage': '-36.125%', 'volume': '107694'}, {'ticker': 'SRPT', 'price': '14.075', 'change_amount': '-7.895', 'change_percentage': '-35.9354%', 'volume': '76206157'}, {'ticker': 'SBFMW', 'price': '0.18', 'change_amount': '-0.09', 'change_percentage': '-33.3333%', 'volume': '2619'}, {'ticker': 'BSLKW', 'price': '0.0335', 'change_amount': '-0.0165', 'change_percentage': '-33.0%', 'volume': '87569'}, {'ticker': 'CLSD', 'price': '0.409', 'change_amount': '-0.1928', 'change_percentage': '-32.0372%', 'volume': '3588143'}, {'ticker': 'BZFDW', 'price': '0.072', 'change_amount': '-0.0331', 'change_percentage': '-31.4938%', 'volume': '25688'}, {'ticker': 'ECDAW', 'price': '0.0175', 'change_amount': '-0.0075', 'change_percentage': '-30.0%', 'volume': '20000'}, {'ticker': 'ACONW', 'price': '0.0251', 'change_amount': '-0.0098', 'change_percentage': '-28.0802%', 'volume': '5750'}],
                               actives = [{'ticker': 'OPEN', 'price': '2.25', 'change_amount': '0.6', 'change_percentage': '88.8888%', 'volume': '546523618'}, {'ticker': 'IXHL', 'price': '0.61', 'change_amount': '0.2399', 'change_percentage': '64.8203%', 'volume': '472831869'}, {'ticker': 'BTOG', 'price': '0.78', 'change_amount': '0.149', 'change_percentage': '23.6133%', 'volume': '357879119'}, {'ticker': 'LCID', 'price': '3.04', 'change_amount': '-0.08', 'change_percentage': '-2.5641%', 'volume': '292312797'}, {'ticker': 'SOXS', 'price': '7.16', 'change_amount': '0.01', 'change_percentage': '0.1399%', 'volume': '199115022'}, {'ticker': 'QS', 'price': '14.63', 'change_amount': '1.03', 'change_percentage': '7.5735%', 'volume': '147003535'}, {'ticker': 'NVDA', 'price': '172.41', 'change_amount': '-0.59', 'change_percentage': '-0.341%', 'volume': '145183487'}, {'ticker': 'UAVS', 'price': '2.03', 'change_amount': '0.56', 'change_percentage': '38.0952%', 'volume': '144699586'}, {'ticker': 'TSLL', 'price': '12.4', 'change_amount': '0.73', 'change_percentage': '6.2554%', 'volume': '140290470'}, {'ticker': 'TELO', 'price': '2.28', 'change_amount': '1.07', 'change_percentage': '88.4298%', 'volume': '135814141'}, {'ticker': 'NAK', 'price': '1.015', 'change_amount' : '4848%', 'volume': '101602827'}, {'ticker': 'GVH', 'price': '0.0351', 'change_amount': '-0.0119', 'change_percentage': '-25.3191%', 'volume': '98235867'}, {'ticker': 'TSLZ', 'price': '1.47', 'change_amount': '-0.105', 'change_percentage': '-6.6667%', 'volume': '94157981'}, {'ticker': 'TSLA', 'price': '329.65', 'change_amount': '10.24', 'change_percentage': '3.2059%', 'volume': '93626667'}, {'ticker': 'NU', 'price': '13.025', 'change_amount': '-0.965', 'change_percentage': '-6.8978%', 'volume': '91304086'}, {'ticker': 'SBET', 'price': '28.98', 'change_amount': '-7.42', 'change_percentage': '-20.3846%', 'volume': '84788935'}])

        self.winners = TopsWidget(self, data.winners, "Winners")
        self.winners.grid(row = 0, column = 0, sticky = "nw", pady = 10)
        
        self.losers = TopsWidget(self, data.losers, "Losers")
        self.losers.grid(row = 1, column = 0, sticky = "nw", pady = 10)
        
        self.actives = TopsWidget(self, data.actives, "Actives")
        self.actives.grid(row = 2, column = 0, sticky = "nw", pady = 10)

class TopsWidget(ttk.Frame):
    def __init__ (self, parent, data:Scraper, section:str):
        '''
        Initialization of Tops widgets (for showing top winners,
        top losers and most active)
        '''
        super().__init__(parent)
        self.label = ttk.Label(self, text = f"{section}",
                               font = title,
                               justify = "left")
        self.label.grid(row = 0, column = 0, padx = 10, pady = 5, columnspan = 5, sticky = "w")

        self.section = section

        self.w_1 = None
        self.w_2 = None
        self.w_3 = None
        self.w_4 = None
        self.w_5 = None
        self.widget = [self.w_1, self.w_2, self.w_3, self.w_4, self.w_5]
        for n, stock  in enumerate(data):
            self.columnconfigure(n, weight=1)
            self.widget[n] = StockMiniInfo(self, stock)
            self.widget[n].grid(row = 1, column = n, padx = 10, sticky = "nsew")
            if n == 4:
                break

# class InfoNotObtained(ttk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.label = ttk.Label(self,
#                                text = "There was a problem and we couldn't load the info",
#                                bootstyle = "danger",
#                                font = subtitle,
#                                justify = "left")
#         self.label.grid(row = 0, column = 0, sticky = "nw")

class StockMiniInfo(ttk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent,
                         bootstyle = "secondary",
                         width = 140,
                         height = 80)
        
        self.grid_propagate(False)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0,1), weight = 1)

        self.label_1 = ttk.Label(self, text = f"{data['ticker']}",
                                 font = subtitle,
                                 bootstyle = "inverse-secondary",
                                 justify = "center",
                                 anchor = "center")
        self.label_1.grid(row = 0, column = 0, sticky = "nsew")

        section = parent.section
        if section == "Winners":
            style = "success"
        elif section == "Losers":
            style = "danger"
        else:
            style = "info"

        self.label_2 = ttk.Label(self,
                                 text = f"{data['price']}\n({data['change_percentage']})",
                                 font = body,
                                 bootstyle = style,
                                 justify = "center",
                                 anchor = "center")
        self.label_2.grid(row = 1, column = 0, sticky = "nsew", )

    # def save_file(self):
    #     save_file = filedialog.asksaveasfilename(
    #                 defaultextension = ".pdf",
    #                 title = "Save PDF",
    #                 initialfile = f"{self.data['stock_name']}.pdf")
    #     self.pdf_create.to_pdf(save_file)

class StockPage(ttk.Frame):
    def __init__ (self, parent, data):
        super().__init__(parent)
        self.columnconfigure((0,1), weight = 1)
        self.title = ttk.Label(self, text = f"*Stock Name",
                               font = title,
                               bootstyle = "primary")
        self.title.grid(row = 0, column = 0, sticky = "nwe", pady = 5, padx = 5)
        self.description = ttk.Label(self, text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                                     font = body,
                                     wraplength = 980,
                                     justify = "left")
        self.description.grid(row = 1, column = 0, columnspan = 2, sticky = "new", padx = 10, pady = 5)

        # stock_data = data
        stock_data = {"titulo1":"hola", "titulo2":"soy", "titulo3":"Falcao", "Jorge":"Te", "Necesitamos":":("}
        self.stock_info = StockInfo(self, stock_data)
        self.stock_info.grid(row = 2, column = 1, sticky = "new")


class StockInfo(ttk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0, 1), weight = 1)
        titles_string = ""
        values_string = ""
        for (title, value) in data.items():
            titles_string += f"{title}: \n"
            values_string += f"{value}\n"
        self.titles = ttk.Label(self, text = titles_string, font = subtitle)
        self.titles.grid(row = 0, column = 0, sticky = "nsew")
        self.values = ttk.Label(self, text = values_string, font = body)
        self.values.grid(row = 0, column = 1, sticky = "nsew")


def main():
    interface = Interface()
    interface.mainloop()
if __name__ == "__main__":
    main()
