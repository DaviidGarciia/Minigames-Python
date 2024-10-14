import random


partida = 0
usuario = 0
maquina = 0
empate = 0
print("""
     *******************************************************************                        
    *                                                                   *            (\__/)
    *    Bienvenido a Piedra, Papel o Tijera !!, vamos a jugar un BO3   *           ( • . •)                   
    *                                                                   *            />  💖
     *******************************************************************  
    """
    )
while partida <= 2:  
    numero_aleatorio = random.randint(1, 3)
    nombrePpt = ""
    if numero_aleatorio == 1:
        nombrePpt = "Piedra"
    elif numero_aleatorio == 2:
        nombrePpt= "Papel"
    elif numero_aleatorio == 3:
        nombrePpt= "Tijera"
    eleccion = input("Elija entre piedra,papel o tijera: ").lower().strip()
    print("\n")
    datoCorrecto = True

    if eleccion == "piedra" and nombrePpt == "Piedra":
        print(f"Empate, {eleccion} empata contra {nombrePpt} 😕 \n")
        empate +=1
        partida +=1
    elif eleccion == "piedra" and nombrePpt == "Papel":
        print(f"Has perdido, {eleccion} pierde contra {nombrePpt} 😭 \n")
        maquina += 1
        partida +=1
    elif eleccion == "piedra" and nombrePpt == "Tijera":
        print(f"Has ganado!! {eleccion} gana contra {nombrePpt} 🥳 \n")
        usuario += 1
        partida +=1
    elif eleccion == "papel" and nombrePpt == "Piedra":
        print(f"Has ganado!! {eleccion} gana contra {nombrePpt} 🥳 \n")
        usuario += 1
        partida +=1
    elif eleccion == "papel" and nombrePpt == "Papel": 
        print(f"Empate, {eleccion} empata contra {nombrePpt} 😕 \n")
        empate += 1
        partida +=1
    elif eleccion == "papel" and nombrePpt == "Tijera": 
        print(f"Has perdido, {eleccion} pierde contra {nombrePpt} 😭 \n")
        maquina +=1
        partida +=1
    elif eleccion=="tijera" and nombrePpt == "Piedra":
        print(f"Has perdido, {eleccion} pierde contra {nombrePpt} 😭 \n")
        maquina += 1
        partida +=1
    elif eleccion=="tijera" and nombrePpt == "Papel":
        print(f"Has ganado!! {eleccion} gana contra {nombrePpt} 🥳 \n")
        usuario += 1
        partida +=1
    elif eleccion=="tijera" and nombrePpt == "Tijera":
        print(f"Empate, {eleccion} empata contra {nombrePpt} 😕 \n")
        empate += 1
        partida +=1
    else:
        print(f"Tienes que elegir entre piedra, papel o tijera, {eleccion} no es válido \n")
        datoCorrecto=False
    
    while datoCorrecto == True:
        estadistica =input("Quieres ver las estadisticas? (Si o no): ").lower().strip()
        print("\n")
        if estadistica == "si":
            print(f"""
        ******************************************************************
                              Victorias: {usuario}\n                      
                              Derrotas:  {maquina}\n                       
                              Empates:   {empate}                       
        ******************************************************************
                     
                                               
            """)
            datoCorrecto=False  
        elif estadistica=="no":
            print("Seguimos jugando \n")
            datoCorrecto=False  
        else:
            print(f"Tienes que elegir entre si o no, {estadistica} no es un valor válido \n")

print("""
     *******************************************************************                        
    *                                                                   *            
    *                 Gracias por jugar con nosotros!!                  *                             
    *                                                                   *            
     *******************************************************************  
                      (\__/)       * *     *   *     *
                     ( • . •)      *  *      *       *
                     />  💖        * *       *     * * 
""")