# Implementation of Dodecahedron Tracker based on Aruco

The use of multiple AR markers is often used to improve the accuracy of estimating object pose information. Here we show how to estimate the pose information of a dodecahedron with multiple AR markers attached to its surface using a camera.

## Building the dodecahedron
Print the dodecahedron.pdf and build a dodecahedron.

## Installation
```
pip install requirements.txt
```

## Run the program
Show the local & global pose information (use 'space' key to switch between them)
```
python ArucoDodecahedron_basic.py
```
Plot the pen tip using matplotlib (push 'p' to start/stop and 'r' to reset)
```
python DocelleDodecahedron_matplotlib.py
```
Plot the pen tip using PyQtGraph (push 'p' to start/stop)
```
python DocelleDodecahedron_matplotlib.py
```