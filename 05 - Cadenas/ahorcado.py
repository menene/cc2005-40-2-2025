
palabra_secreta = input("Ingrese una palabra para el jugador 2: ")
palabra_secreta = palabra_secreta.upper()

max_intentos = 6
intentos_fallidos = 0
largo_palabra = len(palabra_secreta)

if palabra_secreta.isalpha():
        palabra_oculta = "*" * len(palabra_secreta)
        
else:
    palabra_oculta = ""
    
    for letra in palabra_secreta:
        if letra.isalpha():
            palabra_oculta = palabra_oculta + "*"
        else:
            palabra_oculta = palabra_oculta + " "


jugar = True

while jugar:
    
    cumple = False
    while not cumple:
        letra = input("Ingrese una letra: ")
        letra = letra.upper()
        
        if letra.isalpha() and len(letra) == 1:
            cumple = True

    valida = False
    if letra in palabra_secreta:
        valida = True
    

    if valida:
        tmp = ""
        
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                tmp = tmp + letra
                
            else:
                tmp = tmp + palabra_oculta[i]
                
        palabra_oculta = tmp
        
    else:
        intentos_fallidos = intentos_fallidos + 1
        
    print(palabra_oculta)
        
    if intentos_fallidos >= max_intentos:
        print("PERDISTE!!!")
        print("La palabra era:", palabra_secreta)
        jugar = False
        
    else:
        if palabra_secreta == palabra_oculta:
            print("GANSTE!!!")
            jugar = False
                




