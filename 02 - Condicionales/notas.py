
calificacion = int(input("Ingresa tu nota: "))
asistencia = int(input("Ingresa tu asistencia: "))

# no anidado

if (calificacion >= 61 and asistencia >= 80):
    print("Ganaste 👩🏼‍🎓")
    
    if calificacion >= 90:
        print("Mención honorifica 🧠")
        
    if calificacion == 100:
        print("Calificación perfecta 🤓")
        
else:
    print("Perdiste 😭")
    
    
if asistencia == 100:
        print("Asistencia perfecta ♥️")