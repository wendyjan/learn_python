""""
demo_3.py

wendyjan on Github

Description:
  --> Reuse the "RandomNumberWidget" class from "demo_2.py".
  --> Plot the random numbers that are generated from multiple instances of the widget.
  --> Update the plot each time a new random number is generated.
"""
# Standard Library Imports.
import random
import sys
# Third-party imports.
from PyQt4 import QtGui
import pyqtgraph as pg
# Local imports.
from demo_2 import RandomNumberWidget


class RandomPlotter(QtGui.QWidget):

    def __init__(self, r_min=0, r_max=100):
        super(RandomPlotter, self).__init__()

        # First put in 5 RandomNumberWidgets to generate data.
        vert_layout = QtGui.QVBoxLayout()
        self.widget_list = []
        for i in range(100, 600, 100):
            temp_widget = RandomNumberWidget(i, i + 100)
            self.widget_list.append(temp_widget)
            vert_layout.addWidget(temp_widget)
            # Hook up the buttons of the RandomNumberWidgets to update a plot.
            temp_widget.inc_button.clicked.connect(self.update)

        # Next, put in that plot to show their data.
        window = pg.GraphicsWindow(title="demo-3.py")
        rand_plot = window.addPlot(title="Random Numbers")
        self.curve = rand_plot.plot()
        # Set the range of the y-axis explicitly, in order to disable autosizing axis.
        # This keeps the y-axis steady even when random numbers at extremes of list vary.
        # Makes for a more readable widget as the numbers change.
        self.curve.getViewBox().setYRange(0, 600)
        data = [x.random_int for x in self.widget_list]
        self.curve.setData(data)

        main_layout = QtGui.QHBoxLayout()
        main_layout.addLayout(vert_layout)
        main_layout.addWidget(window)
        self.setLayout(main_layout)
        self.setWindowTitle("demo-3.py")
        self.show()

    def handle_checkbox(self):
        self.result_label.setVisible(not self.result_label.isVisible())

    def handle_button(self):
        self.random_int = random.randint(self.min, self.max)
        self.result_label.setText(str(self.random_int))

    def update(self):
        self.curve.setData([x.random_int for x in self.widget_list])


if __name__ == "__main__":

    background_app = QtGui.QApplication([])
    g = RandomPlotter()
    sys.exit(background_app.exec_())
