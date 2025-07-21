import os
import jinja2
import pdfkit
from ImageGenerator import Grapher
from types import SimpleNamespace as namespace
class PDF:
    def __init__(self, info: dict, output_path, css_path=None):
        render_data = info.copy()

        # Configuración de Jinja para cargar la plantilla
        template_path = os.path.dirname(os.path.abspath(__file__))
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
        template = env.get_template("template.html")
        self.html = template.render(render_data)
        
        # Definir parámetros del PDF
        self.options = {
            "page-size": "A4",
            "margin-top": "0.05in",
            "margin-right": "0.05in",
            "margin-bottom": "0.05in",
            "margin-left": "0.05in",
            "encoding": "UTF-8",
            "enable-local-file-access": None 
        }
        
        # --- CÓDIGO CORREGIDO Y CON DEPURACIÓN ---
        
        # 1. Calcular la ruta raíz del proyecto de forma robusta
        #    Sube tres niveles desde la ubicación de este script (resources/DOCS/ -> resources/ -> POO Proyect/)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(script_dir))

        # 2. Construir la ruta completa al ejecutable
        wkhtmltopdf_path = os.path.join(project_root,
                                         "wkhtmltopdf", 
                                         "bin", 
                                         "wkhtmltopdf.exe")
        
        # 3. (Depuración) Imprimir las rutas para verificar
        print(f"DEBUG: Raíz del proyecto calculada: {project_root}")
        print(f"DEBUG: Ruta de wkhtmltopdf esperada: {wkhtmltopdf_path}")
        
        # 4. (Depuración) Verificar si el archivo realmente existe antes de pasarlo a pdfkit
        if not os.path.exists(wkhtmltopdf_path):
            raise FileNotFoundError(
                f"El ejecutable wkhtmltopdf no se encontró en la ruta calculada: '{wkhtmltopdf_path}'. "
                "Por favor, verifica que la carpeta 'REQUIREMENTS' está en la raíz del proyecto."
            )

        self.config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
        self.output_path = output_path
    
    def to_pdf(self):
        pdfkit.from_string(self.html, self.output_path, options=self.options, configuration=self.config)

