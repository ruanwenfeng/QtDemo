""" Qt Demo """
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.Ui_main_window import Ui_MainWindow

if __name__ == '__main__':

    # 创建Application实例
    APP = QApplication(sys.argv)

    # 创建一个窗口
    MainWindow = QMainWindow()
    MainUi = Ui_MainWindow()
    MainUi.setupUi(MainWindow)

    MainWindow.move(300, 300)
    MainWindow.setWindowTitle("第一个PyQt程序")

    # 显示窗口
    MainWindow.show()
    sys.exit(APP.exec())
