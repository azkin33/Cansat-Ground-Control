from json.tool import main
from re import M
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from myFigure import MyFigure
class ContainerWindow(QMainWindow):
    figures = []
    def __init__(self):
        super(ContainerWindow, self).__init__()
        self.setGeometry(0,0,1000,1000)
        self.scroll = QScrollArea()             
        self.widget = QWidget()                 
        self.gbox = QtWidgets.QGridLayout()               


    
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)
        
        altFig = MyFigure("altitude (m)","time (s)")
        tempFig = MyFigure("temp (°C)","time (s)")
        voltFig = MyFigure("voltage (V)","time (s)")
        gpsTimeFig = MyFigure("gps_time ","time (s)")
        gpsLatFig = MyFigure("gps_lat (degrees)","time (s)")
        gpsLongFig = MyFigure("gps_long (degrees)","time (s)")
        gpsAltFig = MyFigure("gps_alt (degrees)","time (s)")
        gpsSatFig = MyFigure("gps_sats ","time (s)")
        self.figures=[altFig,tempFig,voltFig,
            gpsTimeFig,gpsLatFig,gpsLongFig,gpsAltFig,gpsSatFig]
        toolbar1 = NavigationToolbar(altFig.canvas, self)
        toolbar2 = NavigationToolbar(tempFig.canvas, self)
        toolbar3 = NavigationToolbar(voltFig.canvas, self)
        toolbar4 = NavigationToolbar(gpsTimeFig.canvas, self)
        toolbar5 = NavigationToolbar(gpsLatFig.canvas, self)
        toolbar6 = NavigationToolbar(gpsLongFig.canvas, self)
        toolbar7 = NavigationToolbar(gpsAltFig.canvas, self)
        toolbar8 = NavigationToolbar(gpsSatFig.canvas, self)
        self.gbox.addWidget(toolbar1,0,0)
        self.gbox.addWidget(toolbar2,0,1)
        self.gbox.addWidget(toolbar3,0,2)
        self.gbox.addWidget(toolbar4,2,0)
        self.gbox.addWidget(toolbar5,2,1)
        self.gbox.addWidget(toolbar6,2,2)
        self.gbox.addWidget(toolbar7,4,0)
        self.gbox.addWidget(toolbar8,4,1)
        self.gbox.addWidget(altFig.canvas,1,0)
        self.gbox.addWidget(tempFig.canvas,1,1)
        self.gbox.addWidget(voltFig.canvas,1,2)
        self.gbox.addWidget(gpsTimeFig.canvas,3,0)
        self.gbox.addWidget(gpsLatFig.canvas,3,1)
        self.gbox.addWidget(gpsLongFig.canvas,3,2)
        self.gbox.addWidget(gpsAltFig.canvas,5,0)
        self.gbox.addWidget(gpsSatFig.canvas,5,1)
        
        self.widget.setLayout(self.gbox)
        self.setWindowTitle("Container")
   