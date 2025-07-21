import os
import shutil
import tkinter as tk
from tkinter import ttk

class StockMarketFeelingGauge:
    def __init__(self, master, width=800, height=140): # Increased height for better spacing
        self.master = master
        self.width = width
        self.height = height

        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="#F0F0F0", bd=2, relief="flat") # Changed background to light gray
        self.canvas.pack(pady=20, padx=20) # Added padx for better spacing from window edges

        self.min_val = -0.5
        self.max_val = 0.5
        self.ranges = {
            "Bearish": (-0.5, -0.35, "#E64C59"),  # Slightly adjusted red
            "Somewhat-Bearish": (-0.35, -0.15, "#FF8C00"), # Brighter orange
            "Neutral": (-0.15, 0.15, "#808080"),  # Medium gray
            "Somewhat Bullish": (0.15, 0.35, "#4CAF50"), # Brighter green
            "Bullish": (0.35, 0.5, "#388E3C")     # Darker green
        }
        self.labels = {
            -0.5: "-0.5",
            -0.35: "-0.35",
            -0.15: "-0.15",
            0.15: "0.15",
            0.35: "0.35",
            0.5: "0.5   "
        }

        self.draw_gauge()

        # Initial position of the arrow
        self.arrow_id = None
        self.value_text_id = None
        self.value_bg_rect_id = None

        # Slider to control the value (for demonstration)
        self.slider_frame = ttk.Frame(master)
        self.slider_frame.pack(pady=10)
        
        self.value_label = ttk.Label(self.slider_frame, text="Current Value: 0.2", font=("Arial", 10))
        self.value_label.pack(side=tk.LEFT, padx=5)
        
        # Set an initial value (now self.value_label exists)
        self.set_value(0) 

    def draw_gauge(self):
        # Adjust vertical positioning
        y_center_bar = self.height / 2 + 5 # Slightly shifted down for better visual balance
        y_top = y_center_bar - 20
        y_bottom = y_center_bar + 20
        text_label_y = y_bottom + 15 # Position for numerical labels

        # Draw main title
        self.canvas.create_text(self.width / 2, 25, text="Stock Market Feeling (IBM)", font=("Arial", 14, "bold"), fill="#333333")


        # Draw colored sections and their internal text labels
        for name, (start_val, end_val, color) in self.ranges.items():
            x1 = self._value_to_x(start_val)
            x2 = self._value_to_x(end_val)
            self.canvas.create_rectangle(x1, y_top, x2, y_bottom, fill=color, outline=color, width=1) # Added outline for crispness
            
            # Add text labels *inside* the sections
            center_x = (x1 + x2) / 2
            # Use 'fill="white"' for better contrast on darker colors, 'black' for lighter
            text_color = "white"
            self.canvas.create_text(center_x, y_center_bar, text=name.replace("_", " "), 
                                    font=("Arial", 9, "bold"), fill=text_color)


        # Draw value labels (e.g., -0.5, -0.35)
        for val, text in self.labels.items():
            x = self._value_to_x(val)
            self.canvas.create_text(x, text_label_y, text=text, font=("Arial", 9), fill="#555555")
            self.canvas.create_line(x, y_bottom, x, y_bottom + 5, fill="#555555") # Small ticks


    def _value_to_x(self, value):
        # Maps a given value from min_val/max_val range to canvas X coordinate
        range_val = self.max_val - self.min_val
        normalized_val = (value - self.min_val) / range_val
        x = normalized_val * self.width
        return x

    def set_value(self, value):
        # Clear previous arrow, text, and background rectangle
        if self.arrow_id:
            self.canvas.delete(self.arrow_id)
        if self.value_text_id:
            self.canvas.delete(self.value_text_id)
        if self.value_bg_rect_id:
            self.canvas.delete(self.value_bg_rect_id)

        # Calculate arrow position
        arrow_x = self._value_to_x(value)
        arrow_y_top = self.height / 2 + 30 # Adjust vertical position to be below labels
        arrow_y_bottom = arrow_y_top + 15
        arrow_base_width = 10

        # Draw the arrow (a polygon for the triangle)
        self.arrow_id = self.canvas.create_polygon(
            arrow_x, arrow_y_bottom,
            arrow_x - arrow_base_width, arrow_y_top,
            arrow_x + arrow_base_width, arrow_y_top,
            fill="black", outline="black"
        )

        # Draw the value text (e.g., "0.2")
        # Temporarily create text with default color to get its bounding box
        # Position the text slightly above the arrow point, or below based on preference
        text_pos_y = arrow_y_bottom + 15 # Below the arrow
        
        temp_text_id = self.canvas.create_text(
            arrow_x, text_pos_y,
            text=f"{value:.1f}", # Format to one decimal place
            font=("Arial", 10, "bold"),
            fill="white" # Initial text color for the actual visible text
        )
        self.master.update_idletasks() # Ensure the canvas updates so bbox is accurate

        # Get text bounding box
        bbox = self.canvas.bbox(temp_text_id)
        
        if bbox:
            # Calculate padding for the background rectangle
            padding_x = 7
            padding_y = 3   
            rect_x1 = bbox[0] - padding_x
            rect_y1 = bbox[1] - padding_y
            rect_x2 = bbox[2] + padding_x
            rect_y2 = bbox[3] + padding_y
            
            # Create the black background rectangle
            self.value_bg_rect_id = self.canvas.create_rectangle(
                rect_x1, rect_y1, rect_x2, rect_y2,
                fill="black", outline="black", width=1
            )
            
            # Now, delete the temporary text and recreate the actual one on top
            self.canvas.delete(temp_text_id)
            self.value_text_id = self.canvas.create_text(
                arrow_x, text_pos_y,
                text=f"{value:.1f}",
                font=("Arial", 10, "bold"),
                fill="white"
            )
            
            # Ensure the text is on top of the rectangle
            self.canvas.tag_raise(self.value_text_id, self.value_bg_rect_id)
        else:
            # Fallback if bbox somehow fails (shouldn't happen often)
            self.value_text_id = self.canvas.create_text(
                arrow_x, text_pos_y,
                text=f"{value:.1f}",
                font=("Arial", 10, "bold"),
                fill="white"
            )

