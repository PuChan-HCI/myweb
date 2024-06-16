import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np

# Call below first
# app=pg.QtGui.QApplication([])
app=pg.QtWidgets.QApplication([])

# 2D plot
win2d = pg.GraphicsWindow(title="3D")
win2d.resize(1500,750)
win2d.setBackground('k')
plot2d = pg.PlotWidget()

# 3d plot
plot3d = gl.GLViewWidget()
plot3d.setBackgroundColor('k')

# Get the layout
# layoutgb = pg.QtGui.QGridLayout()
layoutgb = pg.QtWidgets.QGridLayout()
# win2d.setLayout(layoutgb)
layoutgb.addWidget(plot3d, 0, 0)
layoutgb.addWidget(plot2d, 0, 1)
# plot2d.sizeHint = lambda: pg.QtCore.QSize(100, 100)
# plot3d.sizeHint = lambda: pg.QtCore.QSize(100, 100)
plot3d.setSizePolicy(plot2d.sizePolicy())
win2d.setLayout(layoutgb)

# When you use void QGridLayout::addWidget(QWidget* widget,
# int fromRow, int fromColumn, int rowSpan, int columnSpan,
# Qt::Alignment alignment = 0),
# rowSpan and columnSpan refers to the other row or another column


# Plot 2D image
img = pg.ImageItem(border='w')
img.setImage(np.random.randn(30, 30))
plot2d.addItem(img)

# Plot 3D
z = pg.gaussianFilter(np.random.normal(size=(50,50)), (1,1))
photo = gl.GLSurfacePlotItem(z=z, shader='shaded', color=(0.5, 0.5, 1, 1))
plot3d.addItem(photo)

if __name__ == '__main__':
    pg.exec()