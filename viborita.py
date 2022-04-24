import turtle
import time
import random

posponer = 0.1

#Marcador

score = 0
hight_score = 0




#Configuracion de la ventana
wn = turtle.Screen()
wn.title("juego de la viborita")
wn.bgcolor("black")
wn.setup(width = 600, height= 600)
wn.tracer(0)

#cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("square")
comida.color("blue")
comida.penup()
comida.goto(0,100)

#Cuerpo serpiente
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("yellow")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntos: 0     Mejor Puntuacion:0",
            align= "center", font= ("Courier", 20, "normal"))



#Funciones

def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def derecha():
    cabeza.direction = "right"

def izquierda():
    cabeza.direction = "left"
    
   


def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
    
   

#Teclado
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")


while True:

    wn.update()

    #Perder por los bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        texto.clear()
        texto.write("Perdiste estupido",
                    align="center", font=("Courier", 20, "normal"))


        #esconder cola
        for segmento in segmentos:
            segmento.goto(1000, 1000)#la mandas a la mierda
            #limpiar los segmentos
        segmentos.clear()

        #Resetear marcador
        score = 0
        texto.clear()
        texto.write("Puntos: {}     Mejor Puntuacion:{}".format(score, hight_score),
                    align="center", font=("Courier", 20, "normal"))


    #Cada vez que toca la comida que se agregue un pedazito, que vaya a la cola y sume el marcador
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        nuevo_segmentos = turtle.Turtle()
        nuevo_segmentos.speed(0)
        nuevo_segmentos.shape("square")
        nuevo_segmentos.color("grey")
        nuevo_segmentos.penup()
        segmentos.append(nuevo_segmentos)
        texto.clear()
        texto.write("Puntos: {}     Mejor Puntuacion:{}".format(score, hight_score),
                    align="center", font=("Courier", 20, "normal"))
        #Aumentar el marcador
        score += 10
        if score > hight_score:
            hight_score = score
            texto.clear()
            texto.write("Puntos: {}     Mejor Puntuacion:{}".format(score, hight_score),
                        align= "center", font= ("Courier", 20, "normal"))



 #mover el cuerpo de la serpiente
    totalseg = len(segmentos)
    for index in range(totalseg-1, 0, -1): #El 0 hace que no lo incluya y vaya del 5 al 1
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalseg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    movimiento()

    #Perder con la cola
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
            segmentos.clear()
            # Resetear marcador
            score = 0
            texto.clear()
            texto.write("Puntos: {}     Mejor Puntuacion:{}".format(score, hight_score),
                        align="center", font=("Courier", 20, "normal"))

    time.sleep(posponer)