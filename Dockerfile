# Usa una imagen base ligera de Python
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt primero e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de tu aplicaciónxfcsdfdsfdsfsxfgdgjsjdrertyu
COPY . .

# Define el comando por defecto que se ejecutará al iniciar el contenedor
CMD ["python", "main.py"]