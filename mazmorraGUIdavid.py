import tkinter
from PIL import Image, ImageTk
import random

class Personaje:
    def __init__(self, vida, energia, velocidad, fuerza):
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


# Inicializar personaje
naruto = Personaje(60, 60, 60, 60)

# Crear la ventana
ventana = tkinter.Tk()
ventana.geometry("1400x1400")
ventana.title("Mazmorra Infernal")

# Función para configurar el fondo de la ventana
def configurar_fondo():
    imagen_fondo = Image.open("mazmorra.jpg")
    imagen_fondo = imagen_fondo.resize((1400, 1400), Image.LANCZOS)
    fondotk = ImageTk.PhotoImage(imagen_fondo)
    label_fondo = tkinter.Label(ventana, image=fondotk)
    label_fondo.image = fondotk  # Guardar referencia a la imagen
    label_fondo.place(relwidth=1, relheight=1)

# Configurar el fondo al inicio
configurar_fondo()
def pantallaPrincipal():
# Crear etiqueta de bienvenida
    limpiar_ventana()
    etiqueta = tkinter.Label(ventana, text="Bienvenido a la mazmorra infernal, ayuda a Naruto a buscar su reconocimiento mundial y para ello necesita conseguir seguidores de Instagram, su plan es subir un reel desde dentro de la mazmorra con la foto perfecta.", bg="grey", fg="white")
    etiqueta.pack(side=tkinter.TOP,pady=150)

# Crear imagen principal
    imagenPrincipal = Image.open("Narutosaludo.jpg")
    imagen_tk = ImageTk.PhotoImage(imagenPrincipal)
    label = tkinter.Label(ventana, image=imagen_tk)
    label.pack(side=tkinter.TOP)

# Crear Labels sin fondo visible
    vida = tkinter.Label(ventana, text=f"Vida base: {naruto.vida}", bg="grey", fg="white")
    energia = tkinter.Label(ventana, text=f"Energia base: {naruto.energia}", bg="grey", fg="white")
    velocidad = tkinter.Label(ventana, text=f"Velocidad base: {naruto.velocidad}", bg="grey", fg="white")
    fuerza = tkinter.Label(ventana, text=f"Fuerza base: {naruto.fuerza}", bg="grey", fg="white")
    pregunta1 = tkinter.Label(ventana, text="""
        Naruto se encuentra dentro de la mazmorra, ahora mismo está indeciso sobre qué camino elegir, a la derecha hay un largo pasillo lúgubre y a la izquierda una sala con una puerta.
            """, bg="grey", fg="white")
    vida.pack(side=tkinter.TOP)
    energia.pack(side=tkinter.TOP)
    velocidad.pack(side=tkinter.TOP)
    fuerza.pack(side=tkinter.TOP)
    pregunta1.pack(pady=40)
    respuesta1a = tkinter.Button(ventana, bg="green", fg="white", text="Pasillo", width="85", height="2", command=respuesta1A)
    respuesta1b = tkinter.Button(ventana, bg="red", fg="white", text="Sala", width="85", height="2", command=respuesta1B)
    respuesta1a.pack(side=tkinter.LEFT)
    respuesta1b.pack(side=tkinter.RIGHT)
    ventana.mainloop()

# Función para limpiar la ventana
def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()
    configurar_fondo()  # Volver a configurar el fondo

# Respuestas a las decisiones
def salir():
    ventana.destroy()
