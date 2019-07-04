# laserPlotter
Plotting laser G-Code with turtle
## What it is:
This Program lets you generate simulate G-Code for CNC-Lasers by plotting them with the Python turtle module
## What you need:
A Python 3 installation and some G-Code to plot.
## How you use it:
Open the laserPlotter.py file with your text editor, adjust the parameters, execute it, and watch the plot appear.
## Adjustable Parameters:
### drawInstantly
If this is false, the G-Code will be executed one after the other, simulating the Lasers behaviour.
If it is True, the end result will be shown immediately.
### fileName
The filename of the G-Code to open and plot.
### canvasScale
The scale by which the plot is scaled. Since G-Code is most often in mm an turtle uses pixels,
a scale of 1 would be hard to see for most application.
### xOffset
The amount the plot is shifted in x-Direction
### yOffset
The amount the plot is shifted in y-Direction
