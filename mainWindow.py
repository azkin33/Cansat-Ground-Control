from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from containerWindow import ContainerWindow
from payloadWindow import *
from telemetryWindow import *
import folium,io
from PyQt5 import QtWebEngineWidgets
import matplotlib.pyplot as plt
class Ui_MainWindow(object):
   containerPlotWindow = None
   payloadPlotWindow = None
   telemetryWindow = None
   form = None
   def setupUi(self, MainWindow):
      
      self.payloadPlotWindow = PayloadWindow()
      self.containerPlotWindow = ContainerWindow()
      MainWindow.setObjectName("MainWindow")
      MainWindow.resize(1096, 720)
      self.centralwidget = QtWidgets.QWidget(MainWindow)
      self.centralwidget.setObjectName("centralwidget")
      self.teamNameLabel = QtWidgets.QLabel(self.centralwidget)
      self.teamNameLabel.setGeometry(QtCore.QRect(430, 70, 181, 31))
      font = QtGui.QFont()
      font.setPointSize(17)
      self.teamNameLabel.setFont(font)
      self.teamNameLabel.setObjectName("teamNameLabel")
      self.teamNumberLabel = QtWidgets.QLabel(self.centralwidget)
      self.teamNumberLabel.setGeometry(QtCore.QRect(900, 70, 111, 31))
      font = QtGui.QFont()
      font.setPointSize(11)
      self.teamNumberLabel.setFont(font)
      self.teamNumberLabel.setObjectName("teamNumberLabel")
      self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
      self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 190, 191, 211))
      self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
      self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
      self.verticalLayout.setContentsMargins(0, 0, 0, 0)
      self.verticalLayout.setObjectName("verticalLayout")
      self.containerPlotsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
      font = QtGui.QFont()
      font.setPointSize(12)
      self.containerPlotsButton.setFont(font)
      self.containerPlotsButton.setObjectName("containerPlotsButton")

      self.containerPlotsButton.clicked.connect(self.openContainerPlots)

      self.verticalLayout.addWidget(self.containerPlotsButton)
      self.payloadPlotsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
      self.payloadPlotsButton.setEnabled(True)
      font = QtGui.QFont()
      font.setPointSize(12)
      self.payloadPlotsButton.setFont(font)
      self.payloadPlotsButton.setObjectName("payloadPlotsButton")

      self.payloadPlotsButton.clicked.connect(self.openPayloadPlots)

      self.verticalLayout.addWidget(self.payloadPlotsButton)
      self.telemetryDataButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
      font = QtGui.QFont()
      font.setPointSize(12)
      self.telemetryDataButton.setFont(font)
      self.telemetryDataButton.setObjectName("telemetryDataButton")

      self.telemetryDataButton.clicked.connect(self.openTelemetryWindow)

      self.verticalLayout.addWidget(self.telemetryDataButton)
      self.payloadWidget = QtWidgets.QWidget(self.centralwidget)
      self.payloadWidget.setGeometry(QtCore.QRect(230, 160, 300, 300))
   
      self.payloadWidget.setObjectName("payloadWidget")
      self.payloadWidget.fig = Figure()
      self.payloadWidget.canvas = FigureCanvas(self.payloadWidget.fig)
      self.payloadWidget.axes = self.payloadWidget.fig.add_subplot(111, projection='3d')
      self.payloadWidget.axes.set_xlim([-1,1])
      self.payloadWidget.axes.set_ylim([-1,1])
      self.payloadWidget.axes.set_zlim([-1,1])
      vec = [0,0,-1]
      self.payloadWidget.axes.quiver(0,0,0,0,0,-1)
      layout = QtWidgets.QVBoxLayout(self.payloadWidget)
      layout.addWidget(self.payloadWidget.canvas)



      self.gpsWidget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
      self.gpsWidget.setGeometry(QtCore.QRect(540, 160, 300, 300))
      
      
      self.gpsWidget.setObjectName("gpsWidget")
      m = folium.Map(
            location=[39.88467683221582, 32.77791281166123], zoom_start=25
        )
      folium.Marker(location=[39.88467683221582,32.77791281166123],popup='Custom Marker 1',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='red',icon='none')).add_to(m)
      data = io.BytesIO()
      m.save(data, close_file=False)
      self.gpsWidget.setHtml(data.getvalue().decode())
      m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
      
      self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
      self.gridLayoutWidget.setGeometry(QtCore.QRect(850, 180, 236, 251))
      self.gridLayoutWidget.setObjectName("gridLayoutWidget")
      self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
      self.gridLayout.setContentsMargins(0, 0, 0, 0)
      self.gridLayout.setHorizontalSpacing(60)
      self.gridLayout.setObjectName("gridLayout")
      self.ppcLabel = QtWidgets.QLabel(self.gridLayoutWidget)
      font = QtGui.QFont()
      font.setPointSize(10)
      self.ppcLabel.setFont(font)
      self.ppcLabel.setObjectName("ppcLabel")
      self.gridLayout.addWidget(self.ppcLabel, 1, 1, 1, 1)
      self.cpcLabel = QtWidgets.QLabel(self.gridLayoutWidget)
      sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(self.cpcLabel.sizePolicy().hasHeightForWidth())
      self.cpcLabel.setSizePolicy(sizePolicy)
      font = QtGui.QFont()
      font.setPointSize(10)
      self.cpcLabel.setFont(font)
      self.cpcLabel.setObjectName("cpcLabel")
      self.gridLayout.addWidget(self.cpcLabel, 0, 1, 1, 1)
      self.cpLabel = QtWidgets.QLabel(self.gridLayoutWidget)
      font = QtGui.QFont()
      font.setPointSize(10)
      self.cpLabel.setFont(font)
      self.cpLabel.setObjectName("cpLabel")
      self.gridLayout.addWidget(self.cpLabel, 0, 0, 1, 1)
      self.ppLabel = QtWidgets.QLabel(self.gridLayoutWidget)
      font = QtGui.QFont()
      font.setPointSize(10)
      self.ppLabel.setFont(font)
      self.ppLabel.setObjectName("ppLabel")
      self.gridLayout.addWidget(self.ppLabel, 1, 0, 1, 1)
      self.ssLabel = QtWidgets.QLabel(self.gridLayoutWidget)
      font = QtGui.QFont()
      font.setPointSize(10)
      self.ssLabel.setFont(font)
      self.ssLabel.setObjectName("ssLabel")
      self.gridLayout.addWidget(self.ssLabel, 2, 0, 1, 1)
      self.sscLabel = QtWidgets.QLabel(self.gridLayoutWidget)
      font = QtGui.QFont()
      font.setPointSize(10)
      self.sscLabel.setFont(font)
      self.sscLabel.setObjectName("sscLabel")
      self.gridLayout.addWidget(self.sscLabel, 2, 1, 1, 1)

      self.containerTStartButton = QtWidgets.QPushButton(self.centralwidget)
      self.containerTStartButton.setGeometry(QtCore.QRect(10, 490, 191, 31))
      font = QtGui.QFont()
      font.setPointSize(12)
      self.containerTStartButton.setFont(font)
      self.containerTStartButton.setObjectName("containerTStartButton")
      self.payloadTStartButton = QtWidgets.QPushButton(self.centralwidget)
      self.payloadTStartButton.setGeometry(QtCore.QRect(10, 560, 191, 31))
      font = QtGui.QFont()
      font.setPointSize(12)
      self.payloadTStartButton.setFont(font)
      self.payloadTStartButton.setObjectName("payloadTStartButton")

      self.saveCsvButton = QtWidgets.QPushButton(self.centralwidget)
      self.saveCsvButton.setGeometry(QtCore.QRect(10, 620, 191, 31))
      self.saveCsvButton.setObjectName("saveCsvButton")
      self.saveCsvButton.setFont(font)
      self.enableMQTT = QtWidgets.QPushButton(self.centralwidget)
      self.enableMQTT.setGeometry(QtCore.QRect(850, 620, 191, 31))
      self.enableMQTT.setObjectName("enableMQTTButton")
      self.enableMQTT.setFont(font)

      self.simEnableButton = QtWidgets.QPushButton(self.centralwidget)
      self.simEnableButton.setGeometry(QtCore.QRect(850, 490, 191, 31))
      font = QtGui.QFont()
      font.setPointSize(12)
      self.simEnableButton.setFont(font)
      self.simEnableButton.setObjectName("simEnableButton")
      self.simEnableButton_2 = QtWidgets.QPushButton(self.centralwidget)
      self.simEnableButton_2.setGeometry(QtCore.QRect(850, 550, 191, 31))
      font = QtGui.QFont()
      font.setPointSize(12)
      self.simEnableButton_2.setFont(font)
      self.simEnableButton_2.setObjectName("simEnableButton_2")
      self.commandShell = QtWidgets.QTextEdit(self.centralwidget)
      self.commandShell.setGeometry(QtCore.QRect(230, 510, 611, 121))
      self.commandShell.setObjectName("commandShell")
      self.pOrientationLabel = QtWidgets.QLabel(self.centralwidget)
      self.pOrientationLabel.setGeometry(QtCore.QRect(300, 130, 201, 31))
      font = QtGui.QFont()
      font.setPointSize(12)
      self.pOrientationLabel.setFont(font)
      self.pOrientationLabel.setObjectName("pOrientationLabel")
      self.gpsLabel = QtWidgets.QLabel(self.centralwidget)
      self.gpsLabel.setGeometry(QtCore.QRect(660, 130, 201, 31))
      font = QtGui.QFont()
      font.setPointSize(12)
      self.gpsLabel.setFont(font)
      self.gpsLabel.setObjectName("gpsLabel")
      MainWindow.setCentralWidget(self.centralwidget)
      self.menubar = QtWidgets.QMenuBar(MainWindow)
      self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 21))
      self.menubar.setObjectName("menubar")
      MainWindow.setMenuBar(self.menubar)
      self.statusbar = QtWidgets.QStatusBar(MainWindow)
      self.statusbar.setObjectName("statusbar")
      MainWindow.setStatusBar(self.statusbar)

      self.retranslateUi(MainWindow)
      QtCore.QMetaObject.connectSlotsByName(MainWindow)
      
   def retranslateUi(self, MainWindow):
      _translate = QtCore.QCoreApplication.translate
      MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
      self.teamNameLabel.setText(_translate("MainWindow", "TEAM APHELION"))
      self.teamNumberLabel.setText(_translate("MainWindow", "Team Number"))
      self.containerPlotsButton.setText(_translate("MainWindow", "Container Plots"))
      self.payloadPlotsButton.setText(_translate("MainWindow", "Payload Plots"))
      self.telemetryDataButton.setText(_translate("MainWindow", "Telemetry Data"))
      self.ppcLabel.setText(_translate("MainWindow", "0"))
      self.cpcLabel.setText(_translate("MainWindow", "0"))
      self.cpLabel.setText(_translate("MainWindow", "Container Packet Count"))
      self.ppLabel.setText(_translate("MainWindow", "Payload Packet Count"))
      self.ssLabel.setText(_translate("MainWindow", "Software State"))
      self.sscLabel.setText(_translate("MainWindow", "0"))
      self.containerTStartButton.setText(_translate("MainWindow", "Container Telemetry Start"))
      self.payloadTStartButton.setText(_translate("MainWindow", "Payload Telemetry Start"))
      self.simEnableButton.setText(_translate("MainWindow", "Simulation Enable"))
      self.simEnableButton_2.setText(_translate("MainWindow", "Simulation Activate"))
      self.saveCsvButton.setText(_translate("MainWindow", "Generate .csv"))
      self.enableMQTT.setText(_translate("MainWindow", "Enable MQTT"))
      self.pOrientationLabel.setText(_translate("MainWindow", "Payload Orientation"))
      self.gpsLabel.setText(_translate("MainWindow", "GPS"))
   
   def openContainerPlots(self):
      self.containerPlotWindow.show()
   def openPayloadPlots(self):
      self.payloadPlotWindow.show()
   def openTelemetryWindow(self):
      if self.telemetryWindow is None:
         self.telemetryWindow = QtWidgets.QWidget()
         self.form = TelemetryWindow()
         self.form.setupUi(self.telemetryWindow)
      self.telemetryWindow.show()
   def getPayloadWindow(self):
      return self.payloadPlotWindow
   def getContainerWindow(self):
      return self.containerPlotWindow
   def getTelemetryWindow(self):
      return self.form
   def xxx(self):
      return 5
