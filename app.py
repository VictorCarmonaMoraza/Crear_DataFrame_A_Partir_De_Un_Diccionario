import pandas as pd
import os


info_pais ={"pais": ["Brasil", "Mexico", "Argentina", "Chile", "Colombia", "Peru"],
            "capital": ["Brasilia", "Mexico City", "Buenos Aires", "Santiago", "Bogota", "Lima"],
            "superficie (MKm2)": [8.5, 1.9, 2.8, 0.8, 1.1, 1.3]}


# Convert the dictionary to a DataFrame
df = pd.DataFrame(info_pais)

# Ver las primera filas del DataFrame
print(df.head())

# Ver las dimensiones del DataFrame
print(df.shape)

# Ver el tipo de datos de cada columna
print(df.dtypes)

# Ver las estadisticas del DataFrame
print(df.describe())

#uta exportacion Dataframe
ruta_export = 'C:/Users/Victo/Desktop/DataCience/CreacionDataframeAPartirDeDiccionario/exportaciones'
nombre_archivo = "info_pais.csv"
ruta_completa = os.path.join(ruta_export, nombre_archivo)
#Exportar el DataFrame a un archivo CSV
df.to_csv(ruta_completa, sep=',', encoding='utf-8', index=True)