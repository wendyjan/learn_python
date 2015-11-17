""""
demo_2.py

wendyjan on Github

Description:
  --> The "RandomNumberWidget" class shows how to make a custom reusable QWidget. The widget contains:
        --> QPushButton to get a new random number
        --> QCheckBox to toggle the display of the random number
        --> QLabel to show the random number
  --> The driver code (bottom of file) shows how to make multiple copies of RandomNumberWidget and show them all.

"""
# Standard Library Imports.
import random
import sys
# Third-party imports.
from PyQt4 import QtGui

class RandomNumberWidget(QtGui.QWidget):

    def __init__(self, r_min=0, r_max=100):
        super(RandomNumberWidget, self).__init__()
        self.min = r_min
        self.max = r_max
        self.random_int = random.randint(self.min, self.max)
        self.result_label = QtGui.QLabel(str(self.random_int))
        self.inc_button = QtGui.QPushButton("Update Random Number")
        self.inc_button.clicked.connect(self.handle_button)
        self.result_checkbox = QtGui.QCheckBox("Display Random Number below:")
        self.result_checkbox.setChecked(True)
        self.result_checkbox.stateChanged.connect(self.handle_checkbox)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.inc_button)
        layout.addWidget(self.result_checkbox)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def handle_checkbox(self):
        self.result_label.setVisible(not self.result_label.isVisible())

    def handle_button(self):
        self.random_int = random.randint(self.min, self.max)
        self.result_label.setText(str(self.random_int))


if __name__ == "__main__":

    background_app = QtGui.QApplication([])
    my_gui = QtGui.QWidget()

    main_layout = QtGui.QVBoxLayout()

    for i in range(100, 600, 100):
        tempWidget = RandomNumberWidget(i, i + 100)
        main_layout.addWidget(tempWidget)
    my_gui.setLayout(main_layout)

    my_gui.setWindowTitle("demo-2.py")
    my_gui.show()
    sys.exit(background_app.exec_())
