#Example 10-1
import pgzrun
from random import randint

#function for display
def draw():
       screen.blit('bg1',(0,0))
       for alien in aliens:
              alien.draw()

def update():
       for alien in aliens:
              alien.x += 1
              alien.y += 1
              if alien.top > HEIGHT:
                     alien.bottom = 0
              if alien.left > WIDTH:
                     alien.right = 0

def on_mouse_down(pos):
       for alien in aliens:
              if alien.collidepoint(pos):
                     aliens.remove(alien)

def create_alien():
       global Num
       aliens.append(Actor('alien'))
       last = len(aliens)
       aliens[last-1].x = randint(50, WIDTH - 50)
       aliens[last-1].y = randint(50, HEIGHT - 50)
       Num += 1
       print (len(aliens))

#main Program
#define size window
WIDTH = 1000
HEIGHT = 600
#create object
Num = 0
aliens = []
clock.schedule_interval(create_alien, 0.5)
pgzrun.go()
