import turtle
import re
import random
import math

# draw slowly or show image immediately?
drawInstantly = False
# show lines where Laser is off?
drawTravel = True
# Draw Points where Laser is on and not moving?
drawWaitBurn = True
# ceiling of burn dot diameter
maxBurnDia = 2
# coefficient for burn dot diameter calculations
burnTimeCoefficient = 800
# color used for plotting when Laser is enabled
cutColor = "black"
# color used for plotting when Laser is disabled (and drawTravel is True)
travelColor = "red"
# speed for plotting travel Moves (based on G-Code G0, not Laser state)
travelSpeed = 0
# speed for plotting cutting Moves (based on G-Code G1, not Laser state)
cutSpeed = 1

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
turtle.speed(travelSpeed)
turtle.goto(xOffset, yOffset)

with open(fileName) as file:
    fileList = file.readlines()

for line in fileList:
    line = line.strip("\n")
    if line.startswith("G0") or line.startswith("G1"):
        travel = False
        if line.startswith("G0"):
            travel = True
        print(travel)
        xPos = re.search("X(\d+(\.\d+)?)", line)
        if xPos != None:
            xPos = float(xPos[0][1:])
        yPos = re.search("Y(\d+(\.\d+)?)", line)
        if yPos != None:
            yPos = float(yPos[0][1:])
        if xPos != None and yPos != None:
            if travel:
                turtle.speed(travelSpeed)
            else:
                turtle.speed(cutSpeed)
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
