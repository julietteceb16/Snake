"""Snake, classic arcade game.
Exercises
Uno de los dos hará que:
1.- La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana
2.- Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes 
entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo.
"""

from random import randrange
from turtle import *
from freegames import square, vector
"""Colores para la serpiente y la comida"""
colores = ["Blue", "magenta", "green", "pink", "grey", 'orange', 'purple', 'yellow', 'turquoise', 'skyblue']
"""Random para elegir el color de la serpiente"""
numero = randrange(5)
"""Eliminar el color elegido por la serpiente para que no sean igual"""
colores.pop(numero)
"""Random para elegir el color de la comida"""
numero2 = randrange(5)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def random_food():
    """Randomizes the position of the food by one square wleaving the window"""
    #Esta función permititirá que la comida pueda moverse de manera random 
    if food.x >= -150 and food.x <=150:#Se mueve en dirección x
        food.x += randrange(-1,2) * 10

    if food.y >= -150 and food.y <=150:#Se mueve en dirección y
        food.y += randrange(-1,2) * 10


    
def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)

    clear()
    for body in snake:
        square(body.x, body.y, 9, colores[numero])
    square(food.x, food.y, 9, colores[numero2])
    if randrange(10) == 1:
        food.x += 10
    if randrange(10) == 2:
        food.x -= 10
    if randrange(10) == 3:
        food.y += 10
    if randrange(10) == 4:
        food.y -= 10

        
    update()
    ontimer(move, 100)



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
