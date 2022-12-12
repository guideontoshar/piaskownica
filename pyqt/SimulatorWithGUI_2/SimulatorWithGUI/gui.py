import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.Qt3DExtras import Qt3DExtras
from PySide2.Qt3DCore import Qt3DCore
from PySide2.QtGui import QVector3D, QColor
from PySide2.Qt3DRender import Qt3DRender
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import QObject, Signal, Slot

class MainWindow(QMainWindow):
    def __init__(self, simulator):
        super(MainWindow, self).__init__()
        self.simulator = simulator
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def run(self):
        print('Running simulation')

    def runSimultation(self):
        self.run() 
        x = self.ui.paramXEntry.value()
        y = self.ui.paramYEntry.value()
        print(f"Simulation parameters x: {x} y: {y}")

def run_application(simulator):
    app = QApplication(sys.argv)
    window = MainWindow(simulator)
    window.show()
    sys.exit(app.exec_())
