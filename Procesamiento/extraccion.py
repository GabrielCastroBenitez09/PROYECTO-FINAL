#   Librerias 
import time
import requests
import pandas as pd
from pathlib import Path


#   Países e Indicadores
PAISES = ['BRA', 'CHL', 'COL', 'URY']

INDICADORES = {
    'pib_per_capita':'NY.GDP.PCAP.KD',
    'crecimiento_pib':'NY.GDP.MKTP.KD.ZG',
    'inflacion':'FP.CPI.TOTL.ZG',
    'desempleo':'SL.UEM.TOTL.ZS',
    'apertura_comercial':'NE.TRD.GNFS.ZS'
    }

AÑO_INICIO, AÑO_FIN = 2018, 2025


#   Extracción
def extraer_datos (pais:str, indicador:str, inicio:int, fin:int):
    """
    Extrae los datos de un país e indicador desde la API del Banco Mundial en un rango de años.

    Parámetro:
        pais (string): Código ISO3 del país.
        indicador (string): Indicador macroeconómico.
        inicio (int): Año inicial.
        fin (int): Año final.

    Retorno:
        dict: Diccionario {año: valor}
    """
    #   URL
    url = f'https://api.worldbank.org/v2/country/{pais}/indicator/{indicador}?date={inicio}:{fin}&format=json&per_page=100'
    
    #   Petición
    r = requests.get(url, timeout=20)
    r.raise_for_status()    # Verificación de petición exitosa

    data = r.json()
    if len(data) < 2 or not data[1]:
        return {}   # Retorna diccionario vacío si no hay datos
    
    return {int(d['date']): d['value'] for d in data[1] if d['value'] is not None}


#   Descarga
datos = []
for pais in PAISES :
    for indicador, codigo in INDICADORES.items() :
        print(f"Extrayendo {indicador} para {pais}... ")
        resultados = extraer_datos(pais, codigo, AÑO_INICIO, AÑO_FIN)
        for año, valor in resultados.items():
            datos.append({
                'pais': pais,
                'indicador': indicador,
                'año': año,
                'valor': valor
            })
        time.sleep(0.5)


#   Guardado
df = pd.DataFrame(datos)
BASE_DIR = Path(__file__).resolve().parent.parent   
ruta_salida = BASE_DIR / 'Datos' / 'diagnostico_raw.csv'    # Ruta de guardado
df.to_csv(ruta_salida, index = False)
print("Extracción completada!")




