""""
demo_1.py

wendyjan on Github

Description:
  --> This file shows 3 basic PyQt widgets interacting with each other:
        --> QPushButton
        --> QCheckBox
        --> QLabel
  --> Writing inline (all in one file and defining lambda functions as we go) works for a quick demo.
  --> In demo_2.py we'll make this same functionality reusable, in case we need it for a real project.

"""
# Standard Library Imports.
import random
import sys
# Third-party imports.
from PyQt4 import QtGui


if __name__ == "__main__":

    background_app = QtGui.QApplication([])
    my_gui = QtGui.QWidget()

    result_label = QtGui.QLabel(str(random.randint(0, 100)))
    inc_button = QtGui.QPushButton("Update Random Number")
    inc_button.clicked.connect(lambda: result_label.setText(str(random.randint(0, 100))))
    result_checkbox = QtGui.QCheckBox("Show Random Number")
    result_checkbox.setChecked(True)
    result_checkbox.stateChanged.connect(lambda: result_label.setVisible(not result_label.isVisible()))
    layout = QtGui.QVBoxLayout()
    layout.addWidget(inc_button)
    layout.addWidget(result_checkbox)
    layout.addWidget(result_label)

    my_gui.setLayout(layout)
    my_gui.setWindowTitle("demo-1.py")
    my_gui.show()
    sys.exit(background_app.exec_())
