import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer
import pandas as pd
import numpy as np
import time
import random
# from gurobipy import *
from PyQt5.QtWidgets import QPushButton, QMainWindow, QWidget, QApplication, QTableWidgetItem, QMessageBox

import MainWindow  # Это наш конвертированный файл дизайна
import SecondWindow


class SecondWindow(QtWidgets.QMainWindow, SecondWindow.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        val = int(value)
        if val == 4:
            b = random.randint(2850, 3200)
            rand = random.randint(2, 6)
            self.tableWidget_2.setItem(0, 2, QTableWidgetItem(str(rand)))
            rand = random.randint(4, 7)
            self.tableWidget_2.setItem(5, 1, QTableWidgetItem(str(rand)))
            rand = random.randint(3, 7)
            self.tableWidget_2.setItem(8, 1, QTableWidgetItem(str(rand)))
            rand = random.randint(1, 7)
            self.tableWidget_2.setItem(7, 0, QTableWidgetItem(str(rand)))
        elif val == 6:
            b = random.randint(3100, 3400)
            rand = random.randint(2, 7)
            self.tableWidget_2.setItem(2, 0, QTableWidgetItem(str(rand)))
            rand = random.randint(1, 3)
            self.tableWidget_2.setItem(3, 1, QTableWidgetItem(str(rand)))
            rand = random.randint(1, 3)
            self.tableWidget_2.setItem(6, 2, QTableWidgetItem(str(rand)))
            rand = random.randint(3, 5)
            self.tableWidget_2.setItem(0, 1, QTableWidgetItem(str(rand)))
            rand = random.randint(4, 6)
            self.tableWidget_2.setItem(8, 1, QTableWidgetItem(str(rand)))
        elif val == 8:
            b = random.randint(3500, 3850)
            rand = random.randint(2, 7)
            self.tableWidget_2.setItem(3, 2, QTableWidgetItem(str(rand)))
            rand = random.randint(1, 5)
            self.tableWidget_2.setItem(4, 0, QTableWidgetItem(str(rand)))
            rand = random.randint(2, 6)
            self.tableWidget_2.setItem(7, 2, QTableWidgetItem(str(rand)))
        else:
            b = random.randint(4400, 4750)
            rand = random.randint(3, 6)
            self.tableWidget_2.setItem(2, 1, QTableWidgetItem(str(rand)))
            rand = random.randint(1, 5)
            self.tableWidget_2.setItem(4, 0, QTableWidgetItem(str(rand)))
            rand = random.randint(4, 7)
            self.tableWidget_2.setItem(4, 2, QTableWidgetItem(str(rand)))
            rand = random.randint(1, 5)
            self.tableWidget_2.setItem(7, 2, QTableWidgetItem(str(rand)))
        self.textBrowser.setText(str(b))
        a = 0
        for i in range(9):
            for y in range(3):
                if (i == y) or ((i-3) == y) or ((i-6) == y):
                    self.tableWidget_2.setItem(i, y, QTableWidgetItem(str(a)))
        m = int(value)
        for i in [11, 7, 5, m]:
            b = random.randint(1, 100)
            if b % 3 == 1:
                a1 = random.randint(3, i) // 3
                a2 = random.randint(3, i) // 3
                a3 = i - a1 - a2
            if b % 3 == 2:
                a3 = random.randint(3, i) // 3
                a1 = random.randint(3, i) // 3
                a2 = i - a1 - a3
            # a.append(random.randint(1,100))
            if b % 3 == 0:
                a3 = random.randint(3, i) // 3
                a2 = random.randint(3, i) // 3
                a1 = i - a3 - a2
            if i == 11: k = 0
            if i == 7: k = 1
            if i == 5: k = 2
            if i == m:  k = 3
            self.tableWidget.setItem(k, 0, QTableWidgetItem(str(a1)))
            self.tableWidget.setItem(k, 1, QTableWidgetItem(str(a2)))
            self.tableWidget.setItem(k, 2, QTableWidgetItem(str(a3)))
        # for x in range(3):
        #     for y in range(3):
        #         c = random.randint(1, 10)
        #         self.tableWidget.setItem(x, y, QTableWidgetItem(str(random.randint(1, c))))


class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_Main):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.SecondWindow = None
        self.ok.clicked.connect(self.check)
        # If using this code within a script tool, AddError can be used to return messages
        #   back to a script tool. If not, AddError will have no effect.

    def check(self):
        ab = (str(self.load.currentText()))
        cd = (str(self.unload.currentText()))
        global value
        value = (str(self.value.currentText()))
        text = self.Name.text()
        if (ab == cd) or (len(text) < 3):
            QMessageBox.critical(self, "Ошибка ", "Данные некорректны", QMessageBox.Ok)
        else:
            # self.calc()
            time.sleep(10)
            self.close()
            self.SecondWindow = SecondWindow()
            self.SecondWindow.show()

    # def calc(self):
    #     daysList = ['Day1', 'Day2', 'Day3']
    #     ordersList = ['Order1', 'Order2', 'Order3', 'Order4']
    #     fullWagonsPerOrder = \
    #         ['order1day1','order1day2','order1day3','order2day1','order2day2','order2day3','order3day1','order3day2','order3day3','order4day1','order4day2','order4day3']
    #     emptyWagonsPerCity = ['1-1day1','1-2day1','1-3day1','2-1day1', '2-2day1','2-3day1','3-1day1','3-2day1','3-3day1',
    #                           '1-1day2','1-2day2','1-3day2','2-1day2', '2-2day2','2-3day2','3-1day2','3-2day2','3-3day2',
    #                           '1-1day3','1-2day3','1-3day3','2-1day3', '2-2day3','2-3day3','3-1day3','3-2day3','3-3day3']
    #     shiftfullWagonsPerOrder = []
    #     cityList = ['City1', 'City2', 'City3']
    #     Req = [3, 2, 4, 4, 5, 4, 5, 4, 2, 4, 5, 4, 3, 5]
    #     shiftRequirements = {s: shiftReq[i] for i, s in enumerate(shiftList)}
    #     available. = {(w, s): availability.loc[w, s] for w in List for s in shiftList}
    #     mgmtList = ['EE01', 'EE03', 'EE05', 'EE07']
    #     nonmgmtList = [x for x in workerList if x not in mgmtList]
    #     fullCost = [200, 100, 225, 110, 190, 105, 210, 120, 95, 100]
    #
    #     OTCost = [1.5 * x for x in regCost]
    #
    #     fullCost = {w: regCost[i] for i, w in enumerate(workerList)}
    #     emptyCost = {w: OTCost[i] for i, w in enumerate(workerList)}
    #
    #
    #
    #     minShifts = 3
    #     maxShifts = 7
    #
    #     OTTrigger = 5
    #
    #     model = Model("WorkersScheduling")
    #
    #
    #     x = model.addVars(workerList, shiftList, ub=avail, vtype=GRB.BINARY, name='x')
    #
    #     regHours = model.addVars(workerList, name='regHrs')
    #     overtimeHours = model.addVars(workerList, name='overtimeHrs')
    #     overtimeTrigger = model.addVars(workerList, name="OT_Trigger", vtype=GRB.BINARY)
    #
    #     model.ModelSense = GRB.MINIMIZE
    #     Cost = 0
    #     Cost += (quicksum(regularCost[w] * regHours[w] + overtimeCost[w] * overtimeHours[w] for w in workerList))
    #     model.setObjective(Cost)
    #     model.write("Optimized_Scheduling.lp")
    #     file = open("Optimized_Scheduling.lp", 'r')
    #     print(file.read())
    #     file.close()
    #     model.optimize()
    #     self.textBrowser.setText(str('Total cost = $' + str(model.ObjVal)))
    #     sol = pd.DataFrame(data={'Solution': model.X}, index=model.VarName)
    #     sol = sol.iloc[0:len(x)]
    #     dashboard1 = pd.DataFrame(index=workerList, columns=shiftList)
    #     for w in workerList:
    #         for s in shiftList:
    #             dashboard1.at[w, s] = sol.loc['x[' + w + ',' + s + ']',][0]
    #
    #     dashboard1
    #     dashboard2 = pd.DataFrame(index=(len(cityList)*len(dayList)), columns=cityList)
    #     for d in dayList:
    #         for s in shiftList:
    #             dashboard1.at[w, s] = sol.loc['x[' + w + ',' + s + ']',][0]
    #
    #     dashboard2


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