def clean_temp_files(root, folder):
    """
    Limpia el contenido de una carpeta especificada y luego cierra la aplicación.
    """
    print(f"Iniciando limpieza de la carpeta: {folder}")
    
    # Verifica si la carpeta existe para evitar errores
    if os.path.exists(folder):
        # Itera sobre todos los archivos y subcarpetas dentro del directorio
        for nombre_archivo in os.listdir(folder):
            ruta_archivo = os.path.join(folder, nombre_archivo)
            try:
                # Si es un archivo, lo elimina
                if os.path.isfile(ruta_archivo) or os.path.islink(ruta_archivo):
                    os.unlink(ruta_archivo)
                # Si es una subcarpeta, la elimina con todo su contenido
                elif os.path.isdir(ruta_archivo):
                    shutil.rmtree(ruta_archivo)
            except Exception as e:
                print(f"Error al eliminar {ruta_archivo}. Razón: {e}")
        print("Limpieza completada.")
    else:
        print(f"La carpeta '{folder}' no existe, no se necesita limpieza.")
        
    # Cierra la ventana principal de Tkinter
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Market Feeling Gauge")

    gauge = StockMarketFeelingGauge(root)
    gauge.set_value(0.2)  # Set an initial value for demonstration

    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Suponiendo que las imágenes se guardan en la misma carpeta que el script de Docs.py
    carpeta_temp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "DOCS", "temp")

    # Asocia la función de limpieza al botón de cierre de la ventana (la 'X')
    # Usamos una lambda para pasar argumentos a nuestra función
    root.protocol("WM_DELETE_WINDOW", lambda: clean_temp_files(root, carpeta_temp))

    root.mainloop()