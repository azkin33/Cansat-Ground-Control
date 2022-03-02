import tempfile
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt, QSize
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from myFigure import MyFigure        
class PayloadWindow(QMainWindow):
    figures = []
    def __init__(self):
        super(PayloadWindow, self).__init__()

        self.setGeometry(0,0,1000,1000)
        self.scroll = QScrollArea()             
        self.widget = QWidget()                 
        self.gbox = QtWidgets.QGridLayout()               


    
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        altFig = MyFigure("tp_alt (m)","seconds")
        tempFig = MyFigure("tp_temp (°C)","seconds")
        gyroR = MyFigure("gyro_r (degrees)","seconds")
        gyroP = MyFigure("gyro_p (degrees)","seconds")
        gyroY = MyFigure("gyro_y (degrees)","seconds")
        accelrFig = MyFigure("accel_r (m/s)","seconds")
        accelpFig = MyFigure("accel_p (m/s)","seconds")
        accelyFig = MyFigure("accel_y (m/s)","seconds")
        magrFig = MyFigure("mag_r","seconds")
        magpFig = MyFigure("mag_p","seconds")
        magyFig = MyFigure("mag_y","seconds")
        errorFig = MyFigure("pointing_error","seconds")
        self.figures=[altFig,tempFig,gyroR,gyroP,gyroY,accelrFig,
            accelpFig,accelyFig,magrFig,magpFig,errorFig]
        toolbar1 = NavigationToolbar(altFig.canvas, self)
        toolbar2 = NavigationToolbar(tempFig.canvas, self)
        toolbar3 = NavigationToolbar(gyroR.canvas, self)
        toolbar4 = NavigationToolbar(gyroP.canvas, self)
        toolbar5 = NavigationToolbar(gyroY.canvas, self)
        toolbar6 = NavigationToolbar(accelrFig.canvas, self)
        toolbar7 = NavigationToolbar(accelpFig.canvas, self)
        toolbar8 = NavigationToolbar(accelyFig.canvas, self)
        toolbar9 = NavigationToolbar(magrFig.canvas, self)
        toolbar10 = NavigationToolbar(magpFig.canvas, self)
        toolbar11 = NavigationToolbar(magyFig.canvas, self)
        toolbar12 = NavigationToolbar(errorFig.canvas, self)
        self.gbox.addWidget(toolbar1,0,0)
        self.gbox.addWidget(toolbar2,0,1)
        self.gbox.addWidget(toolbar3,0,2)
        self.gbox.addWidget(toolbar4,2,0)
        self.gbox.addWidget(toolbar5,2,1)
        self.gbox.addWidget(toolbar6,2,2)
        self.gbox.addWidget(toolbar7,4,0)
        self.gbox.addWidget(toolbar8,4,1)
        self.gbox.addWidget(toolbar9,4,2)
        self.gbox.addWidget(toolbar7,6,0)
        self.gbox.addWidget(toolbar8,6,1)
        self.gbox.addWidget(toolbar9,6,2)
        self.gbox.addWidget(toolbar10,8,0)
        self.gbox.addWidget(toolbar11,8,1)
        self.gbox.addWidget(toolbar12,8,2)
        
        self.gbox.addWidget(altFig.canvas,1,0)
        self.gbox.addWidget(tempFig.canvas,1,1)
        self.gbox.addWidget(gyroR.canvas,1,2)
        self.gbox.addWidget(gyroP.canvas,3,0)
        self.gbox.addWidget(gyroY.canvas,3,1)
        self.gbox.addWidget(accelrFig.canvas,3,2)
        self.gbox.addWidget(accelpFig.canvas,5,0)
        self.gbox.addWidget(accelyFig.canvas,5,1)
        self.gbox.addWidget(magrFig.canvas,5,2)
        self.gbox.addWidget(magpFig.canvas,7,0)
        self.gbox.addWidget(magyFig.canvas,7,1)
        self.gbox.addWidget(errorFig.canvas,7,2)


        self.widget.setLayout(self.gbox)
        self.setWindowTitle("Payload")