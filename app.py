import pandas as pd


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