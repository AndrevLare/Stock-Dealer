import tkinter as tk
import os
import shutil
import webbrowser
import pathlib
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from tkinter import filedialog
from resources.Scrap import Scraper
from resources.DOCS.Docs import PDF
from resources.DOCS.ImageGenerator import Grapher

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
        self.main_page.grid(row = 1, column = 0, sticky = "nsew")

    def to_main_page(self):
        '''
        Removes the current stock_page and goes back to the main page,
        restores the title
        '''
        self.stock_page.destroy()
        self.heading.title.config(text = "Stock-Dealer 🐛")
        self.main_page = MainPage(self)
        self.main_page.grid(row = 1, column = 0, sticky = "nsew")

    def to_stock_page(self, ticker):
        '''
        Removes the main_page, changes the heading title and creates
        the page with all  the info of the stock the user looked for
        '''
        self.main_page.destroy()
        self.heading.title.config(text = "🢀 Stock-Dealer 🐛")

        scraper = Scraper()
        info = scraper.company_info(ticker)
        graph1d = scraper.get_info_and_1D_graph(ticker)
        graph1m = scraper.get_1M_graph(ticker)
        graph1y = scraper.get_1Y_graph(ticker)
        sentiment = scraper.get_ticker_sentiment(ticker)
        data = {"Price" : graph1d.current_value,
                "Info" : info,
                "Graph1D" : graph1d,
                "Graph1M" : graph1m,
                "Graph1Y" : graph1y,
                "Sentiment" : sentiment}

        self.stock_page = StockPage(self, data)
        self.stock_page.grid(row = 1, column = 0, sticky = "nsew")

class Heading(ttk.Frame):
    def __init__ (self, parent):
        '''
        Initialization of frame Heading
        Contains: Title, Backgroung and Search instance
        Its present in every page
        '''
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
        self.title.bind("<Button-1>", lambda e: self.parent.to_main_page())
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
        '''
        Gets the input from the entry box, and calls the
        function that creates the stock_page in the Interface
        '''
        ticker = self.input.get()
        self.parent.parent.to_stock_page(ticker)

