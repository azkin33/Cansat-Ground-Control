from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
class MyFigure(Figure):
    xData = []
    yData = []
    xName = []
    yName = []
    canvas = None
    ax = None
    def __init__(self,y,x):
        super().__init__(figsize =(6,6),dpi=100)
        
        self.xName = x
        self.yName = y
        self.ax = self.add_subplot(111)
        self.ax.set_xlabel(x)
        self.ax.set_ylabel(y)
        canvas = FigureCanvas(self)
        canvas.setFixedWidth(600)
        canvas.setFixedHeight(420)
    def plot(self):
        self.ax.plot(self.xData,self.yData)
    def setData(self,x,y):
        self.xData = x
        self.yData = y