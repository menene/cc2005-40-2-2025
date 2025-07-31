
dia = int(input("Ingresa el día (1 = lunes, 2 = martes, ...): "))
hora = float(input("Ingrese la hora: "))

# anidada

if dia == 4:
    
    if hora >= 10.40:
        
        if hora <= 12.15:
            print("Voy a clase")
            
        else:
            print("No voy a clase")
    
    else:
        print("No voy a clase")
    
else:
    print("No voy a clase")

#no anidada

if (dia == 4 and (hora >= 10.40 and hora <= 12.15)):
    print("Voy a clase")
    
else:
    print("No voy a clase")






