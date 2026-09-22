import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("white")

lapiz = turtle.Turtle()
lapiz.speed(0)


def dibujar_base():
    # Aquí Enrique hará la base de la flor
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