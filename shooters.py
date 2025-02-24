import pgzero
import random

WIDTH = 750
HEIGHT = 650

WHITE = (255,255,255)
BLUE = (0,0,255)
#create shape

ship=Actor("shooter")

bug=Actor("bug")
ship.pos=(WIDTH//2,HEIGHT-60)
bullets=[]
enemies= []
enemies.append(Actor("bug"))
enemies[-1].x=100
enemies[-1].y=-100
score=0
def displayscore():
    pass
