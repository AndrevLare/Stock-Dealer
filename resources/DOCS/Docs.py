import os
import jinja2
import pdfkit
from collections import defaultdict

class PDF:
    def __init__(self, ruta_template: str, info: dict, ruta_css=''):
        self.nombre_template = os.path.basename(ruta_template)
        self.ruta_template = os.path.dirname(ruta_template)
        self.info = info

    def create_pdf(self):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.ruta_template))
        template = env.get_template(self.nombre_template)
        html = template.render(self.info)
        options = {"page-size": "Letter", }
        print(html)
#hola
# Example:
if __name__ == "__main__":
    info = {"TITULO":"HOLA",
            "PARRAFO":"LOREM IPSUM"}
    ruta = r"C:\Users\danie\OneDrive\Documentos\POOyecto\resources\__pycache__\DOCS\template.html"
    pdf = PDF(ruta, info)
    pdf.create_pdf()

