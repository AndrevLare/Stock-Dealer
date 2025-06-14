from bs4 import BeautifulSoup
import requests

# 1. Obtener HTML
url = "https://ejemplo.com"
html = requests.get(url).text

# 2. Crear el objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 3. Extraer datos
titulos = [h1.text for h1 in soup.find_all('h1')]
enlaces = [a['href'] for a in soup.find_all('a', href=True)]