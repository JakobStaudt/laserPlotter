# laserPlotter
Plotting laser G-Code with turtle
## What it is:
This Program lets you simulate G-Code for CNC-Lasers by plotting them with the Python turtle module
## What you need:
A Python 3 installation and some G-Code to plot.
## How you use it:
Open the laserPlotter.py file with your text editor, adjust the parameters, execute it, and watch the plot appear.
## Adjustable Parameters:
### drawInstantly
If this is false, the G-Code will be executed one after the other, simulating the Lasers behaviour.
If it is True, the end result will be shown immediately.
### drawTravel
If this is enabled, the Travel of the Laser will be plotted too.
### drawWaitBurn
This feature attempts to model the burn in dots that appear if the Laser is enabled and doesn't mode. If the Laser is enabled and a G4 (Wait) Command is encountered, the Turtle will draw a dot, which size corresponds to the time of waiting.
### maxBurnDia
Maximum size the waitBurn dots will have. The dots will approach this ceiling asymptotically.
### burnTimeCoefficient
Coefficient used to tune the waitBurn diameter calculation. The total Formula for waitBurn diameter is pointDia = maxBurnDia - (maxBurnDia * (e^(waitTime / -burnTimeCoefficient))).
### cutColor
The Color used for plotting Laser Cuts.
### travelColor
The Color used for plotting Laser Travel.
### travelSpeed
Speed of plotter for travel Moves. The Program determines if a move is travel with the G-Code (G0 is travel), not the Laser state.
### cutSpeed
Speed of plotter for cutting Moves. The Program determines if a move is for cutting with the G-Code (G1 is Cutting), not the Laser state.
### laserEnable
Beginning of a G-Code that means the Laser gets enabled.
Depends on your configuration which G-Code you use to enable your Laser.
### laserDisable
Beginning of a G-Code that means the Laser gets disabled.
Depends on your configuration which G-Code you use to disable your Laser.
### fileName
The filename of the G-Code to open and plot.
### canvasScale
The scale by which the plot is scaled. Since G-Code is most often in mm an turtle uses pixels,
a scale of 1 would be hard to see for most application.
### xOffset
The amount the plot is shifted in x-Direction
### yOffset
The amount the plot is shifted in y-Direction
