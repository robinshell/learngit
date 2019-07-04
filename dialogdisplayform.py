# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogdisplayform.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogReadFile(object):
    def setupUi(self, DialogReadFile):
        DialogReadFile.setObjectName("DialogReadFile")
        DialogReadFile.resize(504, 396)
        self.comboBox = QtWidgets.QComboBox(DialogReadFile)
        self.comboBox.setGeometry(QtCore.QRect(330, 50, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(DialogReadFile)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(DialogReadFile)
        self.label_5.setGeometry(QtCore.QRect(340, 100, 151, 121))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget = QtWidgets.QTabWidget(DialogReadFile)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 311, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 40, 291, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.btnReadFileSet = QtWidgets.QPushButton(self.tab)
        self.btnReadFileSet.setGeometry(QtCore.QRect(100, 280, 111, 41))
        self.btnReadFileSet.setObjectName("btnReadFileSet")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 251, 16))
        self.label_3.setObjectName("label_3")
        self.leFirstDate = QtWidgets.QLineEdit(self.tab_2)
        self.leFirstDate.setGeometry(QtCore.QRect(10, 50, 113, 21))
        self.leFirstDate.setObjectName("leFirstDate")
        self.leLastDate = QtWidgets.QLineEdit(self.tab_2)
        self.leLastDate.setGeometry(QtCore.QRect(150, 50, 113, 21))
        self.leLastDate.setObjectName("leLastDate")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(130, 50, 21, 16))
        self.label_4.setObjectName("label_4")
        self.btnDownloadPeriodData = QtWidgets.QPushButton(self.tab_2)
        self.btnDownloadPeriodData.setGeometry(QtCore.QRect(80, 110, 111, 41))
        self.btnDownloadPeriodData.setObjectName("btnDownloadPeriodData")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(DialogReadFile)
        self.tabWidget.setCurrentIndex(0)
        self.btnReadFileSet.clicked.connect(DialogReadFile.close)
        self.btnDownloadPeriodData.clicked.connect(DialogReadFile.close)
        QtCore.QMetaObject.connectSlotsByName(DialogReadFile)

    def retranslateUi(self, DialogReadFile):
        _translate = QtCore.QCoreApplication.translate
        DialogReadFile.setWindowTitle(_translate("DialogReadFile", "Dialog"))
        self.comboBox.setItemText(0, _translate("DialogReadFile", "苏B-A2345"))
        self.comboBox.setItemText(1, _translate("DialogReadFile", "苏B-A5339"))
        self.label_2.setText(_translate("DialogReadFile", "选择车辆"))
        self.label_5.setText(_translate("DialogReadFile", "注：允许下载单日数据或者批量下载一段时间数据。可以同时下载数据和从文件中读取叉车轨迹显示。但请不要同时下载数据和实时轨迹显示。"))
        self.label.setText(_translate("DialogReadFile", "选择单日日期"))
        self.btnReadFileSet.setText(_translate("DialogReadFile", "下载单日数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DialogReadFile", "下载单日数据"))
        self.label_3.setText(_translate("DialogReadFile", "选择日期区间(日期格式如20190601)"))
        self.label_4.setText(_translate("DialogReadFile", "至"))
        self.btnDownloadPeriodData.setText(_translate("DialogReadFile", "下载批量数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DialogReadFile", "批量下载数据"))

