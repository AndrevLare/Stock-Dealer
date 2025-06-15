# Import neccesary liraries
from datetime import datetime
from urllib.robotparser import RobotFileParser
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import requests

#Class Scrapper
class Scraper():
    # Class attribute with headers for the get request, to protect the IP from get banned
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml',
        'Referer': 'https://www.google.com/'
    }
    main_data_keys = ["previous_close", "day_range", "year_range", "market_cap", "average_volume", "primary_exchange", "ceo", "founded", "website", "employees"]

    # Defines the attributes stock and exchange for the instance
    def __init__(self, stock, exchange):
        self.stock = stock
        self.exchange = exchange

    # Calls the request and organize and return the wanted data
    def get_info(self)->dict:
        response = self.__request_data__(f"https://www.google.com/finance/quote/{self.stock}:{self.exchange}?") # request the data
        soup = BeautifulSoup(response.text, "html.parser") # with bs4 organize the data
        # Diccionary with the return data
        try:
            data = {
            "name": soup.find(class_="zzDege").text,
            "about": soup.find(class_ = "bLLb2d").text,
            "stock": self.stock,
            "time" : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "current_value" : soup.find(class_="YMlKec fxKbKc").text,
            "graph": self.__get_chart_data__("1d")["xml"]
            }
            data.update(self.__get_text_from_html_list__(soup.find_all(class_="P6K39c")))
        except Exception as e:
            print(f"Error al obtener los datos: {e}")
            return None
        return data
    def __get_text_from_html_list__(self, list:list)->dict:
        output = {}
        for i, e in enumerate(list):
            output[self.main_data_keys[i]] = e.text
        return output

    def __request_data__(self, url)-> requests.Response | None:
        html = requests.get(url).text
        for i in range(5):
            # Random sleepTime from 0.5 to 2 seconds
            delay = random.uniform(0.5, 2)
            print(f"Esperando {delay:.2f} segundos...")
            time.sleep(delay)
            try:
                response = requests.get(url, headers=self.headers)
                print("response status:", response.status_code)
                if response.status_code == 200:
                    print("returning:", response)
                    return response
                elif response.status_code == 429:  # Too Many Requests
                    wait_time = (delay * i)
                    print(f"Rate limited. Esperando {wait_time} minutos...")
                    time.sleep(wait_time)
                else:
                    print(f"Error: Status code {response.status_code}")
            except Exception as e:
                print(f"Error en la solicitud: {e}")
                return None
        print("Se excedió el número máximo de reintentos")
        return None
    def __get_chart_data__(self, time_range="1d"):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

        try:
            url = f"https://www.google.com/search?q={self.exchange}%3A{self.stock}"
            driver.get(url)

            # Cambiar al iframe si existe (el gráfico a veces está en un iframe)
            try:
                iframes = driver.find_elements(By.TAG_NAME, "iframe")
                if iframes:
                    driver.switch_to.frame(iframes[0])
            except:
                pass

            # Esperar a que el gráfico esté completamente cargado
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.uch-path"))
            )

            # Mapeo de intervalos de tiempo
            time_range_map = {
                "1d": "1D",
                "1m": "1M",
                "6m": "6M",
                "1y": "1Y",
                "max": "Max"
            }

            # Cambiar el intervalo de tiempo si no es el predeterminado (1D)
            if time_range != "1d":
                target_range = time_range_map.get(time_range, "1M")

                try:
                    # Buscar y hacer clic en el botón del intervalo deseado
                    range_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((
                            By.XPATH, f"//div[@role='button' and .//div[text()='{target_range}']")))
                    range_button.click()

                    # Esperar a que el gráfico se actualice
                    time.sleep(2)  # Espera para la actualización del gráfico
                    WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div.uch-path"))
                    )

                    # Verificar que el botón está seleccionado
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((
                            By.XPATH, f"//div[@role='button' and @aria-selected='true' and .//div[text()='{target_range}']"))
                    )
                except Exception as e:
                    print(f"No se pudo cambiar al intervalo {time_range}: {str(e)}")
                    # Continuar con el gráfico actual si no se puede cambiar

            # Localizar el contenedor padre primero
            chart_container = driver.find_element(By.CSS_SELECTOR, "div.uch-path")

            # Localizar el SVG específico que necesitas
            svg = chart_container.find_element(By.CSS_SELECTOR, "svg.uch-psvg")

            # Extraer toda la información relevante
            svg_data = {
                "xml": svg.get_attribute('outerHTML'),
                "viewBox": svg.get_attribute('viewBox'),
                "size": {
                    "width": svg.get_attribute('width'),
                    "height": svg.get_attribute('height')
                },
                "paths": {
                    "main_path": svg.find_element(By.CSS_SELECTOR, "path.range-normal-line").get_attribute('d'),
                    "secondary_path": svg.find_element(By.CSS_SELECTOR, "path[stroke='#f28b82']").get_attribute('d')
                },
                "gradients": {
                    "fill_gradient": svg.find_element(By.CSS_SELECTOR, "linearGradient[id^='fill-id']").get_attribute('outerHTML'),
                    "chart_gradient": svg.find_element(By.CSS_SELECTOR, "linearGradient[id^='chart-grad']").get_attribute('outerHTML')
                },
                "time_range": time_range  # Guardar el intervalo seleccionado
            }

            return svg_data

        except Exception as e:
            print(f"Error al obtener el gráfico: {str(e)}")
            # Guardar screenshot para diagnóstico
            driver.save_screenshot(f"error_screenshot_{time_range}.png")
            return None
        finally:
            driver.quit()

if __name__ == "__main__":
    # Test
    scrap = Scraper("TTWO", "NASDAQ")
    
    print("\n\n\n\n-------------------------------------\n", scrap.get_info())
