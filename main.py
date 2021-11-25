import turtle

t = turtle.Turtle()


def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


def carres(taille_depart, nb):
    for i in range(0, nb):
        carre(taille_depart+(i*taille_depart))


carres(10, 50)


turtle.done()
