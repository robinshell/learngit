import sys
#import random
import matplotlib
#import csv
#import pylab
#from datetime import datetime
#import matplotlib.image as mpimg
#import time
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation

class MatplotlibWidget(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None):
        #super(MatplotlibWidget,self).__init__(parent)

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        #self.layout=QVBoxLayout(self)
        self.fig = Figure([10,5.6])  # 新建一个figure
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改
        #self.axes.imshow(im3,extent=[lonleft,lonright,latdown,latup])
        #self.axes.plot(line1[1],line1[0],c='blue')
        #self.axes.plot(line2[1],line2[0],c='blue')
        #self.axes.plot(line3[1],line3[0],c='blue')
        #self.axes.plot(line4[1],line4[0],c='blue')          
        #plt.ylim(latdown,latup )
        #plt.xlim(lonleft,lonright)
        self.axes.set_xticks([])
        self.axes.set_yticks([])
        #plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #self.layout.addWidget(self.fig)
        #self.axes.show()
   
    
    
       












    



