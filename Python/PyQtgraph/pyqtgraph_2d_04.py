from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

# Call below first
app=pg.QtWidgets.QApplication([])
app = pg.mkQApp("Gradiant Layout Example")
layout = pg.GraphicsLayout(border=(100,100,100))
view = pg.GraphicsView()
view.setCentralItem(layout)
view.show()
view.setWindowTitle('pyqtgraph example: GraphicsLayout')
view.resize(800,600)

# Add plot
x = np.random.normal(size=500)
y = np.random.normal(size=500)
p1 = layout.addPlot(title="My scatter plot")
p1.plot(x, y, pen=None, symbol='o')

if __name__ == '__main__':
    pg.exec()