# Example:
if __name__ == "__main__":
    
    time_info = namespace(last_refreshed='2025-07-18 19:45:00', current_value='231.1000', values=[('231.1000', '2025-07-18 19:45:00'), ('231.1000', '2025-07-18 19:30:00'), ('231.0000', '2025-07-18 19:15:00'), ('231.0000', '2025-07-18 19:00:00'), ('230.6600', '2025-07-18 18:45:00'), ('230.6600', '2025-07-18 18:30:00'), ('231.0000', '2025-07-18 18:15:00'), ('230.6600', '2025-07-18 18:00:00'), ('229.7200', '2025-07-18 17:45:00'), ('229.7200', '2025-07-18 17:30:00'), ('230.9900', '2025-07-18 17:15:00'), ('231.0000', '2025-07-18 17:00:00'), ('230.9900', '2025-07-18 16:45:00'), ('231.1800', '2025-07-18 16:30:00'), ('231.1800', '2025-07-18 16:15:00'), ('231.4900', '2025-07-18 16:00:00'), ('231.2000', '2025-07-18 15:45:00'), ('229.7050', '2025-07-18 15:30:00'), ('229.4150', '2025-07-18 15:15:00'), ('228.9900', '2025-07-18 15:00:00'), ('229.2950', '2025-07-18 14:45:00'), ('229.9200', '2025-07-18 14:30:00'), ('230.2000', '2025-07-18 14:15:00'), ('230.1000', '2025-07-18 14:00:00'), ('229.5975', '2025-07-18 13:45:00'), ('229.8950', '2025-07-18 13:30:00'), ('229.6800', '2025-07-18 13:15:00'), ('228.6200', '2025-07-18 13:00:00'), ('228.7100', '2025-07-18 12:45:00'), ('228.4900', '2025-07-18 12:30:00'), ('229.4000', '2025-07-18 12:15:00'), ('230.1250', '2025-07-18 12:00:00'), ('230.7200', '2025-07-18 11:45:00'), ('231.5200', '2025-07-18 11:30:00'), ('230.7400', '2025-07-18 11:15:00'), ('230.1650', '2025-07-18 11:00:00'), ('230.1400', '2025-07-18 10:45:00'), ('230.7500', '2025-07-18 10:30:00'), ('229.3900', '2025-07-18 10:15:00'), ('230.4400', '2025-07-18 10:00:00'), ('231.5100', '2025-07-18 09:45:00'), ('232.7650', '2025-07-18 09:30:00'), ('234.4700', '2025-07-18 09:15:00'), ('234.1800', '2025-07-18 09:00:00'), ('234.2000', '2025-07-18 08:45:00'), ('233.5500', '2025-07-18 08:30:00'), ('234.2000', '2025-07-18 08:15:00'), ('234.2000', '2025-07-18 08:00:00'), ('233.9200', '2025-07-18 07:45:00'), ('234.2400', '2025-07-18 07:30:00'), ('234.2400', '2025-07-18 07:00:00'), ('234.9900', '2025-07-18 06:45:00'), ('234.0000', '2025-07-18 06:30:00'), ('234.2400', '2025-07-18 06:00:00'), ('234.5400', '2025-07-18 05:30:00'), ('234.9900', '2025-07-18 05:15:00'), ('234.9900', '2025-07-18 04:45:00'), ('234.5400', '2025-07-18 04:30:00'), ('234.9900', '2025-07-18 04:15:00'), ('235.0000', '2025-07-18 04:00:00'), ('233.9100', '2025-07-17 19:45:00'), ('233.9200', '2025-07-17 19:30:00'), ('233.9000', '2025-07-17 19:15:00'), ('233.8000', '2025-07-17 19:00:00'), ('233.9100', '2025-07-17 18:45:00'), ('233.2800', '2025-07-17 18:30:00'), ('233.1501', '2025-07-17 18:15:00'), ('233.7000', '2025-07-17 18:00:00'), ('233.7500', '2025-07-17 17:45:00'), ('233.9200', '2025-07-17 17:30:00'), ('233.9200', '2025-07-17 17:15:00'), ('233.9200', '2025-07-17 17:00:00'), ('233.9000', '2025-07-17 16:45:00'), ('232.9000', '2025-07-17 16:30:00'), ('232.9000', '2025-07-17 16:15:00'), ('233.9200', '2025-07-17 16:00:00'), ('233.9800', '2025-07-17 15:45:00'), ('234.0450', '2025-07-17 15:30:00'), ('234.1550', '2025-07-17 15:15:00'), ('233.5900', '2025-07-17 15:00:00'), ('233.6500', '2025-07-17 14:45:00'), ('233.5100', '2025-07-17 14:30:00'), ('232.8900', '2025-07-17 14:15:00'), ('232.3800', '2025-07-17 14:00:00'), ('232.5300', '2025-07-17 13:45:00'), ('232.7200', '2025-07-17 13:30:00'), ('232.0650', '2025-07-17 13:15:00'), ('232.1550', '2025-07-17 13:00:00'), ('232.4700', '2025-07-17 12:45:00'), ('231.2800', '2025-07-17 12:30:00'), ('231.5300', '2025-07-17 12:15:00'), ('233.2500', '2025-07-17 12:00:00'), ('233.9400', '2025-07-17 11:45:00'), ('234.5600', '2025-07-17 11:30:00'), ('234.7700', '2025-07-17 11:15:00'), ('235.6200', '2025-07-17 11:00:00')])
    grapher = Grapher(time_info)
    # Guarda la gráfica en el mismo directorio donde se ejecuta el script
    # o especifica una ruta absoluta o relativa adecuada para wkhtmltopdf
    day_path = grapher.plot(filename="day_graph.png")
    month_path = grapher.plot(filename="month_graph.png")
    year_path = grapher.plot(filename="year_graph.png")
    
    tickers = [{'ticker': 'GITS', 'price': '3.84', 'change_amount': '2.21', 'change_percentage': '135.5828%', 'volume': '46169804'}, {'ticker': 'BMNR', 'price': '134.99', 'change_amount': '76.49', 'change_percentage': '130.7521%', 'volume': '37383643'}, {'ticker': 'RGC', 'price': '22.99', 'change_amount': '12.63', 'change_percentage': '121.9112%', 'volume': '18750813'}, {'ticker': 'LRHC', 'price': '0.15', 'change_amount': '0.0699', 'change_percentage': '87.2659%', 'volume': '646214936'}, {'ticker': 'BCTXW', 'price': '0.0745', 'change_amount': '0.0325', 'change_percentage': '77.381%', 'volume': '30431'}, {'ticker': 'AP+', 'price': '0.023', 'change_amount': '0.01', 'change_percentage': '76.9231%', 'volume': '6028'}, {'ticker': 'EGG', 'price': '5.65', 'change_amount': '1.95', 'change_percentage': '52.7027%', 'volume': '8818286'}, {'ticker': 'WOLF', 'price': '1.17', 'change_amount': '0.3969', 'change_percentage': '51.3388%', 'volume': '209443868'}, {'ticker': 'SWVLW', 'price': '0.0184', 'change_amount': '0.0059', 'change_percentage': '47.2%', 'volume': '5'}, {'ticker': 'MBAVW', 'price': '2.74', 'change_amount': '0.85', 'change_percentage': '44.9735%', 'volume': '6168'}, {'ticker': 'CDTTW', 'price': '0.012', 'change_amount': '0.0037', 'change_percentage': '44.5783%', 'volume': '9302'}, {'ticker': 'OUSTW', 'price': '0.0388', 'change_amount': '0.0118', 'change_percentage': '43.7037%', 'volume': '20185'}, {'ticker': 'AENTW', 'price': '0.24', 'change_amount': '0.0688', 'change_percentage': '40.1869%', 'volume': '37210'}, {'ticker': 'LIXT', 'price': '2.83', 'change_amount': '0.81', 'change_percentage': '40.099%', 'volume': '64086883'}, {'ticker': 'JUNS', 'price': '1.65', 'change_amount': '0.46', 'change_percentage': '38.6555%', 'volume': '4909787'}, {'ticker': 'IVDAW', 'price': '0.11', 'change_amount': '0.03', 'change_percentage': '37.5%', 'volume': '27326'}, {'ticker': 'ACONW', 'price': '0.0357', 'change_amount': '0.0096', 'change_percentage': '36.7816%', 'volume': '751'}, {'ticker': 'PERF+', 'price': '0.0545', 'change_amount': '0.0145', 'change_percentage': '36.25%', 'volume': '4580'}, {'ticker': 'DSYWW', 'price': '0.0228', 'change_amount': '0.006', 'change_percentage': '35.7143%', 'volume': '2565'}, {'ticker': 'THTX', 'price': '3.2', 'change_amount': '0.84', 'change_percentage': '35.5932%', 'volume': '10557939'}]
    
    data = namespace(Value=123, Symbol = "IBM", AssetType = "Common Stock", Name = "International Business Machines", Description = "International Business Machines Corporation (IBM) is an American multinational technology company headquartered in Armonk, New York, with operations in over 170 countries. The company began in 1911, founded in Endicott, New York, as the Computing-Tabulating-Recording Company (CTR) and was renamed International Business Machines in 1924. IBM is incorporated in New York. IBM produces and sells computer hardware, middleware and software, and provides hosting and consulting services in areas ranging from mainframe computers to nanotechnology. IBM is also a major research organization, holding the record for most annual U.S. patents generated by a business (as of 2020) for 28 consecutive years. Inventions by IBM include the automated teller machine (ATM), the floppy disk, the hard disk drive, the magnetic stripe card, the relational database, the SQL programming language, the UPC barcode, and dynamic random-access memory (DRAM). The IBM mainframe, exemplified by the System/360, was the dominant computing platform during the 1960s and 1970s.", CIK = "51143", Exchange = "NYSE", Currency = "USD", Country = "USA", Sector = "TECHNOLOGY", Industry = "COMPUTER & OFFICE EQUIPMENT", Address = "1 NEW ORCHARD ROAD, ARMONK, NY, US", OfficialSite = "https://www.ibm.com", FiscalYearEnd = "December", LatestQuarter = "2025-03-31", MarketCapitalization = "271356035000", EBITDA = "13950000000", PERatio = "49.99", PEGRatio = "2.165", BookValue = "28.92", DividendPerShare = "6.68", DividendYield = "0.0228", EPS = "5.84", RevenuePerShareTTM = "67.97", ProfitMargin = "0.0871", OperatingMarginTTM = "0.124", ReturnOnAssetsTTM = "0.0447", ReturnOnEquityTTM = "0.218", RevenueTTM = "62832001000", GrossProfitTTM = "35840000000", DilutedEPSTTM = "5.84", QuarterlyEarningsGrowthYOY = "-0.349", QuarterlyRevenueGrowthYOY = "0.005", AnalystTargetPrice = "258.02", AnalystRatingStrongBuy = "2", AnalystRatingBuy = "8", AnalystRatingHold = "9", AnalystRatingSell = "2", AnalystRatingStrongSell = "1", TrailingPE = "49.99", ForwardPE = "26.6", PriceToSalesRatioTTM = "4.319", PriceToBookRatio = "10.1", EVToRevenue = "5.1", EVToEBITDA = "26.01", Beta = "0.652", SharesOutstanding = "929397000", SharesFloat = "927361000", PercentInsiders = "0.119", PercentInstitutions = "65.274", DividendDate = "2025-06-10", ExDividendDate = "2025-05-09")
    
    info = {
            "tickers": tickers, 
            "SENTIMENT_VALUE": 0.2,
            "NAME": data.Name,
            "TICKER": data.Symbol,
            "VALUE": data.Value,
            "DAY_GRAPH":day_path,
            "MONTH_GRAPH":month_path,
            "YEAR_GRAPH":year_path,
            "COMPANY_DESPRIPTION": data.Description,
            }
    pdf = PDF(info,r"D:\Projects\POO Proyect\PRUEBA.pdf")
    pdf.to_pdf()
    print("PDF generado exitosamente en D:\\Projects\\POO Proyect\\PRUEBA.pdf")