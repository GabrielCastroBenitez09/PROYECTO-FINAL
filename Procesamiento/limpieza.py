#   Librerias
import pandas as pd
from pathlib import Path


#   Datos
BASE_DIR = Path(__file__).resolve().parent.parent
ruta_archivo = BASE_DIR / 'Datos' / 'diagnostico_raw.csv'
datos = pd.read_csv(ruta_archivo)


#   Tratamiento de valores vaciós
datos['valor'] = pd.to_numeric(datos['valor'], errors = 'coerce')


#   Datos estructurados
datos_estructurados = datos.pivot_table(
    index=['pais', 'año'],
    columns='indicador',
    values='valor'
).reset_index()

#   Configuraciones de la base de datos
datos_estructurados.columns.name = None
datos_estructurados = datos_estructurados.sort_values(by = ['pais', 'año'])     # Ordenar los datos


#   Guardado  
ruta_salida = BASE_DIR / 'Datos' / 'diagnostico_limpio.csv'     # Ruta de guardado
datos_estructurados.to_csv(ruta_salida, index = False)  
print("Limpieza completada!")
