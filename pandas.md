# ¿Qué es Pandas y para qué sirve?

**Pandas** es una biblioteca de código abierto para el lenguaje de programación Python, que ofrece estructuras de datos y herramientas de análisis de datos de alto rendimiento. Está especialmente diseñada para trabajar con datos estructurados, como tablas o bases de datos, de manera eficiente.

## Características principales de Pandas:

1. **Estructuras de datos**:
   - **DataFrame**: Es una estructura de datos bidimensional (como una tabla) que contiene filas y columnas. Es similar a una hoja de cálculo o una tabla de bases de datos.
   - **Series**: Es una estructura unidimensional, similar a un array o una lista, pero con etiquetas (índices) para cada valor.

2. **Facilidad para manejar datos faltantes**: Pandas permite fácilmente identificar y manejar valores faltantes o nulos.

3. **Filtrado y selección de datos**: Proporciona herramientas potentes para filtrar, seleccionar y agrupar datos de manera sencilla.

4. **Operaciones de agregación y transformación**: Permite aplicar funciones matemáticas y estadísticas a los datos, como la suma, la media, el conteo, etc.

5. **Lectura y escritura de datos**: Pandas soporta la lectura y escritura de datos en varios formatos, como CSV, Excel, bases de datos SQL, JSON, entre otros.

## ¿Para qué sirve Pandas?

Pandas se utiliza principalmente para:

- **Análisis de datos**: Permite manipular grandes volúmenes de datos de manera eficiente.
- **Limpieza de datos**: Facilita el proceso de depuración, eliminación de datos duplicados o nulos.
- **Visualización de datos**: Aunque no es una biblioteca de visualización, Pandas se puede integrar con bibliotecas como Matplotlib o Seaborn para crear gráficos.
- **Transformación y manipulación**: Permite modificar, agregar, eliminar, y reorganizar datos fácilmente.
- **Integración con otras herramientas**: Se integra fácilmente con otras bibliotecas como NumPy, Matplotlib, y Scikit-learn para análisis numérico y modelado.

## Ejemplo básico de uso:

```python
import pandas as pd

# Crear un DataFrame
data = {'Nombre': ['Juan', 'María', 'Carlos'],
        'Edad': [28, 35, 40],
        'Profesión': ['Ingeniero', 'Doctora', 'Abogado']}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)
