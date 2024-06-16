import sys

import PyQt5
from pyqtgraph.Qt import QtGui
from pyqtgraph.Qt import QtWidgets
from pyqtgraph.opengl import GLViewWidget, GLGridItem


class PrintCameraWidget(GLViewWidget):
    """Small ViewWidget which prints camera parameters"""

    def wheelEvent(self, ev):
        """Update view on zoom event"""
        super().wheelEvent(ev)
        self.get_camera_view()

    def mouseMoveEvent(self, ev):
        """Update view on move event"""
        super().mouseMoveEvent(ev)
        self.get_camera_view()

    def mouseReleaseEvent(self, ev):
        """Update view on move event"""
        super().mouseReleaseEvent(ev)
        self.get_camera_view()

    def get_camera_view(self):
        camera_params = self.cameraParams()
        print("New camera parameters: ", camera_params)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = PrintCameraWidget()
    g = GLGridItem(size=QtGui.QVector3D(100, 100, 1), color=(255, 255, 0, 100))
    w.addItem(g)

    # Create and set Camera parameters
    # camera_params = {'rotation': PyQt5.QtGui.QQuaternion(1.0, 0.0, 0.0, 0.0),
    #                  'distance': 10.0,
    #                  'fov': 60}
    camera_params = {'distance': 10.0,
                     'fov': 60}
    w.setCameraParams(**camera_params)
    print("Initial camera parameters: ", w.cameraParams())

    w.show()
    app.exec()