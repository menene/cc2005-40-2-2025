import pandas as pd
import os
 
path = os.getcwd()
 
file = path + "/Housing.csv"
 
datos = pd.read_csv(file)
 
print(datos.describe())

print(datos['basement'])


print(datos.loc[(datos['parking'] >= 3) & (datos['bedrooms'] > 3) & (datos['price'] <= 9000000)])



