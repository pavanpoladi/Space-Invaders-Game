#Pavan Poladi
#12/1/2019
#This is a fun space invaders game I made using the turtle module!

import turtle
from math import*
import random

#setting up the screen
mainScreen = turtle.Screen()
mainScreen.bgcolor("black")
mainScreen.title("Space Invaders")
mainScreen.bgpic("space_invaders_background.gif")

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#Drawing border
borderPen = turtle.Turtle()
borderPen.speed(0)
borderPen.color("white")
borderPen.penup()
borderPen.setposition(-300,-300)
borderPen.pendown()
borderPen.pensize(3)
for side in range(4):
    borderPen.fd(600)
    borderPen.lt(90)
borderPen.hideturtle()

#Setting the score to 0
score = 0

#Drawing the Score
scorePen = turtle.Turtle()
scorePen.speed(0)
scorePen.color("white")
scorePen.penup()
scorePen.setposition(-290,280)
scoreString = "Score: {}".format(score)
scorePen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
scorePen.hideturtle()

#Create the player object
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90) #Changing where the player object is facing
playerSpeed = 15


#Choosing number of enemies
numberOfEnemies = 5
#Creating empty list of enemies
enemies = []


#Adding enemies to the list
for i in range(numberOfEnemies):
    # Creating the enemy objects and adding them to list of enemies
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100,250)
    enemy.setposition(x, y)
enemySpeed = 2

#Creating the player's bullet object
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletSpeed = 20


#Defining bullet states
#ready state: ready to fire
#fire state: bullet is firing
bulletState = "ready"

#Moving the player left
def move_left():
    x = player.xcor()
    x -= playerSpeed #Moving the player object 15 pixels left every time left arrow key is pressed
    if x < -280: #Checking for left bound
        x = -280
    player.setx(x)


#Moving the player right
def move_right():
    x = player.xcor()
    x += playerSpeed #Moving the player object 15 pixels right every time right arrow key is pressed
    if x > 280: #Checking for right bound
        x = 280
    player.setx(x)

def fire_bullet():
    #Declaring bulletState as a global variable if it needs to be changed
    global bulletState

    if bulletState == "ready":
        bulletState = "fire"
        #Moving bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

#Checking to see if bullet hit the enemy
def isCollision(turtle1, turtle2):
    #using pythagorean theorem to check if bullet is within a certain distance from the enemy
    distance = sqrt(pow(turtle1.xcor() - turtle2.xcor(), 2) + pow(turtle1.ycor() - turtle2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

#Creating keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


#Main game loop
while True:
    for enemy in enemies:
        #Moving the enemy
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)

        #Checking bound for enemy and bouncing off borders
        #Then moving the enemy closer to player once it hits the borders
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemySpeed *= -1

        if enemy.xcor() <-280:
            # Move all enemies down
            for i in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemySpeed *= -1

        # Checking if there is a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bullet.setposition(0, -400)

            # Reset the enemy
            enemy.setposition(-200, 250)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scoreString = "Score: {}".format(score)
            scorePen.clear()
            scorePen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))

        # Checking if there is a collision between the player and the enemy
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Moving the bullet
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)


    #Checking to see if bullet has gone to top border
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"


#Making sure the screen doesn't disappear
mainScreen.mainloop()