class MainPage(ttk.Frame):
    def __init__ (self, parent):
        '''
        Intitialization of main page
        '''
        super().__init__(parent)
        self.parent = parent
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0, 1, 2), weight = 1)
        scraper = Scraper()

        data = scraper.winners_losers_actives()

        # data = SimpleNamespace(winners = [{'ticker': 'CINGW', 'price': '0.099', 'change_amount': '0.0554', 'change_percentage': '127.0642%', 'volume': '415351'}, {'ticker': 'BZAIW', 'price': '0.849', 'change_amount': '0.439', 'change_percentage': '107.0732%', 'volume': '2915272'}, {'ticker': 'TELO', 'price': '2.28', 'change_amount': '1.07', 'change_percentage': '88.4298%', 'volume': '135814141'}, {'ticker': 'ZOOZW', 'price': '0.068', 'change_amount': '0.0287', 'change_percentage': '73.028%', 'volume': '1182'}, {'ticker': 'ABPWW', 'price': '0.0385', 'change_amount': '0.016', 'change_percentage': '71.1111%', 'volume': '40'}, {'ticker': 'PGYWW', 'price': '0.2905', 'change_amount': '0.1195', 'change_percentage': '69.883%', 'volume': '593682'}, {'ticker': 'IXHL', 'price': '0.61', 'change_amount': '0.2399', 'change_percentage': '64.8203%', 'volume': '472831869'}, {'ticker': 'SES+', 'price': '0.1932', 'change_amount': '0.0732', 'change_percentage': '61.0%', 'volume': '81354'}, {'ticker': 'CYCC', 'price': '13.07', 'change_amount': '4.84', 'change_percentage': '58.8092%', 'volume': '22187995'}, {'ticker': 'BZAI', 'price': '4.81', 'change_amount': '1.78', 'change_percentage': '58.7459%', 'volume': '73057516'}, {'ticker': 'LSBPW', 'price': '0.0399', 'change_amount': '0.0143', 'change_percentage': '55.8594%', 'volume': '400'}, {'ticker': 'BDMDW', 'price': '0.0998', 'change_amount': '0.0348', 'change_percentage': '53.5385%', 'volume': '15314'}, {'ticker': 'XPON', 'price': '1.58', 'change_amount': '0.54', 'change_percentage': '51.9231%', 'volume': '53819112'}, {'ticker': 'CDTTW', 'price': '0.013', 'change_amount': '0.0044', 'change_percentage': '51.1628%', 'volume': '22461'}, {'ticker': 'LMFA', 'price': '3.23', 'change_amount': '1.01', 'change_percentage': '45.4955%', 'volume': '16964388'}, {'ticker': 'STEM', 'price': '13.47', 'change_amount': '4.2', 'change_percentage': '45.3074%', 'volume': '3737223'}, {'ticker': 'JFBRW', 'price': '0.0253', 'change_amount': '0.0076', 'change_percentage': '42.9379%', 'volume': '2500'}, {'ticker': 'EUDAW', 'price': '0.1297', 'change_amount': '0.0386', 'change_percentage': '42.371%', 'volume': '1602'}, {'ticker': 'CMBM', 'price': '0.9567', 'change_amount': '0.2817', 'change_percentage': '41.7333%', 'volume': '2414335'}, {'ticker': 'CAPTW', 'price': '0.06', 'change_amount': '0.0172', 'change_percentage': '40.1869%', 'volume': '628'}],
        #                        losers = [{'ticker': 'PTNM', 'price': '2.13', 'change_amount': '-4.48', 'change_percentage': '-67.7761%', 'volume': '4560831'}, {'ticker': 'YHC', 'price': '2.38', 'change_amount': '-4.19', 'change_percentage': '-63.7747%', 'volume': '9726691'}, {'ticker': 'SVREW', 'price': '0.023', 'change_amount': '-0.0274', 'change_percentage': '-54.3651%', 'volume': '13'}, {'ticker': 'AP+', 'price': '0.0113', 'change_amount': '-0.0111', 'change_percentage': '-49.5536%', 'volume': '9631'}, {'ticker': 'PETWW', 'price': '0.0045', 'change_amount': '-0.0038', 'change_percentage': '-45.7831%', 'volume': '956416'}, {'ticker': 'MJID', 'price': '3.3', 'change_amount': '-2.7', 'change_percentage': '-45.0%', 'volume': '4701520'}, {'ticker': 'KMRK', 'price': '2.45', 'change_amount': '-2.0', 'change_percentage': '-44.9438%', 'volume': '12818421'}, {'ticker': 'RANGR', 'price': '0.1201', 'change_amount': '-0.0899', 'change_percentage': '-42.8095%', 'volume': '830'}, {'ticker': 'RELIW', 'price': '0.0276', 'change_amount': '-0.0206', 'change_percentage': '-42.7386%', 'volume': '550'}, {'ticker': 'SVIIR', 'price': '0.0879', 'change_amount': '-0.062', 'change_percentage': '-41.3609%', 'volume': '5201'}, {'ticker': 'NAK', 'price': '1.015', 'change_amount': '-0.615', 'change_percentage': '-37.7301%', 'volume': '127165978'}, {'ticker': 'COLAR', 'price': '0.143', 'change_amount': '-0.086', 'change_percentage': '-37.5546%', 'volume': '100'}, {'ticker': 'ECXWW', 'price': '0.0511', 'change_amount': '-0.0289', 'change_percentage': '-36.125%', 'volume': '107694'}, {'ticker': 'SRPT', 'price': '14.075', 'change_amount': '-7.895', 'change_percentage': '-35.9354%', 'volume': '76206157'}, {'ticker': 'SBFMW', 'price': '0.18', 'change_amount': '-0.09', 'change_percentage': '-33.3333%', 'volume': '2619'}, {'ticker': 'BSLKW', 'price': '0.0335', 'change_amount': '-0.0165', 'change_percentage': '-33.0%', 'volume': '87569'}, {'ticker': 'CLSD', 'price': '0.409', 'change_amount': '-0.1928', 'change_percentage': '-32.0372%', 'volume': '3588143'}, {'ticker': 'BZFDW', 'price': '0.072', 'change_amount': '-0.0331', 'change_percentage': '-31.4938%', 'volume': '25688'}, {'ticker': 'ECDAW', 'price': '0.0175', 'change_amount': '-0.0075', 'change_percentage': '-30.0%', 'volume': '20000'}, {'ticker': 'ACONW', 'price': '0.0251', 'change_amount': '-0.0098', 'change_percentage': '-28.0802%', 'volume': '5750'}],
        #                        actives = [{'ticker': 'OPEN', 'price': '2.25', 'change_amount': '0.6', 'change_percentage': '88.8888%', 'volume': '546523618'}, {'ticker': 'IXHL', 'price': '0.61', 'change_amount': '0.2399', 'change_percentage': '64.8203%', 'volume': '472831869'}, {'ticker': 'BTOG', 'price': '0.78', 'change_amount': '0.149', 'change_percentage': '23.6133%', 'volume': '357879119'}, {'ticker': 'LCID', 'price': '3.04', 'change_amount': '-0.08', 'change_percentage': '-2.5641%', 'volume': '292312797'}, {'ticker': 'SOXS', 'price': '7.16', 'change_amount': '0.01', 'change_percentage': '0.1399%', 'volume': '199115022'}, {'ticker': 'QS', 'price': '14.63', 'change_amount': '1.03', 'change_percentage': '7.5735%', 'volume': '147003535'}, {'ticker': 'NVDA', 'price': '172.41', 'change_amount': '-0.59', 'change_percentage': '-0.341%', 'volume': '145183487'}, {'ticker': 'UAVS', 'price': '2.03', 'change_amount': '0.56', 'change_percentage': '38.0952%', 'volume': '144699586'}, {'ticker': 'TSLL', 'price': '12.4', 'change_amount': '0.73', 'change_percentage': '6.2554%', 'volume': '140290470'}, {'ticker': 'TELO', 'price': '2.28', 'change_amount': '1.07', 'change_percentage': '88.4298%', 'volume': '135814141'}, {'ticker': 'NAK', 'price': '1.015', 'change_amount' : '4848%', 'volume': '101602827'}, {'ticker': 'GVH', 'price': '0.0351', 'change_amount': '-0.0119', 'change_percentage': '-25.3191%', 'volume': '98235867'}, {'ticker': 'TSLZ', 'price': '1.47', 'change_amount': '-0.105', 'change_percentage': '-6.6667%', 'volume': '94157981'}, {'ticker': 'TSLA', 'price': '329.65', 'change_amount': '10.24', 'change_percentage': '3.2059%', 'volume': '93626667'}, {'ticker': 'NU', 'price': '13.025', 'change_amount': '-0.965', 'change_percentage': '-6.8978%', 'volume': '91304086'}, {'ticker': 'SBET', 'price': '28.98', 'change_amount': '-7.42', 'change_percentage': '-20.3846%', 'volume': '84788935'}])

        self.winners = TopsWidget(self, data.winners, "Winners")
        self.winners.grid(row = 0, column = 0, sticky = "nw", pady = 10)
        
        self.losers = TopsWidget(self, data.losers, "Losers")
        self.losers.grid(row = 1, column = 0, sticky = "nw", pady = 10)
        
        self.actives = TopsWidget(self, data.actives, "Actives")
        self.actives.grid(row = 2, column = 0, sticky = "nw", pady = 10)

