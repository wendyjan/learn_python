"""
Filename: sample_userInterface.py

Author: Wendy Jansson

This file shows a sample user interface.
My comments are below each line they apply to.

There is a lot of stuff that we didn't discuss in class here,
so feel free to ask me :) wendyjan@buffalo.edu

NOTE you must have PyQt4 installed for this code to work! Use the Anaconda distribution of Python. 

Check out more user interface tutorials at http://zetcode.com/gui/pyqt4
"""
import sys # This is a standard library that comes with Python.
from PyQt4 import QtGui # PyQt4 is a third-party library that comes separately (packed into Anaconda). 

class Example(QtGui.QWidget): 
    # When you define a class with something inside parentheses after it,
    # in this case "Example(QtGui.QWidget)",
    # it means that your class "Example" will inherit all the behavior of another pre-written class,
    # in this case the QWidget class that is part of PyQt4's QtGui set of code. 
    
    def __init__(self):
        super(Example, self).__init__() 
        # When a class inherits behavior (from QtGui.QWidget in this case),
        # the first line should be "super(myClassName, self).__init__()", 
        # where you substitute the name of your class for myClassName.
    
        updateButton = QtGui.QPushButton('Update my text')
        updateButton.clicked.connect(self.userPressedButton)
        # Make a button, and connect it to the method "userPressedButton".
        
        self.userTextField = QtGui.QTextEdit("")
        self.userTextLabel = QtGui.QLabel()
        # Make a text field to take user input,
        # and a label to display text.
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(updateButton)
        layout.addWidget(self.userTextField)
        layout.addWidget(self.userTextLabel)
        self.setLayout(layout)
        # Make and set the layout to hold each widget (button, text field, and label).
        # Don't worry too much about layouts, they are a topic unto themselves!
        # Google "zetcode PyQt4 layout tutorial" if you are very very curious.
        
        self.setGeometry(300, 300, 400, 600)
        # Put the window at 300, 300 onscreen.
        # And make it 400 x 600 in size.
        self.setWindowTitle('My First User Interface')
        
        self.show()
        
    def userPressedButton(self, pressEvent):
        # This method describes what happens when the user presses our button.
        self.userTextLabel.setText(self.userTextField.toPlainText())
        print ("hi")
        
if __name__ == '__main__':
    app = QtGui.QApplication([]) # Don't worry too much about what this line means, just type it!
    ex = Example() # This line makes an object out of our "Example" class above. 
    sys.exit(app.exec_()) # Don't worry too much about what this line means, just type it!  