def respuesta1A():
    limpiar_ventana()
    naruto.comerPlatano()
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto se ha encontrado un plátano en una esquina, se lo come y le sube la energía y la vida.\n").pack(side=tkinter.TOP,pady=20)
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto obtuvo +20 de energía y +15 de vida.\n").pack(side=tkinter.TOP,pady=20)
    platano = Image.open("platano.jpg")
    platano_tk = ImageTk.PhotoImage(platano)
    tkinter.Label(ventana, image=platano_tk).pack(side=tkinter.TOP,pady=250)
    tkinter.Label(ventana, bg="grey", fg="white", text="Después de que Naruto tomara su primera decisión, se encuentra en una situación donde tiene que elegir si subir a la planta de arriba usando las escaleras, o seguir avanzando recto.\n").pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=False)
    boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Subir", width="85", height="2", command=respuesta2A)
    boton1A.pack(side=tkinter.LEFT)
    boton1B = tkinter.Button(ventana, bg="red", fg="white", text="Recto", width="85", height="2", command=respuesta2B)
    boton1B.pack(side=tkinter.RIGHT)
    ventana.mainloop()

def respuesta2A():
    limpiar_ventana()
    naruto.aliadoMapache()
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto se encontró a Rocket, rocket estaba buscando a Groot, al hablar con Naruto decidió unirse a él en su aventura para lograr su ansioso propósito \n").pack(side=tkinter.TOP,pady=20)
    tkinter.Label(ventana, bg="grey", fg="white", text="Rocket le da a Naruto +10 de velocidad y +15 de fuerza \n").pack(side=tkinter.TOP,pady=20)
    mapache = Image.open("rocket.jpeg")
    mapache_tk = ImageTk.PhotoImage(mapache)
    tkinter.Label(ventana, image=mapache_tk).pack(side=tkinter.TOP,pady=250)
    tkinter.Label(ventana, bg="grey", fg="white", text="""Naruto sigue deambulando por la mazmorra, desesperado buscando la foto perfecta para su instagram cuando de repente encuentra una sala cerrada que le llama la atención. 
                No sabe si abrir la puerta para ver qué hay o pasar y seguir de largo \n""").pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=False)
    boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Abrir", width="85", height="2", command=respuesta3A)
    boton1A.pack(side=tkinter.LEFT)
    boton1B = tkinter.Button(ventana, bg="red", fg="white", text="Pasar", width="85", height="2", command=respuesta3B)
    boton1B.pack(side=tkinter.RIGHT)
    ventana.mainloop()
def respuesta3A():
    limpiar_ventana()
    naruto.miniEspada()
    tkinter.Label(ventana, bg="grey", fg="white", text="Te encuentras una espada muy pequeña, casi como un puñal, decides guardarla por si te hace falta \n").pack(side=tkinter.TOP,pady=20)
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto gana +5 de fuerza \n").pack(side=tkinter.TOP,pady=20)
    miniespada = Image.open("espadapequeña_naruto.jpeg")
    miniespada_tk = ImageTk.PhotoImage(miniespada)
    tkinter.Label(ventana, image=miniespada_tk).pack(side=tkinter.TOP,pady=250)
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto ya está desesperado, quiere salir ya de aquí para volver a su entrenamiento con Jiraiya, va despistado cuando se encuentra con un agujero en el suelo, ¿lo esquiva o se cae? \n").pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=False)
    boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Esquiva", width="85", height="2", command=respuesta4A)
    boton1A.pack(side=tkinter.LEFT)
    boton1B = tkinter.Button(ventana, bg="red", fg="white", text="Cae", width="85", height="2", command=respuesta4B)
    boton1B.pack(side=tkinter.RIGHT)
    ventana.mainloop()
