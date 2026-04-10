import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV
df = pd.read_csv("Exploracion_Data_Titanic/titanic_data/train.csv")

# Mostrar las columnas del CSV
print(df.columns)

# Mostrar las primeras filas
print(df.head())

# Filtrar las personas que no sobrevivieron (Survived == 0)
df_muertos = df[df['Survived'] == 0]

# Crear un gráfico básico de barras con seaborn
sns.countplot(data=df_muertos, x='Sex')
plt.title('Muertes por Sexo')
plt.show()
