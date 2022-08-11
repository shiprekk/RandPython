#******************************************************
#   Purpose:    This program imports and uses turtle functions, coordinates and other data to display the images of a snowman with a hat and my own design of a stop sign.
#
#   Author:     Rekalyn Ware
#
#   Course:     CS 1010 B
#
#   Date:       10/20/20
#
#   Program:    myTurtle7
#
#******************************************************

import turtle

ANIMATION_SPEED = 0
BASE_X = 0
BASE_Y = -200
BASE_RADIUS = 100
MID_X = 0
MID_Y = 0
MID_RADIUS = 60

RIGHT_ARM_X1 = 60
RIGHT_ARM_Y1 = 60
RIGHT_ARM_X2 = 108
RIGHT_ARM_Y2 = 75
RIGHT_ARM_X3 = 118
RIGHT_ARM_Y3 = 75
RIGHT_ARM_X4 = 118
RIGHT_ARM_Y4 = 85

LEFT_ARM_X1 = -60
LEFT_ARM_Y1 = 60
LEFT_ARM_X2 = -105
LEFT_ARM_Y2 = 70
LEFT_ARM_X3 = -120
LEFT_ARM_Y3 = 110
LEFT_ARM_X4 = -130
LEFT_ARM_Y4 = 115
LEFT_ARM_X5 = -120
LEFT_ARM_Y5 = 125

HEAD_X = 0
HEAD_Y = 120
HEAD_RADIUS = 40

LEFT_EYE_X = -20
LEFT_EYE_Y = 170
RIGHT_EYE_X = 20
RIGHT_EYE_Y = 170
EYE_RADIUS = 5

MOUTH_START_X = -25
MOUTH_START_Y = 140
MOUTH_END_X = 25
MOUTH_END_Y = 140

HAT_X1 = -50
HAT_Y1 = 180
HAT_X2 = 50
HAT_Y2 = 180
HAT_X3 = 50
HAT_Y3 = 205
HAT_X4 = -50
HAT_Y4 = 205
HAT_X5 = -30
HAT_Y5 = 205
HAT_X6 = 30
HAT_Y6 = 205
HAT_X7 = 30
HAT_Y7 = 245
HAT_X8 = -30
HAT_Y8 = 245

def drawBase():

    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()
    turtle.circle(100)

def drawMidSection():

    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.circle(60)

def drawArms():  
    
    turtle.penup()
    turtle.goto(60,60)
    turtle.pendown()
    turtle.goto(108,75)
    turtle.goto(118,75)
    turtle.penup()
    turtle.goto(108,75)
    turtle.pendown()
    turtle.goto(118,85)
    #right arm
    
    turtle.penup()
    turtle.goto(-60,60)
    turtle.pendown()
    turtle.goto(-105,70)
    turtle.goto(-120,110)
    turtle.goto(-130,115)
    turtle.penup()
    turtle.goto(-120,110)
    turtle.pendown()
    turtle.goto(-120,125)
    #left arm

def drawHead():
    
    turtle.penup()
    turtle.goto(0,120)
    turtle.pendown()
    turtle.circle(40)
    #head
    
    turtle.penup()
    turtle.goto(-20,170)
    turtle.pendown()
    turtle.circle(5)
    #left eye
    
    turtle.penup()
    turtle.goto(20,170)
    turtle.pendown()
    turtle.circle(5)
    #right eye
    
    turtle.penup()
    turtle.goto(-25,140)
    turtle.pendown()
    turtle.goto(25,140)
    # Draw the mouth
    

def drawHat():
    
    #bottom part of the hat
    turtle.penup()
    turtle.goto(-50,180)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(50,180)
    turtle.goto(50,205)
    turtle.goto(-50,205)
    turtle.goto(-50,180)
    turtle.penup()
    turtle.goto(-30,205)
    turtle.pendown()
    turtle.goto(30,205)
    turtle.goto(30,245)
    turtle.goto(-30,245)
    turtle.goto(-30,205)
    turtle.end_fill()
    # Draw the top part of the hat
    
def snowman():
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()

def myown():
    turtle.reset()
    turtle.goto(0,0)
    turtle.circle(95)
    turtle.penup()
    turtle.goto(0,10)
    turtle.pendown()
    turtle.circle(85)
    turtle.penup()
    turtle.goto(-6,90)
    turtle.hideturtle()
    turtle.write('STOP')
    turtle.goto(-6,0)
    turtle.pendown()
    turtle.goto(-6,-200)
    turtle.penup()
    turtle.goto(6,0)
    turtle.pendown()
    turtle.goto(6,-200)
    turtle.goto(-6,-200)

def main():
    snowman()
    myown()

main()
    
