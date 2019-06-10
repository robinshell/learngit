import sys
#from PyQt5.QtGui import QIcon
from PyQt5 import QtSql
from PyQt5.QtWidgets import (QApplication,QMainWindow,QFileDialog)
from displayform import *#
from PyQt5.QtCore import QTimer, QDateTime, Qt
import csv
#import pylab
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
#import time
#from matplotlib.animation import FuncAnimation

line1=[[31.543713,31.542196,31.542955,31.544502],[120.362781,120.364200,120.365329,120.363901]]
line2=[[31.543267,31.544008],[120.363223, 120.364305]]
line3=[[31.542712,31.54347],[120.363750, 120.364820]]
line4=[[31.544165,31.542606],[120.363329, 120.364826]]#这四根是地图的线
lonleft=120.362561
lonright=120.365339
latup=31.544568
latdown=31.542055#这四个是上下左右四个点谷歌经纬度
#plt.ion() #开启interactive mode 成功的关键函数
def t2s(t):
    h,m,s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)
carColors=['red','yellow','blue','green','purple','white']
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.tempfilename=""
        self.isfileopend=False
        self.isfilechanged=False
        self.starttime=0
        self.endtime=0
        self.isdrawstop=True
        self.isdrawreset=True
        self.setWindowTitle('叉车定位显示系统')
        #self.setWindowIcon(QIcon('/Forklift.ico'))
        imagepath='./mapwitharea.png'
        im3 = mpimg.imread(imagepath)
        self.matplotlibwidget.axes.imshow(im3,extent=[lonleft,lonright,latdown,latup])
        self.matplotlibwidget.axes.plot(line1[1],line1[0],c='blue')
        self.matplotlibwidget.axes.plot(line2[1],line2[0],c='blue')
        self.matplotlibwidget.axes.plot(line3[1],line3[0],c='blue')
        self.matplotlibwidget.axes.plot(line4[1],line4[0],c='blue')          
            #plt.ylim(latdown,latup )
            #plt.xlim(lonleft,lonright)
        self.matplotlibwidget.axes.set_xticks([])
        self.matplotlibwidget.axes.set_yticks([])
        #####################
        self.templon_1=0#用于1号车实时轨迹
        self.templat_1=0#用于1号车实时轨迹
        self.templon_2=0#用于2号车实时轨迹
        self.templat_2=0#用于2号车实时轨迹
        ######################
        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('101.132.150.191')
        self.db.setDatabaseName('mysql')
        self.db.setUserName('userName')
        self.db.setPassword('house')
        self.db.setPort(3306) # 端口号

        self.cbxSelectFunction.currentIndexChanged.connect(self.functionChanged)
        self.timer1=QTimer(self)
        self.timer1.timeout.connect(self.update_lines)
        self.timer2=QTimer(self)
        self.timer2.timeout.connect(self.real_time_drawing)
        
        self.btnOpenFile.clicked.connect(self.openfile)
        self.btnStart.clicked.connect(self.startDraw)
        self.btnStop.clicked.connect(self.stopDraw)
        self.btnReset.clicked.connect(self.resetDraw)
        
    def openfile(self):
        self.btnStart.setEnabled(True)
        filename, _  = QFileDialog.getOpenFileName(self, 'Open file', './data',"文本文件 (*.csv)")
        if filename=="":
            return
        if self.tempfilename==filename:#若打开的是同一个文件，则返回
            return
        self.tempfilename=filename
        self.isfileopend=True
        self.isfilechanged=True
        if self.tempfilename[-5]=="_":
            self.carindex="苏B-A5339"#第二辆车
        else:
            self.carindex="苏B-A2345"#第一辆车
        self.matplotlibwidget.fig.suptitle(self.carindex)    
        
        with open(filename) as f:
            reader = list(csv.reader(f))
            self.lat=[]#纬度数组
            self.lon=[]#经度数组
            self.times=[]
            self.time2s=[]
            self.speed=[]
            self.starnum=[]
            le = len(reader)
            endflag=0#当csv读到空行时变为当前行数，停止继续读取
            temp_time=reader[0][13]
            former_time=t2s(reader[0][13])
            self.lblShowDate.setText(str(reader[0][12]))
            try:
                for i in range(1,le):
                    if not reader[i][0]:
                        endflag = i
                        break
                    #if reader[i][10] == reader[i-1][10] and reader[i][11] == reader[i-1][11]:
                        #continue
                    
                    if int(reader[i][16])>3:
                        file_templat=float(reader[i][10])
                        file_templon=float(reader[i][11])
                        if file_templat < latup and file_templat > latdown and file_templon>lonleft and file_templon<lonright:#记录经纬度
                            self.speed.append(int(reader[i][0]))
                            self.lat.append(file_templat)
                            self.lon.append(file_templon)
                            self.times.append(reader[i][13])
                            self.time2s.append(t2s(reader[i][13]))
                            self.starnum.append(reader[i][16])
            except ValueError:
                print("the %d th line goes wrong."%i)
        self.statusbar.showMessage('文件载入成功',5000)        
            
        #plt.plot(lon[j],lat[j],c='red')
    '''启动绘制动态图'''
    def startDraw(self):
        self.timer1.stop()
        self.timer2.stop()
        if self.cbxSelectFunction.currentIndex()==0:#读文件
            
            if not self.isfileopend:#如果没有文件被打开，就直接返回
                return
            self.isdrawstop=False
            tempstarttime=self.starttimehour.value()*3600+self.starttimeminute.value()*60+self.starttimesecond.value()
            tempendtime=self.endtimehour.value()*3600+self.endtimeminute.value()*60+self.endtimesecond.value()
            if self.isfilechanged:#如果文件变了就重新画
                self.isdrawreset=True
                self.isfilechanged=False
            if self.starttime != tempstarttime or self.endtime != tempendtime:#如果起始时间变了就重新画
                self.starttime = tempstarttime
                self.endtime = tempendtime
                self.isdrawreset=True
            if self.isdrawreset:
                self.matplotlibwidget.axes.cla() 
                imagepath='./mapwitharea.png'
                im3 = mpimg.imread(imagepath)
                self.matplotlibwidget.axes.imshow(im3,extent=[lonleft,lonright,latdown,latup])
                self.matplotlibwidget.axes.plot(line1[1],line1[0],c='blue')
                self.matplotlibwidget.axes.plot(line2[1],line2[0],c='blue')
                self.matplotlibwidget.axes.plot(line3[1],line3[0],c='blue')
                self.matplotlibwidget.axes.plot(line4[1],line4[0],c='blue')          
                #plt.ylim(latdown,latup )
                #plt.xlim(lonleft,lonright)
                self.matplotlibwidget.axes.set_xticks([])
                self.matplotlibwidget.axes.set_yticks([])
                self.isdrawreset=False#只有这里能清除重置位
                
                
                #########此部分用于按输入起止时间显示##########
                if self.starttime==0 and self.endtime==0:
                    self.startindex=0
                    self.endindex=len(self.lat)-1
                elif self.starttime>=self.endtime:
                    return
                else:
                    self.startindex=0
                    self.endindex=len(self.lat)-1
                    for i in range(len(self.lat)):
                        if self.time2s[i]>=self.starttime:
                            self.startindex=i
                            break
                    for i in range(self.startindex,len(self.lat)):
                        if self.time2s[i]>self.endtime:
                            self.endindex=i
                            break 
                self.tempindex=self.startindex
                ############################################
                
            #self.update_lines()
            self.btnStart.setEnabled(False)
            self.cbxSelectFunction.setEnabled(False)
            self.drawspeed=self.sbxdrawspeed.value()    
            self.timer1.start(101-self.drawspeed)
            
        elif self.cbxSelectFunction.currentIndex()==1:
            
            if self.isdrawreset:
                self.matplotlibwidget.axes.cla() 
                imagepath='./mapwitharea.png'
                im3 = mpimg.imread(imagepath)
                self.matplotlibwidget.axes.imshow(im3,extent=[lonleft,lonright,latdown,latup])
                self.matplotlibwidget.axes.plot(line1[1],line1[0],c='blue')
                self.matplotlibwidget.axes.plot(line2[1],line2[0],c='blue')
                self.matplotlibwidget.axes.plot(line3[1],line3[0],c='blue')
                self.matplotlibwidget.axes.plot(line4[1],line4[0],c='blue')          
                #plt.ylim(latdown,latup )
                #plt.xlim(lonleft,lonright)
                self.matplotlibwidget.axes.set_xticks([])
                self.matplotlibwidget.axes.set_yticks([])
                self.isdrawreset=False#只有这里能清除重置位
                
                self.templon_1=0#用于实时轨迹
                self.templat_1=0#用于实时轨迹
                self.templon_2=0#用于实时轨迹
                self.templat_2=0#用于实时轨迹
                
            self.databasename_1='siemens_location'
            self.databasename_2='siemens_location1'
            self.carColor_1=carColors[int(self.cbxCarColor1.currentIndex())]
            self.carColor_2=carColors[int(self.cbxCarColor2.currentIndex())]
            
            self.btnStart.setEnabled(False)
            self.btnStop.setEnabled(False)
            self.cbxSelectFunction.setEnabled(False)
            self.timer2.start(1000)    
        
            #self.ani = FuncAnimation(self.matplotlibwidget.fig, self.update_lines,blit=True, interval=int(100/self.drawspeed))
            
    '''动态图的绘图逻辑可以在这里修改'''

    def update_lines(self):
        QApplication.processEvents()
        if self.tempindex <self.endindex-10:
            for i in range(self.tempindex,self.tempindex+10):
                if self.lon[i]==self.lon[i+1] and self.lat[i]==self.lat[i+1]:
                    continue
                if self.time2s[i+1]-self.time2s[i]>59:
                    continue
                if self.speed[i]<5: 
                    self.matplotlibwidget.axes.plot(self.lon[i:i+2], self.lat[i:i+2], c='r')
                elif self.speed[i]<50:
                    self.matplotlibwidget.axes.plot(self.lon[i:i+2], self.lat[i:i+2], c='orange')
                else:
                    self.matplotlibwidget.axes.plot(self.lon[i:i+2], self.lat[i:i+2], c='y')
                    
                #self.matplotlibwidget.axes.scatter(self.lon[self.tempindex:self.tempindex+11], self.lat[self.tempindex:self.tempindex+11], c='y')
                #self.matplotlibwidget.axes.plot([120.363329,120.364820],[31.542712,31.544165],c='r')
            self.matplotlibwidget.draw()
            self.lblShowTime.setText(self.times[self.tempindex])
            self.lblStarNums1.setText(self.starnum[self.tempindex])
            #self.statusbar.showMessage('测试',2000)
            self.tempindex+=10
        else:
            for i in range(self.tempindex,self.endindex-1):
                if self.lon[i]==self.lon[i+1] and self.lat[i]==self.lat[i+1]:
                    continue
                if self.speed[i]<5: 
                    self.matplotlibwidget.axes.plot(self.lon[i:i+2], self.lat[i:i+2], c='r')
                elif self.speed[i]<50:
                    self.matplotlibwidget.axes.plot(self.lon[i:i+2], self.lat[i:i+2], c='orange')
                else:
                    self.matplotlibwidget.axes.plot(self.lon[i:i+2], self.lat[i:i+2], c='y')
                    
            #self.matplotlibwidget.axes.scatter(self.lon[self.tempindex:self.endindex], self.lat[self.tempindex:self.endindex], c='r')
            self.matplotlibwidget.draw()
            self.lblShowTime.setText(self.times[self.tempindex])
            self.lblStarNums1.setText(self.starnum[self.tempindex])
            self.statusbar.showMessage('画图完毕',2000)
            self.timer1.stop()
            self.btnStart.setEnabled(True)
            self.isdrawreset=True
        
        
        
    def stopDraw(self):
        self.btnStart.setEnabled(True)
        if not self.isdrawstop:
            self.isdrawstop=True
            self.timer1.stop()
            self.timer2.stop()
            self.statusbar.showMessage('画图暂停',2000)
    def resetDraw(self):
        self.btnStart.setEnabled(True)
        self.btnStop.setEnabled(True)
        if not self.isdrawstop:
            self.isdrawstop=True
            #self.ani._stop()
        self.timer1.stop()
        self.timer2.stop()
        self.cbxSelectFunction.setEnabled(True)
        self.statusbar.showMessage('画图完毕',2000)
        self.isdrawreset=True
        
    def real_time_drawing(self):        
        #now = QDateTime.currentDateTime()
        QApplication.processEvents()
        self.timer2.stop()
        if not self.db.open():
            self.statusbar.showMessage('数据库未连接',1000)
            self.btnStart.setEnabled(True)
            #self.cbxSelectFork.setEnabled(True)
            self.cbxSelectFunction.setEnabled(True)
            self.isdrawreset=True
            return
        self.timer2.start(1000)
        if self.chbxCar1.isChecked(): 
            query_1 = QtSql.QSqlQuery("SELECT pulseCount,longitude,latitude,datetime,starnum FROM "+self.databasename_1+" ORDER BY id DESC LIMIT 1;")
            query_1.first()
            #self.statusbar.showMessage(str(query.value(0)),5000)
            curlon=float(query_1.value(1))
            curlat=float(query_1.value(2))
            #speed=int(query_1.value(0))
            datetime=query_1.value(3).toString(Qt.ISODate)
            if curlon==self.templon_1 and curlat == self.templat_1:
                pass
            elif curlon>lonleft and curlon<lonright and curlat>latdown and curlat<latup:
                if self.templon_1==0:
                    self.templon_1=curlon
                    self.templat_1=curlat
                    self.lblShowDate.setText(datetime[:10])
                else:
                    '''if speed<5: 
                        self.matplotlibwidget.axes.plot([self.templon,curlon], [self.templat,curlat], c='r')
                    elif speed<50:
                        self.matplotlibwidget.axes.plot([self.templon,curlon], [self.templat,curlat], c='orange')
                    else:'''
                    self.matplotlibwidget.axes.plot([self.templon_1,curlon], [self.templat_1,curlat], c=self.carColor_1)
                    self.matplotlibwidget.draw()
                    self.templon_1=curlon
                    self.templat_1=curlat
                self.lblStarNums1.setText(str(query_1.value(4)))
                self.lblShowTime.setText(datetime[-8:])
        if self.chbxCar2.isChecked(): 
            query = QtSql.QSqlQuery("SELECT pulseCount,longitude,latitude,datetime,starnum FROM "+self.databasename_2+" ORDER BY id DESC LIMIT 1;")
            query.first()
            #self.statusbar.showMessage(str(query.value(0)),5000)
            curlon=float(query.value(1))
            curlat=float(query.value(2))
            #speed=int(query.value(0))
            datetime=query.value(3).toString(Qt.ISODate)
            if curlon==self.templon_2 and curlat == self.templat_2:
                pass
            elif curlon>lonleft and curlon<lonright and curlat>latdown and curlat<latup:
                if self.templon_2==0:
                    self.lblShowDate.setText(datetime[:10])
                else:
                    '''if speed<5: 
                        self.matplotlibwidget.axes.plot([self.templon,curlon], [self.templat,curlat], c='r')
                    elif speed<50:
                        self.matplotlibwidget.axes.plot([self.templon,curlon], [self.templat,curlat], c='orange')
                    else:'''
                    self.matplotlibwidget.axes.plot([self.templon_2,curlon], [self.templat_2,curlat], c=self.carColor_2)
                    self.matplotlibwidget.draw()
                self.templon_2=curlon
                self.templat_2=curlat
                
                self.lblStarNums2.setText(str(query.value(4)))
                self.lblShowTime.setText(datetime[-8:])
                        
        #self.statusbar.showMessage(datetime,5000)
        #print(datetime)
        self.db.close()
        #showtime=QDateTime.currentDateTime()-now
        #showtime=showtime.toString(Qt.ISODate)
        #self.statusbar.showMessage(str(showtime),500)
    
    def functionChanged(self):
        self.stackedWidget.setCurrentIndex(self.cbxSelectFunction.currentIndex())
        self.isdrawreset=True

        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    myWin=MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
 
