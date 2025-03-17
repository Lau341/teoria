# Actividad:
## ¿Como abrir un csv con python utilizando la libreria pandas?
## Respuesta:
#### ¿Cómo abrir un archivo CSV con Python utilizando la librería Pandas?

**Pandas** hace que trabajar con archivos CSV sea muy sencillo. Puedes utilizar la función `pd.read_csv()` para cargar los datos de un archivo CSV en un **DataFrame**, que es la estructura de datos tabular de Pandas.

##### Pasos para abrir un archivo CSV:

### 1. **Instalar Pandas** (si no lo tienes instalado)
Si aún no tienes Pandas instalado, puedes hacerlo ejecutando el siguiente comando en la terminal o línea de comandos:

```bash
pip install pandas
```

### 2. **Abrir un archivo CSV con Pandas**

Una vez que tengas Pandas instalado, puedes usar la función `pd.read_csv()` para leer el archivo CSV. Aquí tienes un ejemplo básico:

```python
import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('ruta/del/archivo.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())
```

En este ejemplo:
- `'ruta/del/archivo.csv'` es la ruta del archivo CSV que deseas abrir. Puedes usar una ruta relativa o absoluta dependiendo de donde se encuentre el archivo.
- `df.head()` muestra las primeras 5 filas del DataFrame cargado (esto es útil para verificar rápidamente el contenido del archivo).

### 3. **Leer un archivo CSV con delimitadores diferentes (si es necesario)**

Si el archivo CSV usa un delimitador diferente a la coma (por ejemplo, un punto y coma `;`), puedes especificar el delimitador en el parámetro `sep`:

```python
df = pd.read_csv('archivo.csv', sep=';')
```

### 4. **Leer un archivo CSV desde una URL**

También puedes leer un archivo CSV directamente desde una URL:

```python
url = 'https://ruta/del/archivo.csv'
df = pd.read_csv(url)
print(df.head())
```

### 5. **Manejo de valores faltantes**

Pandas tiene herramientas integradas para manejar valores faltantes. Por ejemplo, puedes especificar un valor que debe ser tratado como "nulo" al leer el archivo:

```python
df = pd.read_csv('archivo.csv', na_values=['NA', 'N/A', 'null'])
```

### 6. **Verificar el DataFrame**

Una vez que hayas cargado el CSV en un DataFrame, puedes usar varios métodos de Pandas para inspeccionar y manipular los datos:

- **Mostrar las primeras filas**: `df.head()`
- **Obtener la información del DataFrame**: `df.info()`
- **Verificar estadísticas descriptivas**: `df.describe()`

## Resumen

Para abrir un archivo CSV con Pandas, solo necesitas usar `pd.read_csv('ruta/del/archivo.csv')`. Aquí tienes un ejemplo básico de cómo hacerlo:

```python
import pandas as pd
df = pd.read_csv('archivo.csv')
print(df.head())
```