class TopsWidget(ttk.Frame):
    def __init__ (self, parent, data:Scraper, section:str):

        print(data)

        '''
        Initialization of Tops widgets (for showing top winners,
        top losers and most active)
        '''
        super().__init__(parent)
        self.parent = parent

        self.label = ttk.Label(self, text = f"{section}",
                               font = title,
                               justify = "left")
        self.label.grid(row = 0, column = 0, padx = 10, pady = 5, columnspan = 5, sticky = "w")

        self.section = section

        if not data:
            self.noinfo = InfoNotObtained(self)
            self.noinfo.grid(row=1, column=0, columnspan=5, padx=10, sticky="nsew")
        else:
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
                               justify = "center")
        self.label.grid(row = 0, column = 0, sticky = "nw")

class StockMiniInfo(ttk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent,
                         bootstyle = "secondary",
                         width = 140,
                         height = 80)

        self.grid_propagate(False)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0,1), weight = 1)
        self.parent = parent


        self.label_1 = ttk.Label(self, text = f"{data['ticker']}",
                                font = subtitle,
                                bootstyle = "inverse-secondary",
                                justify = "center",
                                anchor = "center")
        self.label_1.grid(row = 0, column = 0, sticky = "nsew")
        self.label_1.bind("<Button-1>", lambda e: self.__create_stock_page(data['ticker']))

        section = parent.section
        if section == "Winners":
            style = "success"
        elif section == "Losers":
            style = "danger"
        else:
            style = "info"

        self.label_2 = ttk.Label(self,
                                text = f"${data['price']}\n({data['change_percentage']})",
                                font = body,
                                bootstyle = style,
                                justify = "center",
                                anchor = "center")
        self.label_2.grid(row = 1, column = 0, sticky = "nsew", )

    def __create_stock_page(self, ticker):
        self.parent.parent.parent.to_stock_page(ticker)



