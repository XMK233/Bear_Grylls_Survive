# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\XMK1\AnacondaProjects\main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 727)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 841, 701))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.MingQueAdd = QtWidgets.QPushButton(self.tab)
        self.MingQueAdd.setGeometry(QtCore.QRect(310, 60, 75, 51))
        self.MingQueAdd.setObjectName("MingQueAdd")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(450, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(440, 110, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(440, 190, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(440, 270, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(440, 360, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(490, 500, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 320, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(40, 350, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.BMingQueAdd = QtWidgets.QPushButton(self.tab)
        self.BMingQueAdd.setGeometry(QtCore.QRect(300, 320, 75, 101))
        self.BMingQueAdd.setObjectName("BMingQueAdd")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Calculate = QtWidgets.QPushButton(self.tab)
        self.Calculate.setGeometry(QtCore.QRect(90, 610, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Calculate.setFont(font)
        self.Calculate.setObjectName("Calculate")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(390, 10, 20, 631))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.MingQueRecord = QtWidgets.QListWidget(self.tab)
        self.MingQueRecord.setGeometry(QtCore.QRect(20, 130, 256, 121))
        self.MingQueRecord.setObjectName("MingQueRecord")
        self.BMingQueRecord = QtWidgets.QListWidget(self.tab)
        self.BMingQueRecord.setGeometry(QtCore.QRect(10, 470, 256, 121))
        self.BMingQueRecord.setObjectName("BMingQueRecord")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(40, 410, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 60, 135, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MingQueTNT = QtWidgets.QLineEdit(self.layoutWidget)
        self.MingQueTNT.setObjectName("MingQueTNT")
        self.verticalLayout.addWidget(self.MingQueTNT)
        self.MingQueQuantity = QtWidgets.QLineEdit(self.layoutWidget)
        self.MingQueQuantity.setObjectName("MingQueQuantity")
        self.verticalLayout.addWidget(self.MingQueQuantity)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 324, 135, 100))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BMingQueDiameter = QtWidgets.QLineEdit(self.layoutWidget1)
        self.BMingQueDiameter.setText("")
        self.BMingQueDiameter.setObjectName("BMingQueDiameter")
        self.verticalLayout_2.addWidget(self.BMingQueDiameter)
        self.BMingQueLength = QtWidgets.QLineEdit(self.layoutWidget1)
        self.BMingQueLength.setText("")
        self.BMingQueLength.setObjectName("BMingQueLength")
        self.verticalLayout_2.addWidget(self.BMingQueLength)
        self.BMingQueHeadLength = QtWidgets.QLineEdit(self.layoutWidget1)
        self.BMingQueHeadLength.setText("")
        self.BMingQueHeadLength.setObjectName("BMingQueHeadLength")
        self.verticalLayout_2.addWidget(self.BMingQueHeadLength)
        self.BMingQueQuantity = QtWidgets.QLineEdit(self.layoutWidget1)
        self.BMingQueQuantity.setObjectName("BMingQueQuantity")
        self.verticalLayout_2.addWidget(self.BMingQueQuantity)
        self.MingQueClear = QtWidgets.QPushButton(self.tab)
        self.MingQueClear.setGeometry(QtCore.QRect(310, 160, 75, 51))
        self.MingQueClear.setObjectName("MingQueClear")
        self.BMingQueClear = QtWidgets.QPushButton(self.tab)
        self.BMingQueClear.setGeometry(QtCore.QRect(300, 510, 75, 51))
        self.BMingQueClear.setObjectName("BMingQueClear")
        self.ResultTotal = QtWidgets.QLabel(self.tab)
        self.ResultTotal.setGeometry(QtCore.QRect(620, 100, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResultTotal.setFont(font)
        self.ResultTotal.setText("")
        self.ResultTotal.setObjectName("ResultTotal")
        self.ResultTNT = QtWidgets.QLabel(self.tab)
        self.ResultTNT.setGeometry(QtCore.QRect(620, 180, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResultTNT.setFont(font)
        self.ResultTNT.setText("")
        self.ResultTNT.setObjectName("ResultTNT")
        self.ResultBarrier = QtWidgets.QLabel(self.tab)
        self.ResultBarrier.setGeometry(QtCore.QRect(620, 270, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResultBarrier.setFont(font)
        self.ResultBarrier.setText("")
        self.ResultBarrier.setObjectName("ResultBarrier")
        self.ResultAlert = QtWidgets.QLabel(self.tab)
        self.ResultAlert.setGeometry(QtCore.QRect(620, 350, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResultAlert.setFont(font)
        self.ResultAlert.setText("")
        self.ResultAlert.setObjectName("ResultAlert")
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.MingQueAdd.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_7.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.BMingQueAdd.raise_()
        self.label_4.raise_()
        self.Calculate.raise_()
        self.line.raise_()
        self.MingQueRecord.raise_()
        self.BMingQueRecord.raise_()
        self.label_19.raise_()
        self.MingQueClear.raise_()
        self.BMingQueClear.raise_()
        self.ResultTotal.raise_()
        self.ResultTNT.raise_()
        self.ResultBarrier.raise_()
        self.ResultAlert.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.toolBox = QtWidgets.QToolBox(self.tab_2)
        self.toolBox.setGeometry(QtCore.QRect(20, 30, 801, 581))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 801, 500))
        self.page.setObjectName("page")
        self.Table1 = QtWidgets.QTableWidget(self.page)
        self.Table1.setGeometry(QtCore.QRect(30, 40, 301, 411))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Table1.setFont(font)
        self.Table1.setObjectName("Table1")
        self.Table1.setColumnCount(2)
        self.Table1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Table1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table1.setHorizontalHeaderItem(1, item)
        self.ThermoRemove = QtWidgets.QPushButton(self.page)
        self.ThermoRemove.setGeometry(QtCore.QRect(510, 210, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThermoRemove.setFont(font)
        self.ThermoRemove.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ThermoRemove.setObjectName("ThermoRemove")
        self.ThermoAdd = QtWidgets.QPushButton(self.page)
        self.ThermoAdd.setGeometry(QtCore.QRect(500, 60, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThermoAdd.setFont(font)
        self.ThermoAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ThermoAdd.setObjectName("ThermoAdd")
        self.ThermoSave = QtWidgets.QPushButton(self.page)
        self.ThermoSave.setGeometry(QtCore.QRect(510, 360, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThermoSave.setFont(font)
        self.ThermoSave.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ThermoSave.setObjectName("ThermoSave")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 801, 500))
        self.page_2.setObjectName("page_2")
        self.Table2 = QtWidgets.QTableWidget(self.page_2)
        self.Table2.setGeometry(QtCore.QRect(10, 20, 641, 461))
        self.Table2.setObjectName("Table2")
        self.Table2.setColumnCount(6)
        self.Table2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Table2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table2.setHorizontalHeaderItem(5, item)
        self.AnimalRemove = QtWidgets.QPushButton(self.page_2)
        self.AnimalRemove.setGeometry(QtCore.QRect(670, 220, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AnimalRemove.setFont(font)
        self.AnimalRemove.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnimalRemove.setObjectName("AnimalRemove")
        self.AnimalAdd = QtWidgets.QPushButton(self.page_2)
        self.AnimalAdd.setGeometry(QtCore.QRect(670, 80, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AnimalAdd.setFont(font)
        self.AnimalAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnimalAdd.setObjectName("AnimalAdd")
        self.AnimalSave = QtWidgets.QPushButton(self.page_2)
        self.AnimalSave.setGeometry(QtCore.QRect(670, 360, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AnimalSave.setFont(font)
        self.AnimalSave.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnimalSave.setObjectName("AnimalSave")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 801, 500))
        self.page_3.setObjectName("page_3")
        self.Table3 = QtWidgets.QTableWidget(self.page_3)
        self.Table3.setGeometry(QtCore.QRect(10, 20, 641, 461))
        self.Table3.setObjectName("Table3")
        self.Table3.setColumnCount(6)
        self.Table3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Table3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table3.setHorizontalHeaderItem(5, item)
        self.SvvAdd = QtWidgets.QPushButton(self.page_3)
        self.SvvAdd.setGeometry(QtCore.QRect(690, 90, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SvvAdd.setFont(font)
        self.SvvAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SvvAdd.setObjectName("SvvAdd")
        self.SvvRemove = QtWidgets.QPushButton(self.page_3)
        self.SvvRemove.setGeometry(QtCore.QRect(690, 210, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SvvRemove.setFont(font)
        self.SvvRemove.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SvvRemove.setObjectName("SvvRemove")
        self.SvvSave = QtWidgets.QPushButton(self.page_3)
        self.SvvSave.setGeometry(QtCore.QRect(690, 320, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SvvSave.setFont(font)
        self.SvvSave.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SvvSave.setObjectName("SvvSave")
        self.toolBox.addItem(self.page_3, "")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "欢迎使用贝爷食材速查系统"))
        self.label.setText(_translate("MainWindow", "明确生物类型："))
        self.label_2.setText(_translate("MainWindow", " 重量（kg）："))
        self.label_3.setText(_translate("MainWindow", "数量："))
        self.MingQueAdd.setText(_translate("MainWindow", "添加类型"))
        self.label_8.setText(_translate("MainWindow", "结果："))
        self.label_9.setText(_translate("MainWindow", "卡路里总量\n"
"（kg ）："))
        self.label_11.setText(_translate("MainWindow", "建议食用量\n"
"（kg）："))
        self.label_12.setText(_translate("MainWindow", "不闹肚子的量\n"
"（g）："))
        self.label_13.setText(_translate("MainWindow", "可能引发的收视率\n"
"（m）："))
        self.label_14.setText(_translate("MainWindow", "贝爷的野外直播和教程\n"
"详细的食谱等见附录!!"))
        self.label_7.setText(_translate("MainWindow", "头长\n"
"（去掉才可以吃）："))
        self.label_5.setText(_translate("MainWindow", "生物直径："))
        self.label_6.setText(_translate("MainWindow", "身体长："))
        self.BMingQueAdd.setText(_translate("MainWindow", "添加类型"))
        self.label_4.setText(_translate("MainWindow", "不明确生物类型："))
        self.Calculate.setText(_translate("MainWindow", "计算"))
        self.label_19.setText(_translate("MainWindow", "数量："))
        self.MingQueClear.setText(_translate("MainWindow", "清除"))
        self.BMingQueClear.setText(_translate("MainWindow", "清除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "计算"))
        item = self.Table1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "动物名"))
        item = self.Table1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "热量"))
        self.ThermoRemove.setText(_translate("MainWindow", "删除"))
        self.ThermoAdd.setText(_translate("MainWindow", "新增"))
        self.ThermoSave.setText(_translate("MainWindow", "保存"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "热量换算"))
        item = self.Table2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "动物名"))
        item = self.Table2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "身体部位"))
        item = self.Table2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "美味程度"))
        item = self.Table2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "蕴含卡路里"))
        item = self.Table2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "食用上限"))
        item = self.Table2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "备注"))
        self.AnimalRemove.setText(_translate("MainWindow", "删除"))
        self.AnimalAdd.setText(_translate("MainWindow", "新增"))
        self.AnimalSave.setText(_translate("MainWindow", "保存"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "常见动物属性"))
        item = self.Table3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "地方"))
        item = self.Table3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "环境类型"))
        item = self.Table3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "危险程度"))
        item = self.Table3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "存活几率"))
        item = self.Table3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "携带装备"))
        item = self.Table3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "备注"))
        self.SvvAdd.setText(_translate("MainWindow", "新增"))
        self.SvvRemove.setText(_translate("MainWindow", "删除"))
        self.SvvSave.setText(_translate("MainWindow", "保存"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "荒野求生记录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "附录"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
