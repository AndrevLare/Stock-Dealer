import os
import jinja2
import pdfkit

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
            "page-size": "Letter",
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
    tickers = [{'ticker': 'GITS', 'price': '3.84', 'change_amount': '2.21', 'change_percentage': '135.5828%', 'volume': '46169804'}, {'ticker': 'BMNR', 'price': '134.99', 'change_amount': '76.49', 'change_percentage': '130.7521%', 'volume': '37383643'}, {'ticker': 'RGC', 'price': '22.99', 'change_amount': '12.63', 'change_percentage': '121.9112%', 'volume': '18750813'}, {'ticker': 'LRHC', 'price': '0.15', 'change_amount': '0.0699', 'change_percentage': '87.2659%', 'volume': '646214936'}, {'ticker': 'BCTXW', 'price': '0.0745', 'change_amount': '0.0325', 'change_percentage': '77.381%', 'volume': '30431'}, {'ticker': 'AP+', 'price': '0.023', 'change_amount': '0.01', 'change_percentage': '76.9231%', 'volume': '6028'}, {'ticker': 'EGG', 'price': '5.65', 'change_amount': '1.95', 'change_percentage': '52.7027%', 'volume': '8818286'}, {'ticker': 'WOLF', 'price': '1.17', 'change_amount': '0.3969', 'change_percentage': '51.3388%', 'volume': '209443868'}, {'ticker': 'SWVLW', 'price': '0.0184', 'change_amount': '0.0059', 'change_percentage': '47.2%', 'volume': '5'}, {'ticker': 'MBAVW', 'price': '2.74', 'change_amount': '0.85', 'change_percentage': '44.9735%', 'volume': '6168'}, {'ticker': 'CDTTW', 'price': '0.012', 'change_amount': '0.0037', 'change_percentage': '44.5783%', 'volume': '9302'}, {'ticker': 'OUSTW', 'price': '0.0388', 'change_amount': '0.0118', 'change_percentage': '43.7037%', 'volume': '20185'}, {'ticker': 'AENTW', 'price': '0.24', 'change_amount': '0.0688', 'change_percentage': '40.1869%', 'volume': '37210'}, {'ticker': 'LIXT', 'price': '2.83', 'change_amount': '0.81', 'change_percentage': '40.099%', 'volume': '64086883'}, {'ticker': 'JUNS', 'price': '1.65', 'change_amount': '0.46', 'change_percentage': '38.6555%', 'volume': '4909787'}, {'ticker': 'IVDAW', 'price': '0.11', 'change_amount': '0.03', 'change_percentage': '37.5%', 'volume': '27326'}, {'ticker': 'ACONW', 'price': '0.0357', 'change_amount': '0.0096', 'change_percentage': '36.7816%', 'volume': '751'}, {'ticker': 'PERF+', 'price': '0.0545', 'change_amount': '0.0145', 'change_percentage': '36.25%', 'volume': '4580'}, {'ticker': 'DSYWW', 'price': '0.0228', 'change_amount': '0.006', 'change_percentage': '35.7143%', 'volume': '2565'}, {'ticker': 'THTX', 'price': '3.2', 'change_amount': '0.84', 'change_percentage': '35.5932%', 'volume': '10557939'}]
    info = {"TITULO":"HOLA",
            "tickers": tickers, 
            "SENTIMENT_VALUE": 0.4,
            "NAME": "Dani",
            "TICKER": "AAPL",
            "VALUE": "150.00",}
    pdf = PDF(info,r"D:\Projects\POO Proyect\PRUEBA.pdf")
    pdf.to_pdf()
    print("PDF generado exitosamente en D:\\Projects\\POO Proyect\\PRUEBA.pdf")