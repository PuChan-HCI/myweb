from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

# Call below first
app=pg.QtGui.QApplication([])
app = pg.mkQApp("Gradiant Layout Example")
layout = pg.GraphicsLayout(border=(100,100,100))
view = pg.GraphicsView()
view.setCentralItem(layout)
view.show()
view.setWindowTitle('pyqtgraph example: GraphicsLayout')
view.resize(800,600)

# Add plot
p1 = layout.addPlot(title="My first plot")
p1.plot([1,3,2,4,3,5])
p1.plot([3,2,4,5,6,7])

if __name__ == '__main__':
    pg.exec()