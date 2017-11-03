#Defines the function polygon.
from Jump import *

def polygon (t, dist, sides):
    t.begin_fill ()
    angle = 360/sides
    for times in range (sides):
        t.forward (dist)
        t.left (angle)
    t.end_fill ()
 
def angle (t, angle):
  t.left (angle)

def straight (t, dist):
    t.forward (dist)

#This function calls the other defined functions.
def sun (t, color, dist):
    for times in range (37):
        t.color (color)
        polygon (t, 10, 3)
        angle (t, 10)
        t.forward (dist)

def design (t, color, angle, angle2, angle3, dist, dist2, dist3):
    for times in range(1):
        t.color (color)
        t.forward(dist)
        t.right(angle)
        t.forward(dist2)
        t.left(angle2)
        t.forward(dist3)
        t.right(angle3)

def coolcircle (t, color, radius, angle, dist):
    for times in range (10):
        t.color (color)
        t.circle (radius)
        t.forward (dist)
        t.left (angle)

def jump (t, x, y):
   t.penup ()
   t.goto (x, y)
   t.pendown ()

