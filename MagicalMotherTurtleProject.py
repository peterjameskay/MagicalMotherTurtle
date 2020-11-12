#Imports
import turtle
import time
import random

#Global Variables (Sorry, this one needed to be global)
babies = []

#These next "setups" needed to be without functions so I could use them in all other functions
#Screen Setup
screen = turtle.Screen()
screen.title('Magical Mother Turtle')
screen.bgcolor('blue')
screen.setup(600,600)
screen.tracer(0)

#Mom Turtle Setup
mom = turtle.Turtle()
mom.speed(0)
mom.shape('turtle')
mom.color('green')
mom.penup()
mom.goto(0, 100)
mom.direction = "stop"

#Egg Setup
egg = turtle.Turtle()
egg.speed(0)
egg.shape('circle')
egg.color('white')
egg.penup()
egg.shapesize(0.75, 0.50)
egg.goto(0,0)

#Score Setup
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

#Movement Config
def move():
    if mom.direction == 'up':
        y = mom.ycor()
        mom.sety(y + 15)
    elif mom.direction == 'down':
        y = mom.ycor()
        mom.sety(y - 15)
    elif mom.direction == 'right':
        x = mom.xcor()
        mom.setx(x + 15)
    elif mom.direction == 'left':
        x = mom.xcor()
        mom.setx(x - 15)
        
def go_up():
    if mom.direction != "down":
        mom.direction = "up"
def go_down():
    if mom.direction != "up":
        mom.direction = "down"
def go_right():
    if mom.direction != "left":
        mom.direction = "right"
def go_left():
    if mom.direction != "right":
        mom.direction = "left"          
  
#Collision, Score and Hatching  
def eggs_to_babies(color):
    #Determine Scores
    score_game = len(babies)
    high_score_game = 0
    if score_game > high_score_game:
        high_score_game = score_game + 1
    #Collision from Egg
    if mom.distance(egg) < 15:
        x = random.randint(-280, 280)
        y = random.randint(-280, 240)
        egg.goto(x, y)
        #Baby Setup
        baby = turtle.Turtle()
        baby.speed(0)
        baby.shape("turtle")
        baby.color(color[random.randint(0,6)])
        baby.penup()
        #Adding Baby to Babies List
        babies.append(baby)
        #Update Score
        pen.clear()
        pen.write("Eggs: " + str(len(babies)) + "                               " , align="center", font=("Arial", 24, "normal"))
        #Babies "Hatching", leaving baby turtles on screen
        for index in range(len(babies)-1, 0, -1):
            x = babies[index-1].xcor()
            y = babies[index-1].ycor()
            babies[index].goto(x, y)
        if len(babies) > 0:
            x = mom.xcor()
            y = mom.ycor()
            babies[0].goto(x, y)
 
#Determine Level to increase speed of Mom Turtle            
def level(length):
    if length <= 10:
        return len(babies) / 100
    else:
        return 10 / 100


#Movement Config Attaching to Keys
def key_config():
    screen.listen()
    screen.onkey(go_up, "w")
    screen.onkey(go_down, "s")
    screen.onkey(go_right, "d")
    screen.onkey(go_left, "a")

#Defining Main Gameframe
def main():
    #Determining High Score and Play Again
    color_list = ['red', 'pink', 'lime', 'yellow', 'orange', 'purple', 'brown']
    delay = 0.13
    high_score = 0
    play_again = 'Y'
    #Game Loop 1 - Initalizing
    while play_again != 'N':
        game_over = False
        mom.direction = "stop"
        pen.clear()
        pen.write("Eggs: 0                                ", align="center", font=("Arial", 24, "normal"))
        #Game Loop 2 - Playing
        while game_over != True:
            #Determine Current Score and updating High Score
            score = len(babies)
            if score > high_score:
                high_score = score
            #Run Game and Functions
            key_config()
            screen.update()
            move()
            eggs_to_babies(color_list)
            total_time = delay - (level(len(babies)))
            time.sleep(total_time)
            #Set Boundries and Determine "Game Over"
            if mom.xcor() > 295 or mom.xcor() < -300 or mom.ycor() > 295 or mom.ycor() < -295:
                time.sleep(2)
                mom.goto(0, 0)
                mom.direction = "stop"
                game_over = True
        #Game Over Statement
        if game_over == True:
            mom.goto(0,100)
            pen.clear()
            pen.write("Eggs: "+ str(score) +"          High Score: " + str(high_score), align="center", font=("Arial", 24, "normal"))
            score = 0
            babies.clear()
            play_again = input('Press any key and then enter to play again, type \'N\' to quit\n')
            time.sleep(1)
    return 'Thanks for playing! Play again!'
                
    
    
#Call Game
print(main())