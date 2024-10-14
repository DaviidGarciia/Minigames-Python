import random
numeroAleatorio = random.randint(0,7)
lista = ["comer","actor","bizco","cabra","cerdo","avion","pipas","llave"]

palabraSecreta = lista[numeroAleatorio]

count = 0
print("""
     *******************************************************************                       
    *                                                                   *            
    *                          Bienvenido a Wordle                      *                            
    *                                                                   *            
     *******************************************************************  
                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                        ░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
                        ░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
                        ░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
                        ░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
                        ░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
                        ░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
                        ░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
                        ░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
                        ░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
                        ░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
                        ░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
                        ░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    """
    )

while count <=5:
    palabraUsuario = input("Adivina la palabra secreta (pista, tiene 5 letras): ")
    print("\n")
    mostrarPalabra = ["❓","❓","❓","❓","❓"]
    palabraU = list(map(lambda x: x,palabraUsuario))
    palabraS = list(map(lambda x: x, palabraSecreta))
    if len(palabraUsuario) != len(palabraSecreta):
        print("No tiene 5 letras, prueba otra vez. \n")
    else:
        count +=1
        if palabraU[0] == palabraS[0]:
            mostrarPalabra[0]=palabraS[0]
        if palabraU[0] == palabraS[1] or palabraU[0] == palabraS[2] or palabraU[0] == palabraS[3] or palabraU[0] == palabraS[4]:
            print(f"La letra {palabraU[0]} existe en la palabra pero está en una posición errónea ❎ \n")
        if palabraU[1] == palabraS[1]:
            mostrarPalabra[1]=palabraS[1]
        if palabraU[1] == palabraS[2] or palabraU[1] == palabraS[3] or palabraU[1] == palabraS[4] or palabraU[1] == palabraU[0]:
            print(f"La letra {palabraU[1]} existe en la palabra pero está en una posición errónea ❎ \n")
        if palabraU[2] == palabraS[2]:
            mostrarPalabra[2]=palabraS[2]
        if palabraU[2] == palabraS[0] or palabraU[2]== palabraS[1] or palabraU[2] == palabraS[3] or palabraU[2] == palabraS[4]:
            print(f"La letra {palabraU[2]} existe en la palabra pero está en una posición errónea ❎ \n")
        if palabraU[3] == palabraS[3]:
            mostrarPalabra[3]=palabraS[3]
        if palabraU[3] == palabraS[0] or palabraU[3] == palabraS[1] or palabraU[3] == palabraS[2] or palabraU[3] == palabraS[4]:
            print(f"La letra {palabraU[3]} existe en la palabra pero está en una posición errónea ❎ \n")
        if palabraU[4] == palabraS[4]:
            mostrarPalabra[4]=palabraS[4]
        if palabraU[4] == palabraS[1] or palabraU[4] == palabraS[2] or palabraU[4] == palabraS[3] or palabraU[4] == palabraS[0]:
            print(f"La letra {palabraU[4]} existe en la palabra pero está en una posición errónea ❎ \n")
        print(f"Numero de intentos: {count} \n")
        print(mostrarPalabra)
        if palabraUsuario == palabraSecreta:
            print(f"Has acertado, enhorabuena 🏆!! los has logrado en {count} intentos 🔄 ")
            count=7

print("""
*******************************************************************************************      
                                ⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿
                                ⠄⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⠄⣿
                                ⣿⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⠄⠄⣿
                                ⣿⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⠄⠄⣿
                                ⣿⠄⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⣿⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿
                                ⣿⠄⠄⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿
                                ⣿⠄⠄⠄⠄⠄⠄⣿⣿⣿⠄⠄⣿⠄⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                ⣿⠄⠄⠄⠄⠄⣿⠄⠄⠄⣿⣿⠄⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿
                                ⠄⣿⠄⠄⠄⣿⠄⠄⠄⣿⣿⠄⠄⠄⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿
                                ⠄⠄⣿⠄⠄⣿⠄⠄⣿⠄⠄⠄⣿⠄⠄⠄⠄⠄⣿⠄⠄⠄⣿⣿⣿⣿⠄⣿
                                ⠄⠄⠄⣿⠄⣿⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⠄⣿
                                ⣿⣿⣿⠄⠄⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⣿
                                ⣿⠄⠄⠄⣿⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⠄⠄⠄⠄⣿⠄⠄⣿
                                ⠄⣿⠄⠄⠄⣿⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿
                                ⠄⠄⣿⠄⠄⣿⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿
                                ⠄⠄⠄⣿⠄⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿
                                ⠄⠄⠄⠄⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⠄⠄⠄⣿
                                ⠄⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⠄⣿⠄⠄⠄⣿
                                ⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⠄⠄⠄⣿⣿⣿⣿
                                ⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿
                                ⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿
                                ⠄⠄⣿⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⣿
                                ⠄⠄⠄⣿⠄⠄⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⠄⠄⠄⠄⣿
                                ⠄⠄⠄⣿⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⠄⠄⠄⣿⣿
                                ⠄⠄⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿
                              
    
                            Gracias por jugar con nosotros!!
      
*******************************************************************************************      
      """)
