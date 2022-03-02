import PyQt5 as p
from matplotlib import container
from mainWindow import *
import datetime
import numpy as np
from telemetryWindow import *
from test2 import *
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

d1 = datetime.datetime(2022,1,30,12,0,0)
d2 = datetime.datetime(2022,1,30,12,0,1)
d3 = datetime.datetime(2022,1,30,12,0,2)
d4 = datetime.datetime(2022,1,30,12,0,3)
d5 = datetime.datetime(2022,1,30,12,0,4)
d6 = datetime.datetime(2022,1,30,12,0,5)
d7 = datetime.datetime(2022,1,30,12,0,6)
d8 = datetime.datetime(2022,1,30,12,0,7)
##MODE ,TP_RELEASED,ALT,_TEMP,VOLT,GPS_TIME,LAT,LONG,ALT,SAT,SW_STATE,CMD_ECHO
containerT=[["F","R",250,18.2,4,d1,39.8849, 32.7778,3000,15,1,"CXON"]
          ,["F","R",245,18.3,5,d2,39.8849, 32.7778,2995,15,1,"CXON"]
          ,["F","R",240,18.4,4.5,d3,39.8849, 32.7778,2990,15,1,"CXON"]
          ,["F","R",235,18.4,5.5,d4,39.8849, 32.7778,2985,15,1,"CXON"]
          ,["F","R",230,18.5,4.7,d5,39.8849, 32.7778,2980,15,1,"CXON"]
          ,["F","R",225,18.4,5.2,d6,39.8849, 32.7778,2975,15,1,"CXON"]
          ,["F","R",220,18.6,5,d7,39.8849, 32.7778,2970,15,1,"CXON"]
          ,["F","R",215,18.6,4.8,d8,39.8849, 32.7778,2965,15,1,"CXON"]]
payloadT  =[[230,18.2,15,29,41,0.1,0.1,0.1,0.1,0.1,0.1,0.1,"RELEASED"],
            [225,18.1,16,30,43,0.2,0.1,0.2,0.1,0.1,0.1,0.2,"RELEASED"],
            [220,18.3,17,32,42,0.1,0 ,0.1,0.1,0.1,0.1,0.1,"RELEASED"],
            [215,18.3,16,28,39,0.1,0.1,0.1,0.1,0.1,0.1,0.2,"RELEASED"],
            [210,18.3,17,29,38,0.1,0.1,0,0.1,0.1,0.1,0.1,"RELEASED"],
            [205,18.3,16,30,40,0.1,0.1,0.1,0.1,0.1,0.1,0.1,"RELEASED"],
            [200,18.4,17,32,41,0,0,0.1,0.1,0.1,0.1,0,"RELEASED"],
            [195,18.4,16,33,42,0.1,0 ,0,0.1,0.1,0.1,0.1,"RELEASED"],]
time = [60,61,62,63,64,65,66,67]
collected = list(map(list,np.transpose(containerT)))
pollected = list(map(list,np.transpose(payloadT)))
print(collected)
cw = ui.getContainerWindow()
pw = ui. getPayloadWindow()
i = 0 
tw = ui.getTelemetryWindow()
cw.figures[0].setData(time,collected[2])
cw.figures[1].setData(time,collected[3])
cw.figures[2].setData(time,collected[4])
cw.figures[3].setData(time,collected[5])
cw.figures[4].setData(time,collected[6])
cw.figures[5].setData(time,collected[7])
cw.figures[6].setData(time,collected[8])
cw.figures[7].setData(time,collected[9])
k=0 
for i in pw.figures:
    i.setData(time,pollected[k])
    i.plot()
    k+=1
for i in cw.figures:
    i.plot()
print(p.__spec__)
app.exec_()


