# Proyecto-POO

## Diagrama de clases:

```mermaid
---
config:
  theme: 'base'
  themeVariables:
    primaryColor: '#BB2528'
    primaryTextColor: '#fff'
    primaryBorderColor: '#7C0000'
    lineColor: '#F8B229'
    secondaryColor: '#006100'
    tertiaryColor: '#fff'
---
classDiagram

    class Interface {
        +CodeInput input
        +CodeInput compare
        +ttk.Button compare_button
        +__init__()
    }

    class CodeInput {
        +Interface parent
        +ttk.Label label
        +ttk.Entry ticker_entry
        +ttk.Entry exchange_entry
        +ttk.Button button
        +ttk.Label missing_code
        +__init__()
        +get_codes()
        -create_info_page(data : dict) 
        -process_data()
    }

class Scraper {
        +dict headers
        +list main_data_keys
        +str stock
        +str exchange
        +__init__(stock: str, exchange: str)
        +get_info() dict
        - get_chart_data()
        - get_text_from_html_list(list_: list) dict
        - request_data(url: str) requests.Response | None
    }

    class DataPage {
        +CodeInput parent
        +ttk.Label data_label
        +ttk.Button clear_button
        +ttk.Button pdf_button
        +CreatePDF pdf_create
        +__init__(Data)
        +clear_page()
        -create_compare_page()
    }

    class CreatePDF {
        +__init__(data : dict)
        +to_pdf()
    }

    class ComparePage {
        + __init__()
        + compare_stocks()
    }

    Interface "1" *-- "2" CodeInput: contains
    
    Interface --|> tk.Tk
    CodeInput --> Scraper: uses
    CodeInput *-- DataPage: creates
    DataPage --> CreatePDF: uses
    CodeInput --|> ttk.Frame
    ComparePage --|> DataPage
    DataPage --|> ttk.Frame
    ComparePage --* Interface

```

Hola geis, aqui una git guia (guita):

## Antes de empezar:

Hagan pull antes de empezar, asi si alguien cambió algo cuando no estaban,
actualizan su repositorio local y evitan encontrar conflictos cuando suben los
cambios. Comando:

```
git pull origin main
```

## Cada q terminen una caracteristica o quieran crear un "punto de guardado":

Cuando cambien cosas van a haber cambios sin guardar en el repo asi hayan
guardado el archivo, el guardado de archivos en el PC, guardado en el repo
local, y guardado en el repo remoto son cosas ditintas. tienen q hacer cada
una, para registrar los cambios en el local:

si crearon o borraron archivos:

```
git add .
git commit -a -m "mensaje descriptivo para el commit"
```

si solo modificaron:

```
git commit -a -m "mensaje descriptivo para el commit"
```

## Al terminar:

Cuando terminen de trabajar, tienen q subir sus cambios (su lista de commits
realizados) al repositorio remoto para que otros los puedan ver y usar, para
esto se hace push, esto lo q hace es añadir todos los commits realizados en
local a la lista de commits del repo remoto. Antes de hacer push asegurense
de hacer commit en todos sus cambios.

```
git push origin main
```
