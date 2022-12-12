# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(291, 215)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.simulationParams = QGroupBox(self.centralwidget)
        self.simulationParams.setObjectName(u"simulationParams")
        font = QFont()
        font.setPointSize(12)
        self.simulationParams.setFont(font)
        self.formLayout = QFormLayout(self.simulationParams)
        self.formLayout.setSpacing(6)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setObjectName(u"formLayout")
        self.paramXEntry = QDoubleSpinBox(self.simulationParams)
        self.paramXEntry.setObjectName(u"paramXEntry")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.paramXEntry)

        self.paramYEntry = QDoubleSpinBox(self.simulationParams)
        self.paramYEntry.setObjectName(u"paramYEntry")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.paramYEntry)

        self.label_2 = QLabel(self.simulationParams)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.paramXLabel = QLabel(self.simulationParams)
        self.paramXLabel.setObjectName(u"paramXLabel")
        self.paramXLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.paramXLabel)

        self.paramXEntry.raise_()
        self.paramYEntry.raise_()
        self.label_2.raise_()
        self.paramXLabel.raise_()

        self.verticalLayout.addWidget(self.simulationParams)

        self.runButton = QPushButton(self.centralwidget)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setFont(font)

        self.verticalLayout.addWidget(self.runButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 291, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.runButton.clicked.connect(MainWindow.runSimultation)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.simulationParams.setTitle(QCoreApplication.translate("MainWindow", u"Simulator", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X : ", None))
        self.paramXLabel.setText(QCoreApplication.translate("MainWindow", u"Y : ", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
    # retranslateUi

