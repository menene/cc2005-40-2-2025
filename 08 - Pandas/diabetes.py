import pandas as pd
import matplotlib.pyplot as plt

"""## Leer del archivo CSV (dataset)"""

df = pd.read_csv("diabetes.csv")

"""## Verificar la forma de los datos"""

df.shape

"""## Imprimir el DataFrame"""

df

"""## Análisis exploratorio
Primero veamos qué factores están presentes en las mujeres con diabetes:
"""

positivas = df.loc[df["Outcome"] == 1]
positivas.describe()

"""### Promedio de factores para mujeres con diabetes"""

positivas[
    ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
].mean()

"""## Pacientes negativas con alto riesgo"""

riesgo = df.loc[
    (df["Outcome"] == 0)
    & (df["Glucose"] >= 141)
    & (df["Insulin"] >= 100)
    & (df["BloodPressure"] >= 70)
    & (df["BMI"] >= 35)
]
riesgo

riesgo.describe()

"""## Agregar columna de factores"""

df["Factors"] = df["Glucose"] + df["Insulin"] + df["BloodPressure"] + df["BMI"]

df

"""## Análisis de la columna Factors"""

df[["Factors"]].describe()

"""## Calcular riesgo basado en Factors"""


def calculate_risk(factor):
    if factor >= 200:
        return "High"
    else:
        return "Low"


df["Risk"] = df["Factors"].apply(calculate_risk)

df

"""## Análisis de falsos positivos"""

falsos_positivos = df.loc[(df["Outcome"] == 1) & (df["Risk"] == "Low")]
falsos_positivos.shape

"""## Guardar el nuevo archivo CSV"""

df.to_csv("diabetes_new.csv", index=False)

"""## Análisis de relación entre embarazos y diabetes"""

preg_diabetes = df.groupby("Pregnancies")["Outcome"].value_counts()
preg_diabetes

preg_diabetes = preg_diabetes.unstack()
preg_diabetes

preg_diabetes.plot(
    kind="bar",
    title="Cantidad de embarazos vs Diabetes",
    grid=True,
    stacked=False,
    rot=0,
)
plt.legend(title="Dx Diabetes", loc="upper right")
plt.xlabel("Embarazos")
plt.ylabel("Mujeres")
plt.show()
