import tkinter as tk
from tkinter import filedialog
from resources.Scrap import Scraper
import ttkbootstrap as ttk
big_title = ("Bookman Old Style", 42)
title = ("Bookman Old Style", 30)
subtitle = ("Courier New", 18, "bold")
body = ("Courier New", 11, "normal")
class Interface(tk.Tk):
    def __init__ (self):
        '''
        Initialization of the interface
        '''
        super().__init__()
        self.style = ttk.Style(theme = "darkly")
        self.geometry("900x600")
        self.title("Stock dealer :error:")
        self.rowconfigure((0, 1), weight = 1)
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
        '''
        super().__init__(parent, bootstyle = "primary", height = 100)
        self.parent = parent
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.grid_propagate(False)
        self.title = ttk.Label(self,
                               text = "Stock-Dealer :error:",
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
        self.parent.parent.main_page.grid_remove()
class MainPage(ttk.Frame):
    def __init__ (self, parent):
        '''
        Intitialization of main page
        '''
        super().__init__(parent)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0, 1, 2), weight = 1)
        # self.label = ttk.Label(self, text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        #                        font = body,
        #                        wraplength = 400)
        #self.label.grid(row = 0, column = 0, sticky = "nw")
        scraper = Scraper()
        data = scraper.winners_losers_actives()
        self.winners = TopsWidget(self, data.winners, "Winners")
        self.winners.grid(row = 0, column = 0, sticky = "nw")
        self.losers = TopsWidget(self, data.losers, "Losers")
        self.losers.grid(row = 1, column = 0, sticky = "nw")
        self.actives = TopsWidget(self, data.actives, "Actives")
        self.actives.grid(row = 2, column = 0, sticky = "nw", )
class TopsWidget(ttk.Frame):
    def __init__ (self, parent, data:Scraper, section:str):
        '''
        Initialization of Tops widgets (for showing top winners,
        top losers and most active)
        '''
        super().__init__(parent)
        self.rowconfigure(0, weight = 1)
        self.label = ttk.Label(self, text = f"{section}",
                               font = title)
        self.label.grid(row = 0, column = 0)
        if data == None or len(data) == 0:
            self.nodata = InfoNotObtained(self)
            self.nodata.grid(row = 1, column = 0, sticky = "nw")
        print(data)
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
class InfoNotObtained(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ttk.Label(self,
                               text = "There was a problem and we couldn't load the info",
                               bootstyle = "danger",
                               font = subtitle,
                               justify = "left")
        self.label.grid(row = 0, column = 0, sticky = "nw")
class StockMiniInfo(ttk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent,
                         bootstyle = "secondary",
                         width = 100,
                         height = 100)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.label_1 = ttk.Label(self, text = f"{data['ticker']}",
                                 font = subtitle,
                                 bootstyle = "inverse-secondary",
                                 justify = "center")
        self.label_1.grid(row = 0, column = 0, sticky = "nsew")
        self.label_2 = ttk.Label(self, text = f"{data['price']}(+{data['change_percentage']})",
                                 font = body, bootstyle = "success")
        self.label_2.grid(row = 1, column = 0, sticky = "nsew")
    # def save_file(self):
    #     save_file = filedialog.asksaveasfilename(
    #                 defaultextension = ".pdf",
    #                 title = "Save PDF",
    #                 initialfile = f"{self.data['stock_name']}.pdf")
    #     self.pdf_create.to_pdf(save_file)
def main():
    interface = Interface()
    interface.mainloop()
if __name__ == "__main__":
    main()
