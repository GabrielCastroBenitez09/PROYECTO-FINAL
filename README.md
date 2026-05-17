# PROYECTO FINAL
### Gabriel Hernan Castro Benitez

<br>

> Introducción a la Economía
>
> Pregrado en Ciencia de Datos - Universidad Externado de Colombia

## Descripción
Diagnóstico macroeconómico de cuatro paises latinoamericanos:
- Brasil
- Chile
- Colombia
- Uruguay

mediante análisis de indicadores macroeconomicós relevantes:
- PIB per cápita
- Crecimiento del PIB
- Inflación
- Desempleo
- Apertura Comercial

## Estructura del Repositorio
```text
PROYECTO FINAL/
│
├── Datos/
│   ├── diagnostico_raw.csv
│   └── diagnostico_limpio.csv
│
├── Procesamiento/
│   ├── extraccion.py
│   └── limpieza.py
│
├── Visualizacion/
│   └── graficos.py
│
├── Informe.pdf
│
└── README.md
```

### Datos
Contiene las bases de datos generadas por `extraccion.py` y `limpieza.py`:
- **diagnostico_raw.csv:** Conjunto con los datos crudos organizados
  
| columna | descripción |
|---|---|
| pais | Código ISO3 del país |
| año | Año de observación |
| indicador | Nombre del indicador macroeconómico |
| valor | Valor del indicador |


- **diagnostico_limpio.csv:** Base de datos limpia y organizada
  
| columna | descripción |
|---|---|
| pais | Código ISO3 del país |
| año | Año de observación |
| apertura_comercial | Comercio total como % del PIB |
| crecimiento_pib | Crecimiento anual del PIB (%) |
| desempleo | Tasa de desempleo (%) |
| inflacion | Inflación anual (%) |
| pib_per_capita | PIB per cápita en USD constantes |

### Procesamiento
Contiene los scripts:
- **extraccion.py:** Script que descarga los datos de cada país por indicador, directamente desde la API del Banco Mundial. Genera además un archivo `csv` con los datos crudos.
- **limpieza.py:** Script de limpieza de los datos. Controla celdas vacías, organiza los datos de acuerdo al país y año, y genera un archivo `csv` estructurado para análisis.

### Visualización
Contienen un cuaderno de visualizaciones:
- **graficos.ipynb:** Notebook con los gráficos diagnósticos por país, y los gráficos comparativos entre países de cada indicador.

### Informe
Informe ejecutivo ____
