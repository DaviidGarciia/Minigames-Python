import tkinter
import random
from PIL import Image, ImageTk

class Personaje:
    def __init__(self,vida, energia, velocidad, fuerza):
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad
        self.fuerza = fuerza
    def comerPizza (self):
        self.velocidad -= 10
        self.energia += 20
    def comerPlatano (self):
        self.energia += 20
        self.vida += 15
    def beberCerveza (self):
        self.velocidad-=10
        self.vida -=5
    def beberCafe(self):
        self.energia += 15
    def peleaGallo (self):
        self.vida-=5
        self.energia -= 10
    def aliadoMapache (self):
        self.velocidad += 10
        self.fuerza += 15
    def miniEspada (self):
        self.fuerza += 5
    def maxEspada (self):
        self.fuerza += 15
    

jugar = True
naruto = Personaje(60,60,60,60)

#while jugar== True:
ventana = tkinter.Tk()

ventana.geometry("1400x1400")

etiqueta = tkinter.Label(ventana, text = "Bienvenido a la mazmorra infernal, ayuda a Naruto a buscar su reconocimiento mundial y para ello necesita conseguir seguidores de instagram, su plan es subir un reel desde dentro de la mazmorra con la foto perfecta.")
imagenPrincipal = Image.open("Narutosaludo.jpg")
imagen_tk = ImageTk.PhotoImage(imagenPrincipal)
label = tkinter.Label(ventana, image=imagen_tk)
 

vida = tkinter.Label(ventana, text=f"Vida base:{naruto.vida}")
energia = tkinter.Label(ventana, text=f"Energia base:{naruto.energia}")
velocidad=tkinter.Label(ventana, text=f"Velocidad base:{naruto.velocidad}")
fuerza= tkinter.Label(ventana, text=f"Fuerza base:{naruto.fuerza}")
pregunta1 = tkinter.Label(ventana, text="""
    Naruto se encuentra dentro de la mazmorra, ahora mismo está indeciso sobre qué camino elegir, a la derecha hay un largo pasillo lúgubre y a la izquierda una sala con una puerta.\n
          """)
def limpiar_ventana():
        for widget in ventana.winfo_children():
            widget.destroy()
def respuesta1A ():
    limpiar_ventana()
    
    
def respuesta1B ():
    print("sala") 

respuesta1a = tkinter.Button(ventana, bg="green",fg="white",text="Pasillo",width="4",height="2", command = respuesta1A)
respuesta1b = tkinter.Button(ventana, bg="red",fg="white",text="Sala",width="4",height="2",command = respuesta1B)


etiqueta.pack(side=tkinter.TOP,fill= tkinter.BOTH, expand=True)

label.pack(side=tkinter.TOP)

vida.pack(side=tkinter.TOP)
energia.pack(side=tkinter.TOP)
velocidad.pack(side=tkinter.TOP)
fuerza.pack(side=tkinter.TOP)

pregunta1.pack()
respuesta1a.pack(side=tkinter.LEFT,fill= tkinter.BOTH, expand=True)
respuesta1b.pack(side=tkinter.RIGHT,fill= tkinter.BOTH, expand=True)

ventana.mainloop()
