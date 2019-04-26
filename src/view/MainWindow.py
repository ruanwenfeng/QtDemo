from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from ..ui.Ui_main_window import Ui_MainWindow


class FirstMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(FirstMainWindow, self).__init__(parent)

        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        # 设置标题
        self.setWindowTitle("First Window Title")

        self.center()

        self.status = self.statusBar()
        self.status.showMessage("5只存在5秒", 5000)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
