from PyQt5 import QtWidgets, uic
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('test.ui', self)
        self.openGLWidget.show()


def main():
    m = MainWindow()
    grid = gl.GLGridItem()
    m.openGLWidget.addItem(grid)  # <--  Works, no problem.
    pos = np.array([(0, 0, 0), (0, 1, 0)])
    size = np.array([10, 10])
    scatter_plot = gl.GLScatterPlotItem(pos=pos, size=size)
    m.openGLWidget.addItem(scatter_plot)  # <-- Throws error
    return m


if __name__ == '__main__':
    app = pg.mkQApp()
    m = main()
    m.show()
    pg.mkQApp().exec_()