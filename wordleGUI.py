import tkinter
from PIL import Image, ImageTk
import random
numeroAleatorio = random.randint(0,7)

lista = ["comer","actor","bizco","cabra","cerdo","avion","pipas","llave"]

palabraSecreta = lista[numeroAleatorio]

#count = 0

ventana = tkinter.Tk()
ventana.geometry("1400x1400")
ventana.title("Wordle D&J")
def pantallaPrincipal():
    limpiar_ventana()
    configurar_fondo()
    tkinter.Label(ventana,bg="#33fff3",font=50,text="Bienvenidos a Wordle !!").pack(pady=100,)
    tkinter.Label(ventana,bg="#33fff3",font=40,text="""   Este juego trata de adivinar la palabra secreta que contiene 5 letras, para ello tendrás un total de 6 intentos y en cada una de los cuadrados deberás poner una letra de la palabra. \n
    Si la letra aparece de color verde, significa que la letra está correcta y encima está en la misma posición que la palabra secreta.
    Si la letra aparece en amarillo significará que la palabra secreta contiene esa letra pero aparece en otra posición 
    Si la letra aparece en gris significa que la palabra secreta no contiene esta letra.                                                                                                    
                        
                            
""").pack()
    vcmd = (ventana.register(validate_input), '%P')
    tkinter.Entry(ventana,validate="key",validatecommand=vcmd).pack()
    tkinter.Button(ventana, bg="White",font=50,fg="black",text="Comenzar").pack()
    ventana.mainloop()
def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()
    configurar_fondo()
def configurar_fondo():
    label_fondo = tkinter.Label(ventana, bg="#33fff3") 
    label_fondo.place(relwidth=1, relheight=1)
def validate_input(new_value):
    return len(new_value) <= 1
    
pantallaPrincipal()
ventana.mainloop()