class StockPage(ttk.Notebook):
    def __init__(self, parent, data):
        super().__init__(parent)

        # data = {"Price" : 13.69, "Info" : SimpleNamespace(Symbol = "IBM", AssetType = "Common Stock", Name = "International Business Machines", Description = "International Business Machines Corporation (IBM) is an American multinational technology company headquartered in Armonk, New York, with operations in over 170 countries. The company began in 1911, founded in Endicott, New York, as the Computing-Tabulating-Recording Company (CTR) and was renamed International Business Machines in 1924. IBM is incorporated in New York. IBM produces and sells computer hardware, middleware and software, and provides hosting and consulting services in areas ranging from mainframe computers to nanotechnology. IBM is also a major research organization, holding the record for most annual U.S. patents generated by a business (as of 2020) for 28 consecutive years. Inventions by IBM include the automated teller machine (ATM), the floppy disk, the hard disk drive, the magnetic stripe card, the relational database, the SQL programming language, the UPC barcode, and dynamic random-access memory (DRAM). The IBM mainframe, exemplified by the System/360, was the dominant computing platform during the 1960s and 1970s.", CIK = "51143", Exchange = "NYSE", Currency = "USD", Country = "USA", Sector = "TECHNOLOGY", Industry = "COMPUTER & OFFICE EQUIPMENT", Address = "1 NEW ORCHARD ROAD, ARMONK, NY, US", OfficialSite = "https://www.ibm.com", FiscalYearEnd = "December", LatestQuarter = "2025-03-31", MarketCapitalization = "271356035000", EBITDA = "13950000000", PERatio = "49.99", PEGRatio = "2.165", BookValue = "28.92", DividendPerShare = "6.68", DividendYield = "0.0228", EPS = "5.84", RevenuePerShareTTM = "67.97", ProfitMargin = "0.0871", OperatingMarginTTM = "0.124", ReturnOnAssetsTTM = "0.0447", ReturnOnEquityTTM = "0.218", RevenueTTM = "62832001000", GrossProfitTTM = "35840000000", DilutedEPSTTM = "5.84", QuarterlyEarningsGrowthYOY = "-0.349", QuarterlyRevenueGrowthYOY = "0.005", AnalystTargetPrice = "258.02", AnalystRatingStrongBuy = "2", AnalystRatingBuy = "8", AnalystRatingHold = "9", AnalystRatingSell = "2", AnalystRatingStrongSell = "1", TrailingPE = "49.99", ForwardPE = "26.6", PriceToSalesRatioTTM = "4.319", PriceToBookRatio = "10.1", EVToRevenue = "5.1", EVToEBITDA = "26.01", Beta = "0.652", SharesOutstanding = "929397000", SharesFloat = "927361000", PercentInsiders = "0.119", PercentInstitutions = "65.274", DividendDate = "2025-06-10", ExDividendDate = "2025-05-09"), "Graph1D" : SimpleNamespace(last_refreshed='2025-07-18 19:45:00', current_value='231.1000', values=[('231.1000', '2025-07-18 19:45:00'), ('231.1000', '2025-07-18 19:30:00'), ('231.0000', '2025-07-18 19:15:00'), ('231.0000', '2025-07-18 19:00:00'), ('230.6600', '2025-07-18 18:45:00'), ('230.6600', '2025-07-18 18:30:00'), ('231.0000', '2025-07-18 18:15:00'), ('230.6600', '2025-07-18 18:00:00'), ('229.7200', '2025-07-18 17:45:00'), ('229.7200', '2025-07-18 17:30:00'), ('230.9900', '2025-07-18 17:15:00'), ('231.0000', '2025-07-18 17:00:00'), ('230.9900', '2025-07-18 16:45:00'), ('231.1800', '2025-07-18 16:30:00'), ('231.1800', '2025-07-18 16:15:00'), ('231.4900', '2025-07-18 16:00:00'), ('231.2000', '2025-07-18 15:45:00'), ('229.7050', '2025-07-18 15:30:00'), ('229.4150', '2025-07-18 15:15:00'), ('228.9900', '2025-07-18 15:00:00'), ('229.2950', '2025-07-18 14:45:00'), ('229.9200', '2025-07-18 14:30:00'), ('230.2000', '2025-07-18 14:15:00'), ('230.1000', '2025-07-18 14:00:00'), ('229.5975', '2025-07-18 13:45:00'), ('229.8950', '2025-07-18 13:30:00'), ('229.6800', '2025-07-18 13:15:00'), ('228.6200', '2025-07-18 13:00:00'), ('228.7100', '2025-07-18 12:45:00'), ('228.4900', '2025-07-18 12:30:00'), ('229.4000', '2025-07-18 12:15:00'), ('230.1250', '2025-07-18 12:00:00'), ('230.7200', '2025-07-18 11:45:00'), ('231.5200', '2025-07-18 11:30:00'), ('230.7400', '2025-07-18 11:15:00'), ('230.1650', '2025-07-18 11:00:00'), ('230.1400', '2025-07-18 10:45:00'), ('230.7500', '2025-07-18 10:30:00'), ('229.3900', '2025-07-18 10:15:00'), ('230.4400', '2025-07-18 10:00:00'), ('231.5100', '2025-07-18 09:45:00'), ('232.7650', '2025-07-18 09:30:00'), ('234.4700', '2025-07-18 09:15:00'), ('234.1800', '2025-07-18 09:00:00'), ('234.2000', '2025-07-18 08:45:00'), ('233.5500', '2025-07-18 08:30:00'), ('234.2000', '2025-07-18 08:15:00'), ('234.2000', '2025-07-18 08:00:00'), ('233.9200', '2025-07-18 07:45:00'), ('234.2400', '2025-07-18 07:30:00'), ('234.2400', '2025-07-18 07:00:00'), ('234.9900', '2025-07-18 06:45:00'), ('234.0000', '2025-07-18 06:30:00'), ('234.2400', '2025-07-18 06:00:00'), ('234.5400', '2025-07-18 05:30:00'), ('234.9900', '2025-07-18 05:15:00'), ('234.9900', '2025-07-18 04:45:00'), ('234.5400', '2025-07-18 04:30:00'), ('234.9900', '2025-07-18 04:15:00'), ('235.0000', '2025-07-18 04:00:00'), ('233.9100', '2025-07-17 19:45:00'), ('233.9200', '2025-07-17 19:30:00'), ('233.9000', '2025-07-17 19:15:00'), ('233.8000', '2025-07-17 19:00:00'), ('233.9100', '2025-07-17 18:45:00'), ('233.2800', '2025-07-17 18:30:00'), ('233.1501', '2025-07-17 18:15:00'), ('233.7000', '2025-07-17 18:00:00'), ('233.7500', '2025-07-17 17:45:00'), ('233.9200', '2025-07-17 17:30:00'), ('233.9200', '2025-07-17 17:15:00'), ('233.9200', '2025-07-17 17:00:00'), ('233.9000', '2025-07-17 16:45:00'), ('232.9000', '2025-07-17 16:30:00'), ('232.9000', '2025-07-17 16:15:00'), ('233.9200', '2025-07-17 16:00:00'), ('233.9800', '2025-07-17 15:45:00'), ('234.0450', '2025-07-17 15:30:00'), ('234.1550', '2025-07-17 15:15:00'), ('233.5900', '2025-07-17 15:00:00'), ('233.6500', '2025-07-17 14:45:00'), ('233.5100', '2025-07-17 14:30:00'), ('232.8900', '2025-07-17 14:15:00'), ('232.3800', '2025-07-17 14:00:00'), ('232.5300', '2025-07-17 13:45:00'), ('232.7200', '2025-07-17 13:30:00'), ('232.0650', '2025-07-17 13:15:00'), ('232.1550', '2025-07-17 13:00:00'), ('232.4700', '2025-07-17 12:45:00'), ('231.2800', '2025-07-17 12:30:00'), ('231.5300', '2025-07-17 12:15:00'), ('233.2500', '2025-07-17 12:00:00'), ('233.9400', '2025-07-17 11:45:00'), ('234.5600', '2025-07-17 11:30:00'), ('234.7700', '2025-07-17 11:15:00'), ('235.6200', '2025-07-17 11:00:00')]), "Sentiment" : 0.3}

        self.price = data["Price"]
        self.sentiment = data['Sentiment']

        self.add(InfoTab(self, data['Info']), text = "Overview")

        self.add(GraphTab(self, data['Graph1D'], data['Info'], "1-Day Graph"), text = "1-Day Graph")

        self.add(GraphTab(self, data['Graph1M'], data['Info'], "1-Month Graph"), text = "1-Month Graph")

        self.add(GraphTab(self, data['Graph1Y'], data['Info'], "1-Year Graph"), text = "1-Year Graph")

        grapher1 = Grapher(data['Graph1D'])
        day_path = grapher1.plot(filename="day_graph.png")
        grapher2 = Grapher(data['Graph1M'])
        month_path = grapher2.plot(filename="month_graph.png")
        grapher3 = Grapher(data['Graph1Y'])
        year_path = grapher3.plot(filename="year_graph.png")
    

        self.info = {
            "SENTIMENT_VALUE": data['Sentiment'],
            "EXCHANGE": data['Info'].Exchange,
            "NAME": data['Info'].Name,
            "TICKER": data['Info'].Symbol,
            "VALUE": self.price,
            "DAY_GRAPH":day_path,
            "MONTH_GRAPH":month_path,
            "YEAR_GRAPH":year_path,
            "COMPANY_DESCRIPTION": data['Info'].Description,
            "ASSET_TYPE": data['Info'].AssetType,
            "COUNTRY": data['Info'].Country,
            "SECTOR": data['Info'].Sector,
            "INDUSTRY": data['Info'].Industry,
            "FISCAL_YEAR_END": data['Info'].FiscalYearEnd,
            "LATEST_QUARTER": data['Info'].LatestQuarter,
            "DIVIDEND_P_S": data['Info'].DividendPerShare,
            "WEBSITE": data['Info'].OfficialSite,
            "EX_DIVIDEND_DATE": data['Info'].ExDividendDate,
            "CONSOLE_TIME": data['Graph1D'].last_refreshed,

            }

    def pdf_download(self):
        save_file = filedialog.asksaveasfilename(
                    defaultextension = ".pdf",
                    title = "Save PDF",
                    initialfile = f"Report.pdf")
        if save_file:
            pdf = PDF(self.info, save_file)
            pdf.to_pdf()

            # 3. Convierte la ruta del archivo a un URI y ábrelo en el navegador
            try:
                file_uri = pathlib.Path(save_file).as_uri()
                webbrowser.open_new_tab(file_uri)
            except Exception as e:
                print(f"No se pudo abrir el PDF en el navegador: {e}")
        

