# Draw a circle between two points
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import sys

pg.setConfigOptions(antialias=True)
app = pg.QtWidgets.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setCameraPosition(distance=15, azimuth=-90)
g = gl.GLGridItem()
w.addItem(g)

# coordinates
point1 = np.array([0, 0, 0])
point2 = np.array([0, 5, 0])
center = (point1 + point2) / 2
radius = np.linalg.norm(point2 - point1) / 2
md = gl.MeshData.sphere(rows=10, cols=20, radius=radius)
m1 = gl.GLMeshItem(
    meshdata=md,
    smooth=True,
    color=(1, 0, 0, 0.2),
    shader="balloon",
    glOptions="additive",
)
m1.translate(*center)
w.addItem(m1)

if __name__ == "__main__":
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        pg.QtWidgets.QApplication.instance().exec_()