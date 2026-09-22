import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("white")

lapiz = turtle.Turtle()
lapiz.speed(0)


def dibujar_base():
    # Aquí Enrique hará la base de la flor
    
    # Tallo
    lapiz.penup()
    lapiz.goto(0, -200)
    lapiz.pendown()
    lapiz.goto(0, -50)

    # Hoja izquierda
    lapiz.goto(-50, -100)
    lapiz.goto(0, -120)

    # Regresar al centro
    lapiz.goto(0, -50)
    pass


def dibujar_flor():
    # Aquí Carlos hará la flor
    pass


def main():
    dibujar_base()
    dibujar_flor()

    turtle.done()


main()