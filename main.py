import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsScene, \
    QGraphicsView, QGraphicsItem, QGraphicsPathItem
from PyQt5.QtCore import QRectF, Qt, QPoint
from PyQt5.uic import loadUi

class SimpleResizer():
    def __init__(self, item):
        self.item = item

    def resize(self, rect):
        self.item.setRect(rect)


class Demo(QMainWindow):
    def __init__(self, *args):
        super(Demo, self).__init__(*args)

        loadUi('MainWindow.ui', self)
        scene = QGraphicsScene()

        # change resolution
        # draw grid (optional)
        # add square
        # add 4 points as list
        # write func to connect list of points
        # write func to connect pairs of points
        # write func move center of list of points to new center
        # build QGraphicsPath object for every list
        # add objects to scene

        p = QPoint()
        p.setX(p.x() + 1)
        p += QPoint(1, 0)

        path = QtGui.QPainterPath()
        path.addRect(20, 20, 60, 60)
        path.moveTo(0, 0)
        path.cubicTo(99, 0, 50, 50, 99, 99)
        path.cubicTo(0, 99, 50, 50, 0, 0)
        path.setFillRule(Qt.OddEvenFill)

        pathItem = QGraphicsPathItem(path)
        pathItem.setFlag(QGraphicsItem.ItemIsMovable)
        pathItem.f
        scene.addItem(pathItem)

        rectItem = QGraphicsRectItem(QRectF(0, 0, 320, 240))
        rectItem.setBrush(Qt.red)
        # rectItem.setPen(Qt.NoPen)
        rectItem.setFlag(QGraphicsItem.ItemIsMovable)
        scene.addItem(rectItem)

        ellipseItem = QGraphicsEllipseItem(QRectF(0, 0, 200, 200))
        ellipseItem.setBrush(Qt.blue)
        # ellipseItem.setPen(Qt.NoPen)
        ellipseItem.setFlag(QGraphicsItem.ItemIsMovable)
        scene.addItem(ellipseItem)

        graphicsView = QGraphicsView(self)
        graphicsView.setScene(scene)

        self.setCentralWidget(graphicsView)


app = QApplication(sys.argv)
widget = Demo()
widget.show()
sys.exit(app.exec_())