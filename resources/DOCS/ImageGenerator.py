import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from types import SimpleNamespace as namespace
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os # Importar el módulo os para manejar rutas de archivos

class Grapher():
    def __init__(self, time_info):
        self.last_refreshed = time_info.last_refreshed
        self.data = time_info.values
        
        try:
            self.current_value = time_info.current_value
        except:
            self.current_value = 0

        # Asegurarse de que el formato de tiempo sea compatible con matplotlib
        try:
            self.time = [datetime.strptime(point[1], '%Y-%m-%d %H:%M:%S') for point in self.data]
        except:
            self.time = [datetime.strptime(point[1], '%Y-%m-%d') for point in self.data]
        self.values = [float(point[0]) for point in self.data]

    def graph_gui(self):
        fig = plt.Figure(figsize=(3, 4))
        ax = fig.add_subplot(111)
        ax.plot(self.time, self.values, marker='o', linestyle='-', markersize=4)
        ax.set_xlabel("Fecha y Hora")
        ax.set_ylabel("Valor")
        ax.grid(True)
        fig.autofmt_xdate()
        return fig

    def plot(self, filename="stock_price_plot.png"):
        """
        Genera la gráfica y la guarda en un archivo.
        filename: La ruta y nombre del archivo donde se guardará la imagen.
        """
        name = filename
        filename = "resources/DOCS/temp/" + name
        plt.figure(figsize=(10, 6)) # Opcional: ajustar el tamaño de la figura
        plt.plot(self.time, self.values, marker='o', linestyle='-', markersize=4) # Añadir marcadores para visibilidad
        plt.xlabel("Date & Hour")
        plt.ylabel("Price")
        plt.grid(True) # Añadir una cuadrícula para mejor lectura

        # Mejorar el formato del eje X para las fechas/horas
        plt.gcf().autofmt_xdate()

        # Guardar la gráfica en un archivo
        # Se recomienda un formato PNG para wkhtmltopdf
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close() # Cerrar la figura para liberar memoria

        return os.path.abspath(filename) # Devuelve la ruta absoluta del archivo guardado

