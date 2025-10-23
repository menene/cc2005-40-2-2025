import pandas as pd

df = pd.DataFrame({
    "Carnet": [123, 456, 789, 987, 654],
    "Hoja de trabajo 1": [80, 85, 75, 40, 100],
    "Hoja de trabajo 2": [90, 90, 75, 61, 100],
    "Hoja de trabajo 3": [80, 80, 0, 50, 85],
})

print(df)

print(df.shape)

print(df.describe())

print(df["Hoja de trabajo 1"])

print(df["Hoja de trabajo 1"].mean())

df2 = df[["Hoja de trabajo 1", "Hoja de trabajo 3"]]
 
print(df2)
 
print(df2.shape)

valor = df["Hoja de trabajo 1"][0]
 
print(valor)
