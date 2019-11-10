# Importando las librerías
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# Parámetros
page_link = 'https://www.pccomponentes.com/'
tipo_productos = ['smartphone-moviles', 'portatiles', 'portatiles-gaming', 'televisores']

# Llamada con requests:
textContent = []
n_articulos_cuenta = []

for i in tipo_productos: 
    page_response = requests.get(page_link + i, timeout = 5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    n_articulos = page_content.text.count('article') // 2
    n_articulos_cuenta.append(n_articulos)
    
    for j in range(0, n_articulos):
        paragraphs = page_content.find_all("article")[j]
        textContent.append(paragraphs)
   

 # Escogemos la información necesaria: 
export_data = []
columnas = ['Categoría', 'Marca', 'Nombre', 'Precio']
for i in range(np.sum(n_articulos_cuenta)):
    x1 = textContent[i]['data-category']
    x2 = textContent[i]['data-brand']
    x3 = textContent[i]['data-name']
    x4 = textContent[i]['data-price']
    export_data.append([x1, x2, x3, x4])
    
# Creamos el dataset:
df_catalogo = pd.DataFrame(export_data, columns = columnas)

# Exportamos
df_catalogo.to_csv('../data/pccomponentes_catalogo.csv')