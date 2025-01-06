import pgzero
import random
import time

WIDTH = 600
HEIGHT = 600
score=0
game_over = False
bee=Actor("bee")
bee.pos=(100,100)
flower=Actor("flower")
flower.pos=(200,200)
msg=""

def draw():
    screen.built("background",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("score:"+str(score),color="black",topleft=(10,10))

    if game_over:
        screen.fill("blue")
        global msg
        msg="time up!\nyour final score:"
        screen.draw.text(msg+str(score),midtop=(WIDTH/2,20),fontsize=50,color="green")
def place_flower():
    pass

def time_up()
    pass

def update():
    pass

clock,schedule(time_up,60.0)

screen.blit





pgzrun.go()




    

    