class InfoTab(ttk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.parent = parent
        self.columnconfigure((0, 1), weight = 1)

        if data == None:
            self.noinfo = InfoNotObtained(self)
            self.noinfo.grid(row=0, column=0, columnspan=5, padx=10, sticky="nsew")

        self.title = ttk.Label(self, text = f"{data.Name} ({data.Symbol})",
                               font = title,
                               bootstyle = "primary")
        self.title.grid(row = 0, column = 0, sticky = "nwe", pady = 5, padx = 5)
        self.description = ttk.Label(self, text = f"{data.Description}",
                                     font = body,
                                     wraplength = 800,
                                     justify = "left")
        self.description.grid(row = 1, rowspan = 2,
                              column = 0, columnspan = 2,
                              sticky = "new", padx = 10, pady = 5)
        stock_data = dict(list(vars(data).items())[:12])
        self.stock_info = StockInfo(self, stock_data, parent.price)
        self.stock_info.grid(row = 1, column = 1, sticky = "nsew")

        self.sentiment = Sentimentmeter(self, parent.sentiment, data.Symbol)
        self.sentiment.grid(row = 2, column = 0, columnspan = 2)

        self.button = ttk.Button(self, text = "Download PDF", command = self.parent.pdf_download)
        self.button.grid(row = 3, column = 0, sticky="nsew", columnspan =2)


class GraphTab(ttk.Frame):
    def __init__(self, parent, graph_data, data, string):
        super().__init__(parent)
        self.columnconfigure((0, 1), weight = 1)
        self.title = ttk.Label(self, text = f"{data.Name} ({data.Symbol})",
                               font = title,
                               bootstyle = "primary")
        self.title.grid(row = 0, column = 0, sticky = "nwe", pady = 5, padx = 5)
        self.subtitle = ttk.Label(self, text = string, font = title, bootstyle = "primary")
        self.subtitle.grid(row = 1, column = 0, sticky = "nsew")
        self.info = StockInfo(self, dict(list(vars(data).items())[:12]), parent.price)
        self.info.grid(row = 3, column = 1, rowspan = 3, sticky = "nsew", padx = 10)
        self.time = ttk.Label(self, text = f"Created at: {graph_data.last_refreshed}",
                              font = body, bootstyle = "secondary")
        self.time.grid(row = 2, column = 0, sticky = "nsew")
        self.grapher = Grapher(graph_data)
        self.fig = self.grapher.graph_gui()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=3, column=0, sticky="nsew")

