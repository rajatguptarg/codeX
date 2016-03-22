from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class About(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        Icon = QtGui.QLabel("CodeX", self)
        Icon.setPixmap(QtGui.QPixmap("icons/icon.png"))

        Title = QtGui.QLabel("    CodeX", self)
        Title.setFont(QtGui.QFont("Arial", 18))

        Content = QtGui.QLabel("      Beta Version\nGNU GPL License v(3.0)", self)
        Content.setFont(QtGui.QFont("Helvetica", 12))

        Contact = QtGui.QLabel("PyLab www.0xpylab.blogspot.com")

        layout = QtGui.QGridLayout()
        layout.addWidget(Icon, 1,0)
        layout.addWidget(Title, 1, 1)
        layout.addWidget(Content, 3,1)
        layout.addWidget(Contact, 4,1)

        self.setGeometry(300,300, 3,3)
        self.setWindowTitle("About CodeX")
        self.setLayout(layout)
