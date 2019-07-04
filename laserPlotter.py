import turtle
import re
import random
import math

drawInstantly = False
drawTravel = True
drawWaitBurn = True
maxBurnDia = 2
burnTimeCoefficient = 800
cutColor = "black"
travelColor = "red"

laserEnable = "M106"
laserDisable = "M107"

fileName = "qrCode.nc"
canvasScale = 30

xOffset = canvasScale * -11
yOffset = canvasScale * -11



if drawInstantly:
    turtle.tracer(0, 0)

turtle.penup()
laserEnabled = False
turtle.speed(0)
turtle.goto(xOffset, yOffset)

with open(fileName) as file:
    fileList = file.readlines()

for line in fileList:
    line = line.strip("\n")
    if line.startswith("G0") or line.startswith("G1"):
        xPos = re.search("X(\d+(\.\d+)?)", line)
        if xPos != None:
            xPos = float(xPos[0][1:])
        yPos = re.search("Y(\d+(\.\d+)?)", line)
        if yPos != None:
            yPos = float(yPos[0][1:])
        if xPos != None and yPos != None:
            turtle.goto(xPos * canvasScale + xOffset, yPos * canvasScale + yOffset)
    elif line.startswith("G4") and laserEnabled and drawWaitBurn:
        waitTime = re.search("P\d+", line)
        if waitTime != None:
            waitTime = int(waitTime[0][1:])
            pointDia = maxBurnDia - (maxBurnDia * (math.e ** (waitTime / -burnTimeCoefficient)))
            turtle.dot(pointDia * canvasScale)
    elif line.startswith(laserEnable):
        laserEnabled = True
        if drawTravel:
            turtle.color("black")
        turtle.pendown()
    elif line.startswith(laserDisable):
        laserEnabled = False
        if drawTravel:
            turtle.color("red")
        else:
            turtle.penup()

turtle.update()

_ = input()
