import pyqtgraph as pg

# または
# from PyQt5 import QtWidgets
# この場合
# app=QtWidgets.QApplication([])
# となる

import pyqtgraph.opengl as gl
import numpy as np
from numpy import *
import cv2

# Call below first
app=pg.QtWidgets.QApplication([])

# Define Z
pi=3.1415
X=linspace(-10,10,100)
Y1=2+sin(X)
Y2=-2+Y1*Y1
Y3=cos(1*Y1)/(X+0.0131415)
Z=exp(-0.1*X*X)*cos(0.3*(X.reshape(100,1)**2+X.reshape(1,100)**2))

# View widget
widget = gl.GLViewWidget()

# Draw Grid
gx = gl.GLGridItem()
gx.rotate(90, 0, 1, 0)
gx.translate(-10, 0, 0)
widget.addItem(gx)
gy = gl.GLGridItem()
gy.rotate(90, 1, 0, 0)
gy.translate(0, -10, 0)
widget.addItem(gy)
gz = gl.GLGridItem()
gz.translate(0, 0, -10)
widget.addItem(gz)

# Scatter plot
Z=zeros(size(X))
p=array([X,Y2,Z])
p=p.transpose()
C=pg.glColor('b')   # Blue
point3d = gl.GLScatterPlotItem(pos=p, color=C)
widget.addItem(point3d)

# Line plot
# Z=zeros(size(X))
q=array([X,Z,Y3])
q=q.transpose()
C=pg.glColor('r')   # Red
line3d = gl.GLLinePlotItem(pos=q, width=1, color=C, antialias=False)
widget.addItem(line3d)

# Draw image
src = cv2.imread('Lenna.png')
src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
img = pg.makeRGBA(src, levels=[0,255])[0]
#
image1 = gl.GLImageItem(img)
scale = 0.01
image1.scale(scale,scale,scale)
image1.translate(-src.shape[0]*scale/2, -src.shape[1]*scale/2, 0)
image1.rotate(90, 0,1,0)
# image1.rotate(-90, 0,1,0)
widget.addItem(image1)
#
image2 = gl.GLImageItem(img)
scale = 0.04
image2.scale(scale,scale,scale)
image2.translate(-src.shape[0]*scale/2, -src.shape[1]*scale/2, -30)
image2.rotate(90, 0,1,0)
# image2.rotate(-90, 1,0,0)
widget.addItem(image2)
#
# #
# image3 = gl.GLImageItem(img)
# scale = 0.01
# image3.scale(scale,scale,scale)
# image3.translate(-src.shape[0]*scale/2, -src.shape[1]*scale/2, 0)
# widget.addItem(image3)

# Show widget
widget.show()



pg.QtWidgets.QApplication.exec_()
# または
# if __name__ == '__main__':
#     pg.exec()