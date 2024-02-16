import turtle as t
import random

def makeHeart(size):
    t.begin_fill()
    t.forward(size)
    t.circle(size/2, 180)
    t.right(90)
    t.circle(size/2, 180)
    t.forward(size)
    t.left(90)
    t.end_fill()


def iLoveMyBoy(size, length, depth):
    t.speed(0)
    if depth == 0:
        return
    iLoveMyBoy(size*1.5, length, depth-1)
    i = 315
    while i > 0:
        heartColor = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        t.color(heartColor)
        t.fillcolor(heartColor)
        makeHeart(size)
        t.left(45)
        i = i - 45


def checkbox():
    t.forward(50)
    t.color("black")
    t.write("Will you be my valentine?", move=False, align="center", font=("Courier New", 20, "normal"))
    t.right(180)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.down()
    for i in range(4):
        t.forward(30)
        t.left(90)
    t.forward(15)
    t.write("yes", move=False, align="center", font=("Courier New", 20, "normal"))
    t.up()
    t.right(180)

    t.goto(0, 0)
    t.forward(50)
    t.down()
    for i in range(4):
        t.forward(30)
        t.right(90)
    t.forward(15)
    t.write("no", move=False, align="center", font=("Courier New", 20, "normal"))
    t.up()
    t.onscreenclick(yesOrYes, btn=1, add=None)


def yesOrYes(x, y):
    if -30 < y < 0:
        if -80 < x < -50:
            tick()
        if 50 < x < 80:
            cross()


def tick():
    t.onscreenclick(none, btn=1, add=None)
    t.goto(-80, 0)
    t.right(60)
    t.down()
    t.goto(-65, -30)
    t.left(120)
    t.goto(-50, 0)
    t.up()
    heartAttack()


def cross():
    t.onscreenclick(none, btn=1, add=None)
    t.goto(50, 0)
    t.right(45)
    t.down()
    t.goto(80, -30)
    t.left(135)
    t.up()
    t.goto(80, 0)
    t.left(135)
    t.down()
    t.goto(50, -30)
    t.up()
    t.tilt(135)
    error() #if there is no choise


def error():
    t.goto(0, 50)
    t.down()
    t.write("Error", move=False, align="center", font=("Courier New", 96, "bold"))
    t.onscreenclick(undo, btn=1, add=None)


def undo(x, y):
    if (-30 < y < 0) and (-80 < x < -50):
        t.undo()
        t.up()
        yesOrYes(x, y)
    else:
        t.undo()
        t.write("Please!", move=False, align="center", font=("Courier New", 76, "bold"))
        t.onscreenclick(heSaidNo, btn=1, add=None)


        

def heSaidNo(x, y):
    t.speed(6)
    if (-30 < y < 0) and (-80 < x < -50):
        tick()
    if (-30 < y < 0) and (50 < x < 80):
        t.onscreenclick(none, btn=1, add=None)
        t.up()
        t.goto(0, 50)
        t.up()
        t.tilt(-135)
        t.left(45)
        t.forward(275)
        t.left(135)
        t.down()
        makeHeart(300)
        t.left(45)
        t.color("white")
        t.up()
        t.goto(0, 15)
        t.write("He said «No» :(", move=False, align="center", font=("Courier New", 20, "normal"))
        t.up()
        t.goto(0, 200)

        t.down()
        t.left(150)
        t.forward(100)
        t.left(60)
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.left(60)
        t.forward(100)
        t.right(30)
        t.forward(75)


def none():
    return


def heartAttack():
    t.speed(0)
    while 1:
        attackColor = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        t.color(attackColor)
        t.fillcolor(attackColor)
        t.begin_fill()
        makeHeart(100)
        t.end_fill()
        t.left(random.randint(0, 180))
        t.goto(random.randint(-500, 500), random.randint(-500, 500))


def main():
    t.colormode(255)
    iLoveMyBoy(100, 0, 4)
    # move down to make a center heart
    t.speed(0)
    t.up()
    t.color("red")
    t.left(90)
    t.forward(225)
    t.left(135)
    t.down()
    makeHeart(300)
    t.color("black")
    # move up to make a title and a checkbox
    t.up()
    t.left(45)
    t.goto(0, 0)
    checkbox()
    t.done()

main()