if __name__ == "__main__":
    # Example usage
    time_info = namespace(last_refreshed='2025-07-18 19:45:00', current_value='231.1000', values=[('231.1000', '2025-07-18 19:45:00'), ('231.1000', '2025-07-18 19:30:00'), ('231.0000', '2025-07-18 19:15:00'), ('231.0000', '2025-07-18 19:00:00'), ('230.6600', '2025-07-18 18:45:00'), ('230.6600', '2025-07-18 18:30:00'), ('231.0000', '2025-07-18 18:15:00'), ('230.6600', '2025-07-18 18:00:00'), ('229.7200', '2025-07-18 17:45:00'), ('229.7200', '2025-07-18 17:30:00'), ('230.9900', '2025-07-18 17:15:00'), ('231.0000', '2025-07-18 17:00:00'), ('230.9900', '2025-07-18 16:45:00'), ('231.1800', '2025-07-18 16:30:00'), ('231.1800', '2025-07-18 16:15:00'), ('231.4900', '2025-07-18 16:00:00'), ('231.2000', '2025-07-18 15:45:00'), ('229.7050', '2025-07-18 15:30:00'), ('229.4150', '2025-07-18 15:15:00'), ('228.9900', '2025-07-18 15:00:00'), ('229.2950', '2025-07-18 14:45:00'), ('229.9200', '2025-07-18 14:30:00'), ('230.2000', '2025-07-18 14:15:00'), ('230.1000', '2025-07-18 14:00:00'), ('229.5975', '2025-07-18 13:45:00'), ('229.8950', '2025-07-18 13:30:00'), ('229.6800', '2025-07-18 13:15:00'), ('228.6200', '2025-07-18 13:00:00'), ('228.7100', '2025-07-18 12:45:00'), ('228.4900', '2025-07-18 12:30:00'), ('229.4000', '2025-07-18 12:15:00'), ('230.1250', '2025-07-18 12:00:00'), ('230.7200', '2025-07-18 11:45:00'), ('231.5200', '2025-07-18 11:30:00'), ('230.7400', '2025-07-18 11:15:00'), ('230.1650', '2025-07-18 11:00:00'), ('230.1400', '2025-07-18 10:45:00'), ('230.7500', '2025-07-18 10:30:00'), ('229.3900', '2025-07-18 10:15:00'), ('230.4400', '2025-07-18 10:00:00'), ('231.5100', '2025-07-18 09:45:00'), ('232.7650', '2025-07-18 09:30:00'), ('234.4700', '2025-07-18 09:15:00'), ('234.1800', '2025-07-18 09:00:00'), ('234.2000', '2025-07-18 08:45:00'), ('233.5500', '2025-07-18 08:30:00'), ('234.2000', '2025-07-18 08:15:00'), ('234.2000', '2025-07-18 08:00:00'), ('233.9200', '2025-07-18 07:45:00'), ('234.2400', '2025-07-18 07:30:00'), ('234.2400', '2025-07-18 07:00:00'), ('234.9900', '2025-07-18 06:45:00'), ('234.0000', '2025-07-18 06:30:00'), ('234.2400', '2025-07-18 06:00:00'), ('234.5400', '2025-07-18 05:30:00'), ('234.9900', '2025-07-18 05:15:00'), ('234.9900', '2025-07-18 04:45:00'), ('234.5400', '2025-07-18 04:30:00'), ('234.9900', '2025-07-18 04:15:00'), ('235.0000', '2025-07-18 04:00:00'), ('233.9100', '2025-07-17 19:45:00'), ('233.9200', '2025-07-17 19:30:00'), ('233.9000', '2025-07-17 19:15:00'), ('233.8000', '2025-07-17 19:00:00'), ('233.9100', '2025-07-17 18:45:00'), ('233.2800', '2025-07-17 18:30:00'), ('233.1501', '2025-07-17 18:15:00'), ('233.7000', '2025-07-17 18:00:00'), ('233.7500', '2025-07-17 17:45:00'), ('233.9200', '2025-07-17 17:30:00'), ('233.9200', '2025-07-17 17:15:00'), ('233.9200', '2025-07-17 17:00:00'), ('233.9000', '2025-07-17 16:45:00'), ('232.9000', '2025-07-17 16:30:00'), ('232.9000', '2025-07-17 16:15:00'), ('233.9200', '2025-07-17 16:00:00'), ('233.9800', '2025-07-17 15:45:00'), ('234.0450', '2025-07-17 15:30:00'), ('234.1550', '2025-07-17 15:15:00'), ('233.5900', '2025-07-17 15:00:00'), ('233.6500', '2025-07-17 14:45:00'), ('233.5100', '2025-07-17 14:30:00'), ('232.8900', '2025-07-17 14:15:00'), ('232.3800', '2025-07-17 14:00:00'), ('232.5300', '2025-07-17 13:45:00'), ('232.7200', '2025-07-17 13:30:00'), ('232.0650', '2025-07-17 13:15:00'), ('232.1550', '2025-07-17 13:00:00'), ('232.4700', '2025-07-17 12:45:00'), ('231.2800', '2025-07-17 12:30:00'), ('231.5300', '2025-07-17 12:15:00'), ('233.2500', '2025-07-17 12:00:00'), ('233.9400', '2025-07-17 11:45:00'), ('234.5600', '2025-07-17 11:30:00'), ('234.7700', '2025-07-17 11:15:00'), ('235.6200', '2025-07-17 11:00:00')])
    grapher = Grapher(time_info)
    # Guarda la gráfica en el mismo directorio donde se ejecuta el script
    # o especifica una ruta absoluta o relativa adecuada para wkhtmltopdf
    image_path = grapher.plot(filename="stock_price_plot.png")
    print(f"Gráfica guardada en: {image_path}")

    # Ahora puedes pasar 'image_path' a tu sistema de generación de PDF
    # (por ejemplo, a tu función Jinja render)