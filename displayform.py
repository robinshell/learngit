# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'displayform.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1077, 743)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.matplotlibwidget = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget.setGeometry(QtCore.QRect(340, 10, 731, 651))
        self.matplotlibwidget.setMinimumSize(QtCore.QSize(400, 600))
        self.matplotlibwidget.setObjectName("matplotlibwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 100, 311, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(311, 221))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1866, 579))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(60, 10, 72, 15))
        self.label.setObjectName("label")
        self.starttimehour = QtWidgets.QSpinBox(self.page)
        self.starttimehour.setGeometry(QtCore.QRect(60, 30, 46, 22))
        self.starttimehour.setMaximum(23)
        self.starttimehour.setObjectName("starttimehour")
        self.starttimeminute = QtWidgets.QSpinBox(self.page)
        self.starttimeminute.setGeometry(QtCore.QRect(130, 30, 46, 22))
        self.starttimeminute.setMaximum(59)
        self.starttimeminute.setObjectName("starttimeminute")
        self.starttimesecond = QtWidgets.QSpinBox(self.page)
        self.starttimesecond.setGeometry(QtCore.QRect(200, 30, 46, 22))
        self.starttimesecond.setMaximum(59)
        self.starttimesecond.setObjectName("starttimesecond")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 72, 15))
        self.label_2.setObjectName("label_2")
        self.endtimehour = QtWidgets.QSpinBox(self.page)
        self.endtimehour.setGeometry(QtCore.QRect(60, 80, 46, 22))
        self.endtimehour.setMaximum(23)
        self.endtimehour.setObjectName("endtimehour")
        self.endtimeminute = QtWidgets.QSpinBox(self.page)
        self.endtimeminute.setGeometry(QtCore.QRect(130, 80, 46, 22))
        self.endtimeminute.setMaximum(59)
        self.endtimeminute.setObjectName("endtimeminute")
        self.endtimesecond = QtWidgets.QSpinBox(self.page)
        self.endtimesecond.setGeometry(QtCore.QRect(200, 80, 46, 22))
        self.endtimesecond.setMaximum(59)
        self.endtimesecond.setObjectName("endtimesecond")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(60, 120, 72, 21))
        self.label_5.setObjectName("label_5")
        self.sbxdrawspeed = QtWidgets.QSpinBox(self.page)
        self.sbxdrawspeed.setGeometry(QtCore.QRect(160, 120, 46, 22))
        self.sbxdrawspeed.setMinimum(10)
        self.sbxdrawspeed.setMaximum(100)
        self.sbxdrawspeed.setObjectName("sbxdrawspeed")
        self.btnOpenFile = QtWidgets.QPushButton(self.page)
        self.btnOpenFile.setGeometry(QtCore.QRect(40, 170, 111, 28))
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.btnDownloadData = QtWidgets.QPushButton(self.page)
        self.btnDownloadData.setGeometry(QtCore.QRect(180, 170, 111, 28))
        self.btnDownloadData.setObjectName("btnDownloadData")
        self.lblShowDownloadMsg = QtWidgets.QLabel(self.page)
        self.lblShowDownloadMsg.setGeometry(QtCore.QRect(191, 210, 81, 20))
        self.lblShowDownloadMsg.setText("")
        self.lblShowDownloadMsg.setObjectName("lblShowDownloadMsg")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 302, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chbxCar1 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chbxCar1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.chbxCar1.setObjectName("chbxCar1")
        self.gridLayout_2.addWidget(self.chbxCar1, 1, 1, 1, 1)
        self.lblCar2Status = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lblCar2Status.setText("")
        self.lblCar2Status.setObjectName("lblCar2Status")
        self.gridLayout_2.addWidget(self.lblCar2Status, 2, 2, 1, 1)
        self.chbxCar2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chbxCar2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.chbxCar2.setObjectName("chbxCar2")
        self.gridLayout_2.addWidget(self.chbxCar2, 1, 2, 1, 1)
        self.lblCar1Status = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lblCar1Status.setText("")
        self.lblCar1Status.setObjectName("lblCar1Status")
        self.gridLayout_2.addWidget(self.lblCar1Status, 2, 1, 1, 1)
        self.lblCar2StayTime = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lblCar2StayTime.setText("")
        self.lblCar2StayTime.setObjectName("lblCar2StayTime")
        self.gridLayout_2.addWidget(self.lblCar2StayTime, 4, 2, 1, 1)
        self.lblCar1StayTime = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lblCar1StayTime.setText("")
        self.lblCar1StayTime.setObjectName("lblCar1StayTime")
        self.gridLayout_2.addWidget(self.lblCar1StayTime, 4, 1, 1, 1)
        self.lblCar1LastTime = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lblCar1LastTime.setText("")
        self.lblCar1LastTime.setObjectName("lblCar1LastTime")
        self.gridLayout_2.addWidget(self.lblCar1LastTime, 3, 1, 1, 1)
        self.lblCar2LastTime = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lblCar2LastTime.setText("")
        self.lblCar2LastTime.setObjectName("lblCar2LastTime")
        self.gridLayout_2.addWidget(self.lblCar2LastTime, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.ver_widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.ver_widget_3.setGeometry(QtCore.QRect(30, 400, 161, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ver_widget_3.sizePolicy().hasHeightForWidth())
        self.ver_widget_3.setSizePolicy(sizePolicy)
        self.ver_widget_3.setObjectName("ver_widget_3")
        self.layoutWidget = QtWidgets.QWidget(self.ver_widget_3)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 0, 111, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnStart = QtWidgets.QPushButton(self.layoutWidget)
        self.btnStart.setObjectName("btnStart")
        self.verticalLayout.addWidget(self.btnStart)
        self.btnStop = QtWidgets.QPushButton(self.layoutWidget)
        self.btnStop.setObjectName("btnStop")
        self.verticalLayout.addWidget(self.btnStop)
        self.btnReset = QtWidgets.QPushButton(self.layoutWidget)
        self.btnReset.setObjectName("btnReset")
        self.verticalLayout.addWidget(self.btnReset)
        self.ver_widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.ver_widget_4.setGeometry(QtCore.QRect(10, 530, 231, 151))
        self.ver_widget_4.setObjectName("ver_widget_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.ver_widget_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 10, 199, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lblShowTime = QtWidgets.QLabel(self.layoutWidget1)
        self.lblShowTime.setText("")
        self.lblShowTime.setObjectName("lblShowTime")
        self.gridLayout.addWidget(self.lblShowTime, 1, 1, 1, 1)
        self.lblShowDate = QtWidgets.QLabel(self.layoutWidget1)
        self.lblShowDate.setText("")
        self.lblShowDate.setObjectName("lblShowDate")
        self.gridLayout.addWidget(self.lblShowDate, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lblStarNums1 = QtWidgets.QLabel(self.layoutWidget1)
        self.lblStarNums1.setText("")
        self.lblStarNums1.setObjectName("lblStarNums1")
        self.gridLayout.addWidget(self.lblStarNums1, 2, 1, 1, 1)
        self.lblStarNums2 = QtWidgets.QLabel(self.layoutWidget1)
        self.lblStarNums2.setText("")
        self.lblStarNums2.setObjectName("lblStarNums2")
        self.gridLayout.addWidget(self.lblStarNums2, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.ver_widget_1 = QtWidgets.QWidget(self.centralwidget)
        self.ver_widget_1.setGeometry(QtCore.QRect(20, 50, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ver_widget_1.sizePolicy().hasHeightForWidth())
        self.ver_widget_1.setSizePolicy(sizePolicy)
        self.ver_widget_1.setObjectName("ver_widget_1")
        self.layoutWidget2 = QtWidgets.QWidget(self.ver_widget_1)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 199, 23))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(111, 20))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.cbxSelectFunction = QtWidgets.QComboBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbxSelectFunction.sizePolicy().hasHeightForWidth())
        self.cbxSelectFunction.setSizePolicy(sizePolicy)
        self.cbxSelectFunction.setMaximumSize(QtCore.QSize(111, 28))
        self.cbxSelectFunction.setObjectName("cbxSelectFunction")
        self.cbxSelectFunction.addItem("")
        self.cbxSelectFunction.addItem("")
        self.horizontalLayout.addWidget(self.cbxSelectFunction)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.cbxSelectFunction.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "开始时间:"))
        self.label_2.setText(_translate("MainWindow", "结束时间:"))
        self.label_5.setText(_translate("MainWindow", "画图速度："))
        self.btnOpenFile.setText(_translate("MainWindow", "打开文件"))
        self.btnDownloadData.setText(_translate("MainWindow", "下载数据"))
        self.chbxCar1.setText(_translate("MainWindow", "苏B-A2345"))
        self.chbxCar2.setText(_translate("MainWindow", "苏B-A5339"))
        self.label_8.setText(_translate("MainWindow", "选择车辆"))
        self.label_16.setText(_translate("MainWindow", "停留时间"))
        self.label_9.setText(_translate("MainWindow", "最后运行时间"))
        self.label_15.setText(_translate("MainWindow", "状态"))
        self.btnStart.setText(_translate("MainWindow", "开始"))
        self.btnStop.setText(_translate("MainWindow", "暂停"))
        self.btnReset.setText(_translate("MainWindow", "重置"))
        self.label_4.setText(_translate("MainWindow", "时间："))
        self.label_10.setText(_translate("MainWindow", "卫星个数2："))
        self.label_6.setText(_translate("MainWindow", "卫星个数1："))
        self.label_3.setText(_translate("MainWindow", "日期："))
        self.label_7.setText(_translate("MainWindow", "功能选择："))
        self.cbxSelectFunction.setItemText(0, _translate("MainWindow", "文件读取"))
        self.cbxSelectFunction.setItemText(1, _translate("MainWindow", "实时轨迹"))

from matplotlibwidget import MatplotlibWidget
