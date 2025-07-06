import os
import jinja2
import pdfkit
from collections import defaultdict

class PDF:
    def __init__(self, info: dict, css_path=''):
        #os. functions, so it works on both win and linux
        template_path = os.path.dirname(os.path.abspath(__file__))
        template_name = "template.html"
        self.css_path = css_path
        self.info = info
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
        template = env.get_template(template_name)
        self.html = template.render(self.info)
        #defining pdf parameters
        self.options = {"page-size": "Letter",
                   "margin-top": "0.05in",
                   "margin-right": "0.05in",
                   "margin-bottom": "0.05in",
                   "margin-left": "0.05in",
                   "encoding":"UTF-8"}
        #Defining the path of this package
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        wkhtmltopdf_path = os.path.join(project_root, 
                                         "wkhtmltopdf", 
                                         "bin", 
                                         "wkhtmltopdf.exe")
        self.config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
        self.output_path = r"C:\Users\danie\OneDrive\Documentos\POOyecto\resources\DOCS\prueba.pdf"
    
    def to_pdf(self):
        pdfkit.from_string(self.html,self.output_path,css=self.css_path,options=self.options, configuration= self.config)

# Example:
if __name__ == "__main__":
    info = {"TITULO":"HOLA",
            "PARRAFO":"LOREM IPSUM"}
    pdf = PDF(info)
    pdf.to_pdf()


