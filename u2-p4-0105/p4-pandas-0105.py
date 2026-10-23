import pandas as pd
import numpy as np
## Iker Montoya NC 0105
n_filas = 5
n_columna = 5
tag_columna= tuple("ABCDE")#etiquetas para las columnas de una tapla 
print(tag_columna)
matriz = np.random.randint(1, 6, size=(n_filas, n_columna))
print("Genera matriz de 5 filas por 5 columnas ")
print("con numeros aleatorios comprendidos entre 1 y 10  ")
print(matriz)
# la variable  df es dataframe 
df = pd.DataFrame(matriz, columns = tag_columna)
print("---la tabla o datframe---- NC = 0105 ") 
print(df)
print("Iker Montoya NC 0105")