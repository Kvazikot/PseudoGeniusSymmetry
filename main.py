import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsScene, \
    QGraphicsView, QGraphicsItem, QGraphicsPathItem
from PyQt5.QtCore import QRectF, Qt, QPoint
from PyQt5.uic import loadUi
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

class SimpleResizer():
    def __init__(self, item):
        self.item = item

    def resize(self, rect):
        self.item.setRect(rect)


def lin(path,p1,p2):
    path.moveTo(p1.x(),p1.y())
    path.lineTo(p2.x(),p2.y())
    #print(f'{p2[i1].x()},{p2[i1].y()} - {p2[i2].x()},{p2[i2].y()}')


class Demo(QMainWindow):
      
    def __init__(self, *args):
        super(Demo, self).__init__(*args)
        loadUi('MainWindow.ui', self)
        scene = QGraphicsScene()
        scene.setSceneRect(0,0,WINDOW_WIDTH-100,WINDOW_HEIGHT-100)
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
        
        w = 200
        h = 200
        
        R = w
        c = QPoint(350,350)
        angle = math.pi
        path = QtGui.QPainterPath()        
        lst1 = []
        lst2 = []
#draw romb
        for i in range(0,5,1):
          x = c.x() + R * math.cos(angle)
          y = c.y() + R * math.sin(angle)
          if i == 0:
            path.moveTo(x,y)
          item = scene.addText(f'A{i}')
          item.setPos(x,y)
          angle = angle + math.pi/2
          path.lineTo(x,y)
          path.moveTo(x,y)
          lst1.append(QPoint(x,y))
          print(f'{x}')
          
        # path.moveTo(c)
        # R = w
        # for i in range(0,3,1):
          # x = c.x() + R * math.cos(angle)
          # y = c.y() + R * math.sin(angle)
          # angle = angle + math.pi/2
          # path.lineTo(x,y)
          # print(f'{x}')


# draw square
        path2 = QtGui.QPainterPath()        
        path2.moveTo(c)
        R = w / math.sqrt(2)
        angle = math.pi / 4
        for i in range(0,5,1):
          x = c.x() + R * math.cos(angle)
          y = c.y() + R * math.sin(angle)
          if i == 0:
            path2.moveTo(x,y)          
          item = scene.addText(f'P{i}')
          item.setPos(x,y)
          angle = angle + math.pi/2
          path2.lineTo(x,y)
          path2.moveTo(x,y)
          lst2.append(QPoint(x,y))
          print(f'{x}')

# draw diogonals
        lin(path, lst1[1], lst1[3])
        lin(path, lst1[2], lst1[4])
        lin(path2, lst2[1], lst2[3])
        lin(path2, lst2[2], lst2[4])
        
    
        #path.addRect(20, 20, 60, 60)
        #path.moveTo(0, 0)
        #path.cubicTo(99, 0, 50, 50, 99, 99)
        #path.cubicTo(0, 99, 50, 50, 0, 0)
        path.setFillRule(Qt.OddEvenFill)

        pathItem = QGraphicsPathItem(path)
        pathItem.setFlag(QGraphicsItem.ItemIsMovable)
        scene.addItem(pathItem)

        pathItem2 = QGraphicsPathItem(path2)
        pathItem2.setFlag(QGraphicsItem.ItemIsMovable)
        scene.addItem(pathItem2)

        # rectItem = QGraphicsRectItem(QRectF(0, 0, 320, 240))
        # rectItem.setBrush(Qt.red)
        # # rectItem.setPen(Qt.NoPen)
        # rectItem.setFlag(QGraphicsItem.ItemIsMovable)
        # scene.addItem(rectItem)

        # ellipseItem = QGraphicsEllipseItem(QRectF(0, 0, 200, 200))
        # ellipseItem.setBrush(Qt.blue)
        # # ellipseItem.setPen(Qt.NoPen)
        # ellipseItem.setFlag(QGraphicsItem.ItemIsMovable)
        # scene.addItem(ellipseItem)

        graphicsView = QGraphicsView(self)
        graphicsView.setScene(scene)

        self.setCentralWidget(graphicsView)


app = QApplication(sys.argv)
screen = app.primaryScreen()
print('Screen: %s' % screen.name())
size = screen.size()
print('Size: %d x %d' % (size.width(), size.height()))
rect = screen.availableGeometry()
print('Available: %d x %d' % (rect.width(), rect.height()))
widget = Demo()
widget.setGeometry(0,0,WINDOW_WIDTH,WINDOW_HEIGHT)
widget.show()
sys.exit(app.exec_())
