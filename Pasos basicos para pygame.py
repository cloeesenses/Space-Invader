import pygame  # importar pygame

pygame.init()  # Boton de encendido obligatorio

ventana = pygame.display.set_mode((400, 400))  # Creacion de ventana de juego

# Paleta de colores iventada por mi
rojo = (250, 0, 0)
verde = (0, 150, 0)
azul = (0, 0, 100)
color_fav = (0, 150, 150)

# Crear reloj para controlar FPS
reloj = pygame.time.Clock()

# Necesita un loop para mantenerse activa, de lo contrario se cerrará
corriendo = True
while corriendo:
    for evento in pygame.event.get():  # Leer eventos (ES LOS OJOS)
        if evento.type == pygame.QUIT:  # Dar clic en x
            corriendo = False  # Si dan clic en x salimos
        elif evento.type == pygame.KEYDOWN:
            print("Presionaste una tecla")

    ventana.fill(color_fav)  # Fondo color fav
    # (x,y,largo,altura)    RECTANGULO
    pygame.draw.rect(ventana, azul, (175, 175, 50, 50))
    # ((x,y),radio)      CIRCULO
    pygame.draw.circle(ventana, rojo, (100, 100), 25)
    # ((x,y)inicio,(x,y)final, pixeles de grosor)   LINEA
    pygame.draw.line(ventana, verde, (224, 223), (300, 300), 5)
    pygame.display.flip()  # Actualizar pantalla
    pygame.display.set_caption("Space-Invader")  # Titulo
    reloj.tick(60)  # Mantener juego a 60 FPS


pygame.quit()  # Apagar el pygame cuando sales

# Tambien existe sys.exit()  pero este solo es ecesario cuando la interface funciona mas alla del bucle while.