def respuesta4A():
    limpiar_ventana()
    naruto.maxEspada()
    tkinter.Label(ventana, bg="grey", fg="white", text="Con sus habilidades ninjas, logra esquivar de un salto el agujero del suelo y ve algo brillante en la esquina, se acerca y es una espada enorme \n").pack(side=tkinter.TOP,pady=20)
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto obtiene +15 de fuerza \n").pack(side=tkinter.TOP,pady=20)
    espadagrande = Image.open("espadagrande_naruto.jpeg")
    espadagrande_tk = ImageTk.PhotoImage(espadagrande)
    tkinter.Label(ventana, image=espadagrande_tk).pack(side=tkinter.TOP,pady=150)
    tkinter.Label(ventana,bg="grey", fg="white",text="Estado de Naruto:").pack(side=tkinter.TOP,pady=10)
    tkinter.Label(ventana, text=f"Vida actual: {naruto.vida}", bg="grey", fg="white").pack(side=tkinter.TOP)
    tkinter.Label(ventana, text=f"Energia actual: {naruto.energia}", bg="grey", fg="white").pack(side=tkinter.TOP)
    tkinter.Label(ventana, text=f"Velocidad actual: {naruto.velocidad}", bg="grey", fg="white").pack(side=tkinter.TOP)
    tkinter.Label(ventana, text=f"Fuerza actual: {naruto.fuerza}", bg="grey", fg="white").pack(side=tkinter.TOP)
    tkinter.Label(ventana, bg="grey", fg="white", text="Después de varias horas caminando por la mazmorra, encuentras a lo lejos el sitio ideal para su foto pero hay un Dragón gigante que bloquea el paso. ¿Qué hace Naruto? ¿Pelea o se intenta escapar? \n").pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=False,pady=20)
    boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Pelea", width="85", height="2", command=respuesta5A)
    boton1A.pack(side=tkinter.LEFT)
    boton1B = tkinter.Button(ventana, bg="red", fg="white", text="Escapa", width="85", height="2", command=respuesta5B)
    boton1B.pack(side=tkinter.RIGHT)
    ventana.mainloop()
def respuesta5A():
    limpiar_ventana()
    fuerzaDragon = random.randint(75,100)
    if naruto.fuerza > fuerzaDragon or naruto.fuerza == fuerzaDragon:
        tkinter.Label(ventana,bg="grey", fg="white",text="Naruto logró derrotar al Dragón y lo dejó inconsciente gracias a eso logra su objetivo de conseguir seguidores subiendo un selfie con el Dragón abatido !! \n").pack(side=tkinter.TOP,pady=30)
        gana = Image.open("Naruto_gana.jpeg")
        gana_tk = ImageTk.PhotoImage(gana)
        tkinter.Label(ventana, image=gana_tk).pack(side=tkinter.TOP,pady=150)
        tkinter.Label(ventana,text="¿Quieres volver a jugar?").pack(side=tkinter.TOP)
        boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Si", width="85", height="2", command=pantallaPrincipal)
        boton1A.pack(side=tkinter.LEFT)
        boton1B = tkinter.Button(ventana, bg="red", fg="white", text="No", width="85", height="2", command=salir)
        boton1B.pack(side=tkinter.RIGHT)
        ventana.mainloop()
    elif naruto.fuerza < fuerzaDragon:
        tkinter.Label(ventana,text="El dragón dejó malherido a Naruto ya que tiene más fuerza que él, Naruto se logra escabullir del Dragón y se va del lugar avergonzado por la humillante derrota.\n").pack(side=tkinter.TOP,pady=30)
        pierde = Image.open("Naruto_pierde.jpeg")
        pierde_tk = ImageTk.PhotoImage(pierde)
        tkinter.Label(ventana, image=pierde_tk).pack(side=tkinter.TOP,pady=150)
        tkinter.Label(ventana,text="¿Quieres volver a jugar?").pack(side=tkinter.TOP)
        boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Si", width="85", height="2", command=pantallaPrincipal)
        boton1A.pack(side=tkinter.LEFT)
        boton1B = tkinter.Button(ventana, bg="red", fg="white", text="No", width="85", height="2", command=salir)
        boton1B.pack(side=tkinter.RIGHT)
        ventana.mainloop()
