#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:06:56 2022

@author: stephenomitoki
"""

print("7.")
      
import turtle

turtle.pensize(3) # Set pen thickness to 3 pixels
turtle.penup() # Pull the pen up
turtle.goto(-170, -25)
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("green")
turtle.circle(30, steps = 3) # Draw a triangle
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(170, -25)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("blue")
turtle.circle(30) # Draw a circle
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(-85, -25)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("yellow")
turtle.circle(30, steps = 4) # Draw a square
turtle.end_fill() # Fill the shape



turtle.color("blue")
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.write("Welcome to Python", 
  font = ("Times", 18, "bold"))
turtle.hideturtle()

turtle.done() 