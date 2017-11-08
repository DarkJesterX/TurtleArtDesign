#MainFile.py
import turtle

bob = turtle.Turtle ()
bob.speed (0)#Sets the speed to the fastest.

from DesignFunctions import * #Imports every function from my function file.

turtle.bgcolor("black")#Sets the background to black.

jump (bob, 0, 0)
for times in range (5): #Repeats these codes 7 times.
    sun (bob, "red", 18) #This calls the function sun and it accepts the turtle name, color, and distance as its parameters.
    jump (bob, 0, 0) #This makes it so that the pen moves to 0,0 without the pen drawing an unnecessary lines.
    sun (bob, "orange", 18)
    jump (bob, 0, 0)
    sun (bob, "yellow", 18)
    jump (bob, 0, 0)
    sun (bob, "green", 18)
    jump (bob, 0, 0)
    sun (bob, "blue", 18)
    jump (bob, 0, 0)
    sun (bob, "indigo", 18)
    jump (bob, 0, 0)
    sun (bob, "purple", 18)
    jump (bob, 0, 0)

jump (bob, -30, 480)
for times in range(15):
    design (bob, "red", 45, 50, 55, 100, 150, 200)
    design (bob, "orange",45, 50, 55, 100, 150, 200)
    design (bob, "yellow",45, 50, 55, 100, 150, 200)
    design (bob, "green", 45, 50, 55, 100, 150, 200)
    design (bob, "blue", 45, 50, 55, 100, 150, 200)
    design (bob, "indigo", 45, 50, 55, 100, 150, 200)
    design (bob, "purple", 45, 50, 55, 100, 150, 200) #This calls the function design from the other file and it accepts the turtle name, color, angle, angle2, angle3, dist, dist2, dist3 as its parameters.

jump (bob, 0, 0)
for times in range (20):
    jump (bob, 0, 0)
    coolcircle (bob, "white", 1, 30, 100) #I called the function coolcircle from my other file which accepts turtle, color, radius, distance, and angle as its parameters.
    bob.left (5)
 
