import asyncio
from playwright.async_api import async_playwright

async def capture_chart():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)  # Primero prueba en modo visible
            page = await browser.new_page()
            
            # Configurar User-Agent y viewport
            await page.set_viewport_size({"width": 1280, "height": 800})
            await page.set_extra_http_headers({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            })
            
            # Navegar a Google Finance directamente (más confiable)
            await page.goto('https://www.google.com/finance/quote/KOF:NYSE', wait_until='networkidle', timeout=60000)
            
            # Esperar alternativamente por estos selectores
            selectors = [
                'div.knowledge-finance-wholepage-chart__container',  # Selector nuevo
                'div.uch-path',  # Selector del SVG
                'canvas',  # Canvas alternativo
                'div[aria-label="Gráfico de precios"]'  # Por accesibilidad
            ]
            
            found = False
            for selector in selectors:
                try:
                    chart = await page.wait_for_selector(selector, timeout=10000)
                    found = True
                    break
                except:
                    continue
            
            if not found:
                raise Exception("No se pudo encontrar el gráfico")
            
            # Scroll y espera adicional
            await chart.scroll_into_view_if_needed()
            await page.wait_for_timeout(2000)  # Espera para renderizado
            
            # Capturar solo el gráfico
            await chart.screenshot(
                path='kof_chart.png',
                type='png',
                quality=100
            )
            
            return True
            
    except Exception as e:
        print(f"Error: {str(e)}")
        # Guardar screenshot de diagnóstico
        await page.screenshot(path='error_debug.png')
        return False
    finally:
        await browser.close()

# Ejecutar
result = asyncio.run(capture_chart())
print("Captura completada:", result)