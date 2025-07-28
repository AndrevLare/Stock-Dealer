# _Stock-Dealer_

<img src="Misc/stock-dealer.jpg" alt="ICON" width="1000" />

# AUTHORS

<h3 style="display: flex; align-items:center">
<img src="Misc/Taizoo.jpeg" alt="TaizooNameplate" width="262"/>
  <img src="Misc/Gorje.jpeg" alt="GorjeNameplate" width="262"/>
  <img src="Misc/Daniel.jpeg" alt="DanielNameplate" width="291"/>
</h3>

# Stock-Dealer
With Stock Dealer you can get info and analyze common stocks, look at the most actives, top winners and losers, also get info from specific tickers. Look at the market sentiment and download a pdf report to take the data and use it as you want. *The proyect is in a early phase and may crash*

## How to use:
1. Download the repository
2. Go to https://www.alphavantage.co/support/#api-key and get 2 api keys
3. Create an .env on program's root and put the following info:
   ```
   BASE_URL=https://www.alphavantage.co/query?

   API_KEY_1=Your 1st api key
   API_KEY_2=Your 2nd api key
   ```
4. Activate your virtual enviroment (in case you have one)
   ```
   .\env\Scripts\activate
   ```
4. Execute the following command (be sure that you are on the program's folder)
   ```
   pip install -r requirements.txt
   ```
6. Run the main.py

##  By:
- [@AndrevLare](https://github.com/AndrevLare)
- [@Taizooavila](https://github.com/Taizooavila)
- [@daseb-xd](https://github.com/daseb-xd)

## Class Diagram:

```mermaid
classDiagram

    class Interface {
        +style
        +heading
        +main_page
        +stock_page
        +__init__()
        +to_main_page()
        +to_stock_page(ticker:str)
    }

    class Heading {
        +parent
        +title
        +search
        +__init__(parent)
    }

    class Search {
        +parent
        +label
        +input
        +button
        +__init__(parent)
        __create_stock_page()
    }

    class MainPage {
        +parent
        +winners
        +losers
        +actives
        +__init__(parent)
    }

    class TopsWidget {
        +parent
        +label
        +section
        +w_1
        +w_2
        +w_3
        +w_4
        +w_5
        +__init__(parent, data, section)
    }

    class InfoNotObtained {
        +label
    }

    class StockMiniInfo {
        +parent
        +section
        +label_1
        +label_2
        +__init__(parent, data)
        __create_stock_page(ticker)
    }

    class StockPage {
        +price
        +sentiment
        +info
        +__init__(parent, data)
        +pdf_download()
    }

    class InfoTab {
        +parent
        +title
        +description
        +stock_info
        +sentiment
        +button
        +__init__(parent, data)
    }

    class GraphTab {
        +title
        +subtitle
        +info
        +time
        +grapher
        +fig
        +canvas
        +__init__(parent, graph_data, data, string) 
    }

    class StockInfo {
        +price
        +titles
        +values
        +__init__(parent, data, price)
    }

    class Sentimentmeter {
        +width
        +height
        +stock_name
        +canvas
        +min_val
        +max_val
        +ranges
        +labels
        +arrow_id
        +value_text_id
        +value_bg_rect_id

        +__init__(parent, value: float, stock_name: str)
        +draw_gauge()
        -_value_to_x(value: float) float
        +set_value(value: float)
    }

    class Scraper {
        +__init__()
        +winners_lossers_actives(): dict
        +get_info_and_1D_graph(ticker:string): dict
        +get_1M_graph(ticker:string): dict
        +get_1Y_graph(ticker:string): dict
        +company_info(ticker:string): dict
        +get_ticker_sentiment(ticker:string): float
        - api_key()
    }

    class DataPage {
        +CodeInput parent
        +ttk.Label data_label
        +ttk.Button clear_button
        +ttk.Button pdf_button
        +CreatePDF pdf_create
        +__init__(Data)
        +clear_page()
        -create_compare_page()
    }

    class CreatePDF {
        - info: dict
        - output_path: r str
        + __init__(info: dict, output_path: str)
        + to_pdf()
    }

    class Grapher {
        - time_info: dict
        + __init__(info: dict, output_path: str)
        + plot(filename)
    }

    Interface "1" *-- "2" CodeInput: contains

    Interface --|> tk.Tk
    Heading --|> ttk.Frame
    Search --|> ttk.Frame
    MainPage --|> ttk.Frame
    TopsWidget --|> ttk.Frame
    InfoNotObtained --|> ttk.Frame
    StockMiniInfo --|> ttk.Frame
    StockPage --|> ttk.Notebook
    InfoTab --|> ttk.Frame
    GraphTab --|> ttk.Frame
    StockInfo --|> ttk.Frame
    Sentimentmeter --|> ttk.Frame

    Interface "1" *-- "1" Heading : Contiene
    Interface "1" *-- "1" MainPage : Contiene
    Interface "1" *-- "0..1" StockPage : Contiene (dinámico)

    Heading "1" *-- "1" Search : Contiene

    MainPage "1" *-- "3" TopsWidget : Contiene (Winners, Losers, Actives)
    TopsWidget "1" *-- "5" StockMiniInfo : Contiene (hasta 5 items)

    StockPage "1" *-- "1" InfoTab : Contiene
    StockPage "1" *-- "3" GraphTab : Contiene (1D, 1M, 1Y)
    InfoTab "1" *-- "1" StockInfo : Contiene
    InfoTab "1" *-- "1" Sentimentmeter : Contiene

    MainPage ..> Scraper : Usa para obtener datos
    StockPage ..> Grapher : Usa para gráficos
    StockPage ..> PDF : Usa para generar reportes
    StockMiniInfo ..> Interface : Navega a StockPage
    Search ..> Interface : Navega a StockPage
```

