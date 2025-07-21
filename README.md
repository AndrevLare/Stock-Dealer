# _Stock-Dealer_ (POOyecto)

<img src="Misc/stock-dealer.jpg" alt="ICON" width="1000" />

# AUTORES

<h3 style="display: flex; align-items:center">
<img src="Misc/Taizoo.jpeg" alt="TaizooNameplate" width="262"/><span>ㅤㅤ­­­­</span><span>ㅤㅤ­­­­</span>
  <img src="Misc/Gorje.jpeg" alt="GorjeNameplate" width="262"/><span>ㅤㅤ­­­­</span><span>ㅤㅤ­­­­</span>
  <img src="Misc/Daniel.jpeg" alt="DanielNameplate" width="291"/>
</h3>

## Diagrama de clases:

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

## Antes de empezar:

Hagan pull antes de empezar, asi si alguien cambió algo cuando no estaban,
actualizan su repositorio local y evitan encontrar conflictos cuando suben los
cambios. Comando:

```
git pull origin main
```

## Cada q terminen una caracteristica o quieran crear un "punto de guardado":

Cuando cambien cosas van a haber cambios sin guardar en el repo asi hayan
guardado el archivo, el guardado de archivos en el PC, guardado en el repo
local, y guardado en el repo remoto son cosas ditintas. tienen q hacer cada
una, para registrar los cambios en el local:

si crearon o borraron archivos:

```
git add .
git commit -a -m "mensaje descriptivo para el commit"
```

si solo modificaron:

```
git commit -a -m "mensaje descriptivo para el commit"
```

## Al terminar:

Cuando terminen de trabajar, tienen q subir sus cambios (su lista de commits
realizados) al repositorio remoto para que otros los puedan ver y usar, para
esto se hace push, esto lo q hace es añadir todos los commits realizados en
local a la lista de commits del repo remoto. Antes de hacer push asegurense
de hacer commit en todos sus cambios.

```
git push origin main
```

# Estructuras de datos usadas:

## Para winners-losers-actives:

obteniendo la data de forma:

```
Scrapper().winners_lossers_actives()
```

puedes acceder a las tres secciones de la forma:

```
# Ejemplo de uso

scrapper = Scrapper()

raw_data = scrapper.winners_losers_actives()


# Las 3 listas se acceden asi:

winners = raw_data.winners
losers = raw_data.losers
actives = raw_data.actives
```

Estos datos son listas de diccionarios, ejemplo de acceso:

```
if __name__ == "__main__":
    # Test
    scrap = Scraper()
    market_data = scrap.winners_lossers_actives()

    # Obtener datos de cada acción ganadora
    print("=== TOP GAINERS ===")
    for stock in market_data.winners:
        ticker = stock['ticker']
        price = stock['price']
        change_amount = stock['change_amount']
        change_percentage = stock['change_percentage']
        volume = stock['volume']

        print(f"Ticker: {ticker}")
        print(f"Precio: ${price}")
        print(f"Cambio: ${change_amount} ({change_percentage})")
        print(f"Volumen: {volume}")
        print("-" * 30)
```

## Para Obtener la info y valores de la accion de la compañia:

obteniendo la data de forma:

```
Scrapper().company_info(ticker)
```

puedes acceder a la info de la forma:

```
# Ejemplo de uso

scrapper = Scrapper()

data = scrapper.company_info(ticker)

data.key
```

Siendo "key" el nombre del valor al que quieres accesar, aqui un JSON de ejemplo de como se llaman todos los datos q llegan para el ticker IBM, no se van a mostrar todos, (ver PDF de GUI):

