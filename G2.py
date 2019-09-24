#Example 10-2
import pgzrun
from random import randint

#function for display
def draw():
       screen.blit( 'backdrop800' ,(0,0) )
       ship.draw()
       alien.draw()
       for bullet in bullets:
              bullet.draw()
       screen.draw.text( "Bullet : " +str(len(bullets)),
                         topleft = (10,10),fontsize = 28 , color = 'white')

def on_key_down(key):
       if key == keys.SPACE:
              bullets.append( Actor('bullet') )
              last = len(bullets)
              bullets[last-1].pos = ship.pos

def update():
       #check key for move ship
       if keyboard.LEFT:
              ship.x -= 1
              if ship.left < 0:
                     ship.left = 0
       elif keyboard.RIGHT:
              ship.x += 1
              if ship.right > WIDTH:
                     ship.right = WIDTH
       #move bullets
       for bullet in bullets:
              bullet.y -= 1
              if bullet.top < 0:
                     bullets.remove( bullet )
       #move alien
       alien.left += 1
       if alien.left > WIDTH:
              alien.right = 0

       #collision alien
       for bullet in bullets:
              if bullet.y < 100:
                   if  bullet.colliderect(alien) :
                            alien.pos = (60,30)
                            bullets.remove(bullet)

#Main Program
#define size window
WIDTH = 800
HEIGHT = 600

#create object
ship = Actor('ship')
ship.pos = (WIDTH/2, HEIGHT-40)
bullets = []
alien = Actor('alien')
alien.pos = (400,30)
pgzrun.go()
              
