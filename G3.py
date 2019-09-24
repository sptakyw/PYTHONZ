#Example 10-3
import pgzrun
from random import randint

#function for display
def draw():
       screen.fill( (100, 200, 200) )
       if StatusGame == 0:
              message = "Are you ready, press Enter key to play."
              screen.draw.text(message,topleft=(200,350),fontsize=40,color='blue')

       elif StatusGame == 1:
              for fruit in fruits:
                     fruit.draw()
              screen.draw.text("Score : "+str(Score), topleft = (10, 10),
                                fontsize=30, color='black')
              screen.draw.text( "Time : "+str(Time), topright = (850, 10),
                                fontsize=30, color='black')
              
       elif StatusGame == 2:
              screen.fill( (200, 100, 200) )
              message = "Time out, your score : "+str(Score)
              screen.draw.text(message,topleft = (220,300),
                                fontsize = 50,color = 'cyan')
              message = "Play again, press spacebar key."
              screen.draw.text(message,topleft = (180, 350),
                                fontsize = 50, color = 'cyan')

def on_mouse_down(pos, button):
       pass

def on_key_down(key):
       global StatusGame, Score, Time
       if StatusGame == 0:
              if key == keys.RETURN:
                     start_game()
       elif StatusGame == 2:
              if key == keys.SPACE:
                     start_game()

def update():
       global StatusGame,MaxFruits
       if StatusGame == 1:
              for n in range(MaxFruits):
                     fruits[n].top += speeds[n]
                     if (fruits[n].top > HEIGHT):
                            fruits[n].bottom = 0

def start_game():
       global StatusGame, Time, Score
       for n in range(MaxFruits):
              speeds[n] = randint(2, 10)
              fruits[n].pos = POS[n]
       StatusGame = 1
       Time = 0
       Score = 0
       clock.schedule_interval(time_count, 1)
       clock.schedule(time_out, MaxTime)

def time_count():
       global Time
       Time += 1

def time_out():
       global StatusGame
       StatusGame = 2
       clock.unschedule(time_count)

#Main Program
#define size window
WIDTH = 900
HEIGHT = 650

#create object
POS = [(50, 0) ,  (150, 0) , (250, 0) , (350, 0) , (450, 0) , (550, 0) , (650, 0) , (750, 0) , (850, 0)]
MaxFruits = 9
MaxTime = 10
StatusGame = 0
Score = 0
Time = 0
fruits = []
speeds = []
for n in range(MaxFruits):
       fruits.append( Actor('apple') )
       speeds.append( randint(2, 10) )
       fruits[n].pos = POS[n]

pgzrun.go()
