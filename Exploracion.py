import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Exploracion_Data_Titanic/titanic_data/train.csv")

print(df.columns)

print(df.head())

df_muertos = df[df['Survived'] == 0]
df_sobrevivientes = df[df['Survived'] == 1]

sns.countplot(data=df_muertos, x='Sex')
plt.title('Muertes por Sexo')
plt.show()

sns.countplot(data=df_muertos, x="Sex", hue= "Pclass")
plt.title("Muertes por Clase") 
plt.show()

sns.histplot(data=df_muertos, x="Age", hue="Survived")
plt.title("Muertes por Edad") 
plt.show()

sns.histplot(data=df_sobrevivientes, x="Age", hue="Survived")
plt.title("Sobrevivientes por Edad") 
plt.show()

