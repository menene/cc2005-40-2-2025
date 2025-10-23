
def promedio(lista_notas):
    
    if len(lista_notas) == 0:
        return 0
    
    suma = 0
    for nota in lista_notas:
        suma = suma + nota
        
    return suma / len(lista_notas)


# estudiante = {
#     "nombre": "Erick Marroquin",
#     "carnet": "12345",
#     "notas": [100, 90, 80, 79, 70]
# }
# 
# 
# print("promedio", promedio(estudiante["notas"]))
# print("promedio", promedio([1,2,3]))

# seccion40 = [
#     {"carnet": "123", "nombre": "Erick", "notas": [100, 90, 89, 90, 90, 100, 70]},
#     {"carnet": "456", "nombre": "Maria", "notas": [89, 80, 89]},
#     {"carnet": "789", "nombre": "Pedro", "notas": [100, 100, 100]}
# ]

# print(seccion40[0]["notas"])

# promedios = []
# 
# for estudiante in seccion40:
#     p = promedio(estudiante["notas"])
#     print("Promedio de", estudiante["nombre"], ":", p)
#     promedios.append(p)
#     
# promedio_general = promedio(promedios)
# 
# print("Promedio general", promedio_general)
# 
# 
# 
# 
# carnet = input("Ingrese el carnet para consultar: ")
# 
# for e in seccion40:
#     if e["carnet"] == carnet:
#         p = promedio(e["notas"])
#         print("Promedio de", e["nombre"], ":", p)



seccion40 = {
    "123": {"nombre": "Erick", "notas": [100, 100, 100]},
    "456": {"nombre": "Maria", "notas": [90, 80, 70]},
}

print(seccion40["123"])