class StockInfo(ttk.Frame):
    def __init__(self, parent, data, price):
        super().__init__(parent)
        self.columnconfigure((0, 1), weight = 1)
        self.price = ttk.Label(self, text = f"Current price: {price}",
                               font = subtitle,
                               bootstyle = "primary")
        self.price.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
        for (i, (title, value)) in enumerate(data.items()):
            if title == "Description":
                continue
            self.title = ttk.Label(self, text = f"{title}", font = subtitle)
            self.title.grid(row = (i+1), column = 0, sticky = "nsew")
            self.value = ttk.Label(self, text = f"{value}", font = body)
            self.value.grid(row = (i+1), column = 1, sticky = "nsew")
            if title == "OfficialSite":
                self.value.bind("<Button-1>", lambda e: webbrowser.open(data["OfficialSite"], new = 0, autoraise=True))

class Sentimentmeter(ttk.Frame):
    def __init__(self, parent, value, stock_name):
        super().__init__(parent)
        self.width = 800
        self.height = 140
        self.stock_name = stock_name

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg="#F0F0F0", bd=2, relief="flat")
        self.canvas.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.min_val = -0.5
        self.max_val = 0.5
        self.ranges = {
            "Bad :(": (-0.5, -0.35, "#E64C59"),
            "Meh": (-0.35, -0.15, "#FF8C00"),
            "Neutral": (-0.15, 0.15, "#808080"),
            "Pretty good": (0.15, 0.35, "#4CAF50"),
            "GOOD 🐛": (0.35, 0.5, "#388E3C")
        }
        self.labels = {
            -0.5: "-0.5",
            -0.35: "-0.35",
            -0.15: "-0.15",
            0.15: "0.15",
            0.35: "0.35",
            0.5: "0.5   "
        }

        self.arrow_id = None
        self.value_text_id = None
        self.value_bg_rect_id = None

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.draw_gauge()

        self.set_value(value)

    def draw_gauge(self):
        y_center_bar = self.height / 2 + 5
        y_top = y_center_bar - 20
        y_bottom = y_center_bar + 20
        text_label_y = y_bottom + 15

        self.canvas.create_text(self.width / 2, 25, text = f"Stock Market Feeling ({self.stock_name})",
                               font = subtitle, fill="white")

        for name, (start_val, end_val, color) in self.ranges.items():
            x1 = self._value_to_x(start_val)
            x2 = self._value_to_x(end_val)
            self.canvas.create_rectangle(x1, y_top, x2, y_bottom, fill=color, outline=color, width=1)
            center_x = (x1 + x2) / 2
            self.canvas.create_text(center_x, y_center_bar, text = name.replace("_", " "),
                                   font = body, fill="white")

        for val, text in self.labels.items():
            x = self._value_to_x(val)
            self.canvas.create_text(x, text_label_y, text=text, font = body, fill="#555555")
            self.canvas.create_line(x, y_bottom, x, y_bottom + 5, fill="#555555")

    def _value_to_x(self, value):
        range_val = self.max_val - self.min_val
        normalized_val = (value - self.min_val) / range_val
        x = normalized_val * self.width
        return x

    def set_value(self, value):
        if self.arrow_id:
            self.canvas.delete(self.arrow_id)
        if self.value_text_id:
            self.canvas.delete(self.value_text_id)
        if self.value_bg_rect_id:
            self.canvas.delete(self.value_bg_rect_id)

        arrow_x = self._value_to_x(value)
        arrow_y_top = self.height / 2 + 30
        arrow_y_bottom = arrow_y_top + 15
        arrow_base_width = 10

        self.arrow_id = self.canvas.create_polygon(
            arrow_x, arrow_y_bottom,
            arrow_x - arrow_base_width, arrow_y_top,
            arrow_x + arrow_base_width, arrow_y_top,
            fill="black", outline="black"
        )

        text_pos_y = arrow_y_bottom + 15
        temp_text_id = self.canvas.create_text(
            arrow_x, text_pos_y,
            text=f"{value:.1f}",
            font=body,
            fill="white"
        )
        self.update_idletasks()
        bbox = self.canvas.bbox(temp_text_id)

        if bbox:
            padding_x = 7
            padding_y = 3
            rect_x1 = bbox[0] - padding_x
            rect_y1 = bbox[1] - padding_y
            rect_x2 = bbox[2] + padding_x
            rect_y2 = bbox[3] + padding_y

            self.value_bg_rect_id = self.canvas.create_rectangle(
                rect_x1, rect_y1, rect_x2, rect_y2,
                fill="black", outline="black", width=1
            )
            self.canvas.delete(temp_text_id)
            self.value_text_id = self.canvas.create_text(
                arrow_x, text_pos_y,
                text=f"{value:.1f}",
                font=body,
                fill="white"
            )
            self.canvas.tag_raise(self.value_text_id, self.value_bg_rect_id)
        else:
            self.value_text_id = self.canvas.create_text(
                arrow_x, text_pos_y,
                text=f"{value:.1f}",
                font=body,
                fill="white"
            )

def clean_temp_files(root, folder):
    print(f"Iniciando limpieza de la carpeta: {folder}")
    if os.path.exists(folder):
        for nombre_archivo in os.listdir(folder):
            ruta_archivo = os.path.join(folder, nombre_archivo)
            try:
                if os.path.isfile(ruta_archivo) or os.path.islink(ruta_archivo):
                    os.unlink(ruta_archivo)
                elif os.path.isdir(ruta_archivo):
                    shutil.rmtree(ruta_archivo)
            except Exception as e:
                print(f"Error al eliminar {ruta_archivo}. Razón: {e}")
        print("Limpieza completada.")
    else:
        print(f"La carpeta '{folder}' no existe, no se necesita limpieza.")
    root.destroy()

def main():
    interface = Interface()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    carpeta_temp = os.path.join(script_dir, "resources", "DOCS", "temp")

    interface.protocol("WM_DELETE_WINDOW", lambda: clean_temp_files(interface, carpeta_temp))

    interface.mainloop()


if __name__ == "__main__":
    main()