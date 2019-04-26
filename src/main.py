""" Qt Demo """
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication

from src.view.MainWindow import FirstMainWindow

if __name__ == '__main__':

    # 创建Application实例
    APP = QApplication(sys.argv)

    # 创建一个窗口
    MainWindow = FirstMainWindow()

    # 显示窗口
    MainWindow.show()
    sys.exit(APP.exec())
