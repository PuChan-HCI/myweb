import sys
import multiprocessing as mp

import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QQuaternion, QVector3D, QVector4D
from PyQt5.QtCore import QTimer
import pyqtgraph.opengl as gl


...
q = QQuaternion(1, 2, 3, 4).normalized()
axis, angle = q.getAxisAndAngle()

mesh = gl.GLMeshItem(...)
mesh.resetTransform()
mesh.rotate(angle, axis.x(), axis.y(), axis.z())
...