from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import sys

app = pg.QtWidgets.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 20
w.show()
w.setWindowTitle('pyqtgraph example: GLScatterPlotItem')

g = gl.GLGridItem()
w.addItem(g)

vertexes = np.array([[1, 0, 0], #0
                     [0, 0, 0], #1
                     [0, 1, 0], #2
                     [0, 0, 1], #3
                     [1, 1, 0], #4
                     [1, 1, 1], #5
                     [0, 1, 1], #6
                     [1, 0, 1]])#7

faces = np.array([[1,0,7], [1,3,7],
                  [1,2,4], [1,0,4],
                  [1,2,6], [1,3,6],
                  [0,4,5], [0,7,5],
                  [2,4,5], [2,6,5],
                  [3,6,5], [3,7,5]])

colors = np.array([[1,0,0,1] for i in range(12)])

cube = gl.GLMeshItem(vertexes=vertexes, faces=faces, faceColors=colors,
                     drawEdges=True, edgeColor=(0, 0, 0, 1))

w.addItem(cube)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        pg.QtWidgets.QApplication.exec_()