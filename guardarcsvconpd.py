import pandas as pd

datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 34, 45]
}
df = pd.DataFrame(datos)

df.to_csv('archivo.csv', index=False)  # index=False evita guardar el índice como una columna