def respuesta1B():
    limpiar_ventana()
    naruto.peleaGallo()
    tkinter.Label(ventana, bg="grey", fg="white", text="Abre la puerta con cuidado, entra, y se encuentra a un gallo que le persigue por toda la sala intentando picarle \n").pack(side=tkinter.TOP,pady=20)
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto perdió -5 de vida y -10 de energia \n").pack(side=tkinter.TOP,pady=20)
    gallo = Image.open("gallo_ataque.jpeg")
    gallo_tk = ImageTk.PhotoImage(gallo)
    tkinter.Label(ventana, image=gallo_tk).pack(side=tkinter.TOP,pady=250)
    tkinter.Label(ventana, bg="grey", fg="white", text="Después de que Naruto tomara su primera decisión, se encuentra en una situación donde tiene que elegir si subir a la planta de arriba usando las escaleras, o seguir avanzando recto.\n").pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=False)
    boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Subir", width="85", height="2", command=respuesta2A)
    boton1A.pack(side=tkinter.LEFT)
    boton1B = tkinter.Button(ventana, bg="red", fg="white", text="Recto", width="85", height="2", command=respuesta2B)
    boton1B.pack(side=tkinter.RIGHT)
    ventana.mainloop()
def respuesta2B():
    limpiar_ventana()
    naruto.comerPizza()
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto se encontró una pizza encima de una mesa, con el hambre que tenía decidió parar comer \n").pack(side=tkinter.TOP,pady=20)
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto pierde -10 de velocidad y gana +20 de energia \n").pack(side=tkinter.TOP,pady=20)
    pizza = Image.open("pizza_naruto.jpg")
    pizza = pizza.resize((200, 200), Image.LANCZOS)
    pizza_tk = ImageTk.PhotoImage(pizza)
    tkinter.Label(ventana, image=pizza_tk).pack(side=tkinter.TOP,pady=250)
    tkinter.Label(ventana, bg="grey", fg="white", text="""Naruto sigue deambulando por la mazmorra, desesperado buscando la foto perfecta para su instagram cuando de repente encuentra una sala cerrada que le llama la atención. 
                No sabe si abrir la puerta para ver qué hay o pasar y seguir de largo \n""").pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=False)
    boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Abrir", width="85", height="2", command=respuesta3A)
    boton1A.pack(side=tkinter.LEFT)
    boton1B = tkinter.Button(ventana, bg="red", fg="white", text="Pasar", width="85", height="2", command=respuesta3B)
    boton1B.pack(side=tkinter.RIGHT)
    ventana.mainloop()
def respuesta3B():
    limpiar_ventana()
    naruto.beberCerveza()
    tkinter.Label(ventana, bg="grey", fg="white", text="Te encuentras un barril de cerveza, y decides beber porque hace mucho calor en la mazmorra \n").pack(side=tkinter.TOP,pady=20)
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto pierde -10 de velocidad y -5 de vida \n").pack(side=tkinter.TOP,pady=20)
    cerveza = Image.open("cerveza_naruto.jpeg")
    cerveza_tk = ImageTk.PhotoImage(cerveza)
    tkinter.Label(ventana, image=cerveza_tk).pack(side=tkinter.TOP,pady=250)
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto ya está desesperado, quiere salir ya de aquí para volver a su entrenamiento con Jiraiya, va despistado cuando se encuentra con un agujero en el suelo, ¿lo esquiva o se cae? \n").pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=False)
    boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Esquiva", width="85", height="2", command=respuesta4A)
    boton1A.pack(side=tkinter.LEFT)
    boton1B = tkinter.Button(ventana, bg="red", fg="white", text="Cae", width="85", height="2", command=respuesta4B)
    boton1B.pack(side=tkinter.RIGHT)
    ventana.mainloop()