```
{
    "Symbol": "IBM",
    "AssetType": "Common Stock",
    "Name": "International Business Machines",
    "Description": "International Business Machines Corporation (IBM) is an American multinational technology company headquartered in Armonk, New York, with operations in over 170 countries. The company began in 1911, founded in Endicott, New York, as the Computing-Tabulating-Recording Company (CTR) and was renamed International Business Machines in 1924. IBM is incorporated in New York. IBM produces and sells computer hardware, middleware and software, and provides hosting and consulting services in areas ranging from mainframe computers to nanotechnology. IBM is also a major research organization, holding the record for most annual U.S. patents generated by a business (as of 2020) for 28 consecutive years. Inventions by IBM include the automated teller machine (ATM), the floppy disk, the hard disk drive, the magnetic stripe card, the relational database, the SQL programming language, the UPC barcode, and dynamic random-access memory (DRAM). The IBM mainframe, exemplified by the System/360, was the dominant computing platform during the 1960s and 1970s.",
    "CIK": "51143",
    "Exchange": "NYSE",
    "Currency": "USD",
    "Country": "USA",
    "Sector": "TECHNOLOGY",
    "Industry": "COMPUTER & OFFICE EQUIPMENT",
    "Address": "1 NEW ORCHARD ROAD, ARMONK, NY, US",
    "OfficialSite": "https://www.ibm.com",
    "FiscalYearEnd": "December",
    "LatestQuarter": "2025-03-31",
    "MarketCapitalization": "271356035000",
    "EBITDA": "13950000000",
    "PERatio": "49.99",
    "PEGRatio": "2.165",
    "BookValue": "28.92",
    "DividendPerShare": "6.68",
    "DividendYield": "0.0228",
    "EPS": "5.84",
    "RevenuePerShareTTM": "67.97",
    "ProfitMargin": "0.0871",
    "OperatingMarginTTM": "0.124",
    "ReturnOnAssetsTTM": "0.0447",
    "ReturnOnEquityTTM": "0.218",
    "RevenueTTM": "62832001000",
    "GrossProfitTTM": "35840000000",
    "DilutedEPSTTM": "5.84",
    "QuarterlyEarningsGrowthYOY": "-0.349",
    "QuarterlyRevenueGrowthYOY": "0.005",
    "AnalystTargetPrice": "258.02",
    "AnalystRatingStrongBuy": "2",
    "AnalystRatingBuy": "8",
    "AnalystRatingHold": "9",
    "AnalystRatingSell": "2",
    "AnalystRatingStrongSell": "1",
    "TrailingPE": "49.99",
    "ForwardPE": "26.6",
    "PriceToSalesRatioTTM": "4.319",
    "PriceToBookRatio": "10.1",
    "EVToRevenue": "5.1",
    "EVToEBITDA": "26.01",
    "Beta": "0.652",
    "52WeekHigh": "296.16",
    "52WeekLow": "169.32",
    "50DayMovingAverage": "265.83",
    "200DayMovingAverage": "240.9",
    "SharesOutstanding": "929397000",
    "SharesFloat": "927361000",
    "PercentInsiders": "0.119",
    "PercentInstitutions": "65.274",
    "DividendDate": "2025-06-10",
    "ExDividendDate": "2025-05-09"
}
```

## Dia, Mes y Año:

con las funciones get_info_and_1D_graph(), get_1M_graph() y get_1Y_graph()
podemos acceder al historico de valores de la accion, si no encuentra info,
se retorna None,

```
#ejemplo de uso

ticker = "AAPL"
day_info = scrap.get_info_and_1D_graph(ticker)

if day_info:
    print(f"Last Refreshed: {day_info.last_refreshed}")
    print(f"Current Value: {day_info.current_value}")
    print("Values:", day_info.values)

else:
    print("No data found for the ticker.")


month_info = scrap.get_1M_graph(ticker)

if month_info:
    print(f"Last Refreshed: {month_info.last_refreshed}")
    print("Values:", month_info.values)

else:
    print("No data found for the ticker.")


year_info = scrap.get_1Y_graph(ticker)

if year_info:
    print(f"Last Refreshed: {year_info.last_refreshed}")
    print("Values:", year_info.values)

else:
    print("No data found for the ticker.")
```
