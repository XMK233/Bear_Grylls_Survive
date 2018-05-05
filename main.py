# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from math import pi
import os
import csv

from Ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.initializeTable1()
        self.initializeTable2()
        self.initializeTable3()

        self.MingQueRecord.itemClicked.connect(self.removeMingQue)
        self.BMingQueRecord.itemClicked.connect(self.removeBMingQue)

#---------------初始化附录表---------------------
    def initializeTable1(self):
        if os.path.exists("Table1.csv"):
            f = open("Table1.csv", "r", encoding="utf-8")
            lines = csv.reader(f)
            n = 0
            for line in lines:
                self.Table1.insertRow(n)
                self.Table1.setItem(n, 0, QTableWidgetItem(line[0]))
                self.Table1.setItem(n, 1, QTableWidgetItem(line[1]))
                n += 1
        else:
            pass

    def initializeTable2(self):
        if os.path.exists("Table2.csv"):
            f = open("Table2.csv", "r", encoding="utf-8")
            lines = csv.reader(f)
            n = 0
            for line in lines:
                self.Table2.insertRow(n)
                self.Table2.setItem(n, 0, QTableWidgetItem(line[0]))
                self.Table2.setItem(n, 1, QTableWidgetItem(line[1]))
                self.Table2.setItem(n, 2, QTableWidgetItem(line[2]))
                self.Table2.setItem(n, 3, QTableWidgetItem(line[3]))
                self.Table2.setItem(n, 4, QTableWidgetItem(line[4]))
                self.Table2.setItem(n, 5, QTableWidgetItem(line[5]))
                n += 1
        else:
            pass
    def initializeTable3(self):
        if os.path.exists("Table3.csv"):
            f = open("Table3.csv", "r", encoding="utf-8")
            lines = csv.reader(f)
            n = 0
            for line in lines:
                self.Table3.insertRow(n)
                self.Table3.setItem(n, 0, QTableWidgetItem(line[0]))
                self.Table3.setItem(n, 1, QTableWidgetItem(line[1]))
                self.Table3.setItem(n, 2, QTableWidgetItem(line[2]))
                self.Table3.setItem(n, 3, QTableWidgetItem(line[3]))
                self.Table3.setItem(n, 4, QTableWidgetItem(line[4]))
                self.Table3.setItem(n, 5, QTableWidgetItem(line[5]))
        else:
            pass

#-------------------计算--------------------------
    @pyqtSlot()
    def on_MingQueAdd_clicked(self):
        tnt = float(self.MingQueTNT.text())
        qty = float(self.MingQueQuantity.text())

        self.MingQueRecord.addItem("%.2f,%d" % (tnt, qty))

        self.MingQueTNT.clear()
        self.MingQueQuantity.clear()

        return

    @pyqtSlot()
    def on_BMingQueAdd_clicked(self):

        d = float(self.BMingQueDiameter.text())
        l = float(self.BMingQueLength.text())
        lr = float(self.BMingQueHeadLength.text())
        n = float(self.BMingQueQuantity.text())

        self.BMingQueRecord.addItem("%.2f,%.2f,%.2f,%d" % (d, l, lr, n))

        self.BMingQueDiameter.clear()
        self.BMingQueLength.clear()
        self.BMingQueHeadLength.clear()
        self.BMingQueQuantity.clear()

        return

    @pyqtSlot()
    def on_Calculate_clicked(self):
        totalMass = 0.0
        for i in range(self.MingQueRecord.count()):
            line = [float(i) for i in self.MingQueRecord.item(i).text().split(",")]
            totalMass += line[0] * line[1]

        for i in range(self.BMingQueRecord.count()):
            k = [float(i) for i in self.BMingQueRecord.item(i).text().split(",")]
            totalMass += pi + (k[0] * 2) - k[1] + k[2] ** 2 + 3.5 * 8 * 3 / 1000 + k[3]

        resultTotal = round(totalMass)
        self.ResultTotal.setText(str(resultTotal))

        resultAdvice = 0.0
        if resultTotal <= 2:
            resultAdvice = 0.2
        elif resultTotal > 2 and resultTotal <= 4:
            resultAdvice = 0.29
        elif resultTotal > 4 and resultTotal <= 10:
            resultAdvice = 1.0
        else:
            resultAdvice = 8.0
        self.ResultTNT.setText(str(resultAdvice))

        resultBarrier = round(6 + 8.3 * resultTotal)
        self.ResultBarrier.setText(str(resultBarrier))

        resultAlert = 0
        if resultTotal <= 1:
            resultAlert = 9
        elif resultTotal > 1 and resultTotal <= 15:
            resultAlert = 58
        elif resultTotal > 15 and resultTotal <= 26:
            resultAlert = 230
        else:
            resultAlert = 2500
        self.ResultAlert.setText(str(resultAlert))

        return

    @pyqtSlot()
    def on_MingQueClear_clicked(self):
        self.MingQueRecord.clear()
        return

    @pyqtSlot()
    def on_BMingQueClear_clicked(self):
        self.BMingQueRecord.clear()
        return

    def removeMingQue(self):
        self.MingQueRecord.takeItem(self.MingQueRecord.currentRow())##删除一行
        return

    def removeBMingQue(self):
        self.BMingQueRecord.takeItem(self.BMingQueRecord.currentRow())##删除一行
        return

