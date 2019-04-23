import sys
import PyQt5
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class SigSlot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('XXOO')
        lcd = QtWidgets.QLCDNumber(self)
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        slider.setRange(0, 1000)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)

        slider.valueChanged.connect(lcd.display)
        self.resize(350, 250)


app = QtWidgets.QApplication(sys.argv)
qb = SigSlot()
qb.show()
sys.exit(app.exec_())
