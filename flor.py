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
    lapiz.penup()
    lapiz.goto(0, -50)
    lapiz.pendown()

    # Pétalos
    for i in range(6):
        lapiz.circle(50)
        lapiz.left(60)

    # Centro
    lapiz.penup()
    lapiz.goto(0, -25)
    lapiz.pendown()
    lapiz.circle(25)


def main():
    dibujar_base()
    dibujar_flor()

    turtle.done()


main()