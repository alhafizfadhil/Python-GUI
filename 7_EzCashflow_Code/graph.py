# Plotter Class

from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import ( NavigationToolbar2QT  as  NavigationToolbar )
from matplotlib.figure import Figure

class graph (QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self,parent)

        self.canvas = FigureCanvas(Figure())

        toolbar = NavigationToolbar(self.canvas,self)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(toolbar)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.clear()
        self.canvas.figure.tight_layout()
        self.setLayout(vertical_layout)
        self.canvas.axes.set_title("Balance Graph")
        self.canvas.figure.tight_layout()
        self.canvas.draw()