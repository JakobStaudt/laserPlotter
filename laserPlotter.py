import turtle
import re
import random
import math

drawInstantly = False

fileName = "qrCode.nc"
canvasScale = 30

xOffset = canvasScale * -11
yOffset = canvasScale * -11

if drawInstantly:
    turtle.tracer(0, 0)

turtle.penup()
turtle.speed(0)
turtle.goto(xOffset, yOffset)

with open(fileName) as file:
    fileList = file.readlines()

for line in fileList:
    line = line.strip("\n")
    if line[:2] == "G0" or line[:2] == "G1":
        xPos = re.search("X(\d+(\.\d+)?)", line)
        if xPos != None:
            xPos = float(xPos[0][1:])
        yPos = re.search("Y(\d+(\.\d+)?)", line)
        if yPos != None:
            yPos = float(yPos[0][1:])
        if xPos != None and yPos != None:
            turtle.goto(xPos * canvasScale + xOffset, yPos * canvasScale + yOffset)
    elif line[:4] == "M106":
        turtle.pendown()
    elif line[:4] == "M107":
        turtle.penup()

turtle.update()

_ = input()