def respuesta4B():
    limpiar_ventana()
    naruto.beberCafe()
    tkinter.Label(ventana, bg="grey", fg="white", text="Cae por el agujero y llega a un sótano, dentro del sótano hay una mesita y encuentra café recién hecho, sin pensarlo, toma una taza de café para espabilarse después de la caida. \n").pack(side=tkinter.TOP,pady=20)
    tkinter.Label(ventana, bg="grey", fg="white", text="Naruto obtiene +15 de energia \n").pack(side=tkinter.TOP,pady=20)
    cafe = Image.open("cafe_naruto.jpeg")
    cafe_tk = ImageTk.PhotoImage(cafe)
    tkinter.Label(ventana, image=cafe_tk).pack(side=tkinter.TOP,pady=150)
    tkinter.Label(ventana,bg="grey", fg="white",text="Estado de Naruto:").pack(side=tkinter.TOP,pady=10)
    tkinter.Label(ventana, text=f"Vida actual: {naruto.vida}", bg="grey", fg="white").pack(side=tkinter.TOP)
    tkinter.Label(ventana, text=f"Energia actual: {naruto.energia}", bg="grey", fg="white").pack(side=tkinter.TOP)
    tkinter.Label(ventana, text=f"Velocidad actual: {naruto.velocidad}", bg="grey", fg="white").pack(side=tkinter.TOP)
    tkinter.Label(ventana, text=f"Fuerza actual: {naruto.fuerza}", bg="grey", fg="white").pack(side=tkinter.TOP)
    tkinter.Label(ventana, bg="grey", fg="white", text="Después de varias horas caminando por la mazmorra, encuentras a lo lejos el sitio ideal para su foto pero hay un Dragón gigante que bloquea el paso. ¿Qué hace Naruto? ¿Pelea o se intenta escapar? \n").pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=False,pady=20)
    boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Pelea", width="85", height="2", command=respuesta5A)
    boton1A.pack(side=tkinter.LEFT)
    boton1B = tkinter.Button(ventana, bg="red", fg="white", text="Escapa", width="85", height="2", command=respuesta5B)
    boton1B.pack(side=tkinter.RIGHT)
    ventana.mainloop()
def respuesta5B():
    limpiar_ventana()
    fuerzaDragon = random.randint(75,100)
    tkinter.Label(ventana,text="Naruto intentó escapar pero el Dragón lo persiguió y lo acorraló !! \n")
    if naruto.fuerza > fuerzaDragon or naruto.fuerza == fuerzaDragon:
        tkinter.Label(ventana,bg="grey", fg="white",text="Naruto logró derrotar al Dragón y lo dejó inconsciente gracias a eso logra su objetivo de conseguir seguidores subiendo un selfie con el Dragón abatido !! \n").pack(side=tkinter.TOP,pady=30)
        gana = Image.open("Naruto_gana.jpeg")
        gana_tk = ImageTk.PhotoImage(gana)
        tkinter.Label(ventana, image=gana_tk).pack(side=tkinter.TOP,pady=150)
        tkinter.Label(ventana,text="¿Quieres volver a jugar?").pack(side=tkinter.TOP)
        boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Si", width="85", height="2", command=pantallaPrincipal)
        boton1A.pack(side=tkinter.LEFT)
        boton1B = tkinter.Button(ventana, bg="red", fg="white", text="No", width="85", height="2", command=salir)
        boton1B.pack(side=tkinter.RIGHT)
        ventana.mainloop()
    elif naruto.fuerza < fuerzaDragon:
        tkinter.Label(ventana,text="El dragón dejó malherido a Naruto ya que tiene más fuerza que él, Naruto se logra escabullir del Dragón y se va del lugar avergonzado por la humillante derrota.\n").pack(side=tkinter.TOP,pady=30)
        pierde = Image.open("Naruto_pierde.jpeg")
        pierde_tk = ImageTk.PhotoImage(pierde)
        tkinter.Label(ventana, image=pierde_tk).pack(side=tkinter.TOP,pady=150)
        tkinter.Label(ventana,text="¿Quieres volver a jugar?").pack(side=tkinter.TOP)
        boton1A = tkinter.Button(ventana, bg="green", fg="white", text="Si", width="85", height="2", command=pantallaPrincipal)
        boton1A.pack(side=tkinter.LEFT)
        boton1B = tkinter.Button(ventana, bg="red", fg="white", text="No", width="85", height="2", command=salir)
        boton1B.pack(side=tkinter.RIGHT)
        ventana.mainloop()
    


# Empaquetar Labels y botones
pantallaPrincipal()

