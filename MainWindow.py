# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setEnabled(True)
        Main.resize(358, 315)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 190, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 220, 131, 16))
        self.label_8.setObjectName("label_8")
        self.load = QtWidgets.QComboBox(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(230, 40, 101, 22))
        self.load.setObjectName("load")
        self.load.addItem("")
        self.load.addItem("")
        self.load.addItem("")
        self.unload = QtWidgets.QComboBox(self.centralwidget)
        self.unload.setGeometry(QtCore.QRect(230, 70, 101, 22))
        self.unload.setObjectName("unload")
        self.unload.addItem("")
        self.unload.addItem("")
        self.unload.addItem("")
        self.value = QtWidgets.QComboBox(self.centralwidget)
        self.value.setGeometry(QtCore.QRect(230, 100, 101, 22))
        self.value.setObjectName("value")
        self.value.addItem("")
        self.value.addItem("")
        self.value.addItem("")
        self.value.addItem("")
        self.time = QtWidgets.QSpinBox(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(230, 130, 101, 22))
        self.time.setObjectName("time")
        self.time.setMinimum(3)
        self.time.setMaximum(31)
        self.cost = QtWidgets.QComboBox(self.centralwidget)
        self.cost.setGeometry(QtCore.QRect(230, 220, 101, 22))
        self.cost.setObjectName("cost")
        self.cost.addItem("")
        self.cost.addItem("")
        self.cost.addItem("")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(230, 10, 101, 21))
        self.Name.setObjectName("Name")
        self.value_2 = QtWidgets.QComboBox(self.centralwidget)
        self.value_2.setGeometry(QtCore.QRect(230, 160, 101, 22))
        self.value_2.setObjectName("value_2")
        self.value_2.addItem("")
        self.value_2.addItem("")
        self.value_2.addItem("")
        self.value_3 = QtWidgets.QComboBox(self.centralwidget)
        self.value_3.setGeometry(QtCore.QRect(230, 190, 101, 22))
        self.value_3.setObjectName("value_3")
        self.value_3.addItem("")
        self.value_3.addItem("")
        self.value_3.addItem("")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(230, 265, 101, 23))
        self.ok.setObjectName("ok")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 358, 20))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Ввод данных"))
        self.label.setText(_translate("Main", "Наименование груза"))
        self.label_2.setText(_translate("Main", "Пункт погрузки"))
        self.label_3.setText(_translate("Main", "Пункт разгрузки"))
        self.label_4.setText(_translate("Main", "Объем поставки"))
        self.label_5.setText(_translate("Main", "Срок выполнения"))
        self.label_6.setText(_translate("Main", "Суммарная длительность"))
        self.label_7.setText(_translate("Main", "Штраф за недопоставку"))
        self.label_8.setText(_translate("Main", "Затраты на выполнение"))
        self.load.setItemText(0, _translate("Main", "1"))
        self.load.setItemText(1, _translate("Main", "2"))
        self.load.setItemText(2, _translate("Main", "3"))
        self.unload.setItemText(0, _translate("Main", "1"))
        self.unload.setItemText(1, _translate("Main", "2"))
        self.unload.setItemText(2, _translate("Main", "3"))
        self.value.setItemText(0, _translate("Main", "4"))
        self.value.setItemText(1, _translate("Main", "6"))
        self.value.setItemText(2, _translate("Main", "8"))
        self.value.setItemText(3, _translate("Main", "10"))
        self.value_2.setItemText(0, _translate("Main", "1"))
        self.value_2.setItemText(1, _translate("Main", "2"))
        self.value_2.setItemText(2, _translate("Main", "3"))
        self.value_3.setItemText(0, _translate("Main", "5"))
        self.value_3.setItemText(1, _translate("Main", "10"))
        self.value_3.setItemText(2, _translate("Main", "15"))
        self.cost.setItemText(0, _translate("Main", "20"))
        self.cost.setItemText(1, _translate("Main", "25"))
        self.cost.setItemText(2, _translate("Main", "30"))
        self.ok.setText(_translate("Main", "Отправить"))