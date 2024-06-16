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

# Add plot''
p1 = layout.addPlot(title="My first plot")
p2 = layout.addPlot(title="My second plot")
layout.nextRow()
p3 = layout.addPlot(title='My third plot')
p4 = layout.addPlot(title='My fourth plot')
p1.plot([1,3,2,4,3,5])
p2.plot([3,2,4,5,6,7])
p3.plot([4,3,2,1,3,1])
p4.plot([1,3,2,5,2,4])

pg.QtWidgets.QApplication.exec_()
# または
# if __name__ == '__main__':
#     pg.exec()