#-------------附录-------------------------
    @pyqtSlot()
    def on_ThermoAdd_clicked(self):
        n = self.Table1.rowCount()
        self.Table1.insertRow(n)
        self.Table1.setItem(n, 0, QTableWidgetItem("--请修改--"))
        self.Table1.setItem(n, 1, QTableWidgetItem("--请修改--"))
        return

    @pyqtSlot()
    def on_ThermoRemove_clicked(self):
        self.Table1.removeRow(self.Table1.currentRow())
        return

    @pyqtSlot()
    def on_ThermoSave_clicked(self):
        f = open("Table1.csv", "w", encoding="utf-8")
        for i in range(self.Table1.rowCount()):
            tmp = []
            for j in range(2):
                tmp.append(self.Table1.item(i, j).text())
            f.write(",".join(tmp) + "\n")

        f.close()
        return

    @pyqtSlot()
    def on_AnimalAdd_clicked(self):
        n = self.Table2.rowCount()
        self.Table2.insertRow(n)
        self.Table2.setItem(n, 0, QTableWidgetItem("--请修改--"))
        self.Table2.setItem(n, 1, QTableWidgetItem("--请修改--"))
        self.Table2.setItem(n, 2, QTableWidgetItem("--请修改--"))
        self.Table2.setItem(n, 3, QTableWidgetItem("--请修改--"))
        self.Table2.setItem(n, 4, QTableWidgetItem("--请修改--"))
        self.Table2.setItem(n, 5, QTableWidgetItem("--请修改--"))
        return

    @pyqtSlot()
    def on_AnimalRemove_clicked(self):
        self.Table2.removeRow(self.Table2.currentRow())
        return

    @pyqtSlot()
    def on_AnimalSave_clicked(self):
        f = open("Table2.csv", "w", encoding="utf-8")
        for i in range(self.Table2.rowCount()):
            tmp = []
            for j in range(6):
                tmp.append(self.Table2.item(i, j).text())
            f.write(",".join(tmp) + "\n")

        f.close()
        return

    @pyqtSlot()
    def on_SvvAdd_clicked(self):
        n = self.Table3.rowCount()
        self.Table3.insertRow(n)
        self.Table3.setItem(n, 0, QTableWidgetItem("--请修改--"))
        self.Table3.setItem(n, 1, QTableWidgetItem("--请修改--"))
        self.Table3.setItem(n, 2, QTableWidgetItem("--请修改--"))
        self.Table3.setItem(n, 3, QTableWidgetItem("--请修改--"))
        self.Table3.setItem(n, 4, QTableWidgetItem("--请修改--"))
        self.Table3.setItem(n, 5, QTableWidgetItem("--请修改--"))
        return

    @pyqtSlot()
    def on_SvvRemove_clicked(self):
        self.Table3.removeRow(self.Table3.currentRow())
        return

    @pyqtSlot()
    def on_SvvSave_clicked(self):
        f = open("Table3.csv", "w", encoding="utf-8")
        for i in range(self.Table3.rowCount()):
            tmp = []
            for j in range(6):
                tmp.append(self.Table3.item(i, j).text())
            f.write(",".join(tmp) + "\n")

        f.close()
        return


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
