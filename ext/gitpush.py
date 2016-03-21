from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
import os
import re

class Gitpush(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        Title = QtGui.QLabel("GitPush", self)
        Title.setFont(QtGui.QFont("Arial", 18))

        # Enter git url to clone
        self.cloneRepo_label1 = QtGui.QLabel("Enter Git Repo: ")
        self.cloneRepo_label2 = QtGui.QLabel("Please use SSH")

        self.cloneRepo_input = QtGui.QLineEdit(self)
        self.cloneRepo_input.setBaseSize(10,10)

        self.cloneRepo_button = QtGui.QPushButton()
        self.cloneRepo_button.setText("Clone it!")
        self.cloneRepo_button.clicked.connect(self.cloneRepo)

        # Upload to Github
        self.pushRepo_label1 = QtGui.QLabel("Push files to GitHub")
        self.pushRepo_label2 = QtGui.QLabel("Git commit :")

        self.pushRepo_input = QtGui.QLineEdit(self)

        self.pushRepo_button = QtGui.QPushButton()
        self.pushRepo_button.setText("Push")
        self.pushRepo_button.clicked.connect(self.pushRepo)

        # Show output, info of what's happening
        self.board = QtGui.QTextEdit(self)
        self.board.resize(400, 100)
        # This is for showing feedback, therefore
        # we have to make it read only and unable to edit the widget
        self.board.isReadOnly()

        # Main Layout
        layout = QtGui.QGridLayout()

        # Adding Widgets
        layout.addWidget(Title, 0,0)

        layout.addWidget(self.cloneRepo_label1, 1,0)
        layout.addWidget(self.cloneRepo_label2, 2,0)
        layout.addWidget(self.cloneRepo_input, 1,1)
        layout.addWidget(self.cloneRepo_button, 2,1)

        # Empty space
        layout.addWidget(QtGui.QLabel(""), 3,0)

        layout.addWidget(self.pushRepo_label1, 4,0)
        layout.addWidget(self.pushRepo_label2, 5,0)
        layout.addWidget(self.pushRepo_input, 5,1)
        layout.addWidget(self.pushRepo_button, 6,1)

        # Empty space
        layout.addWidget(QtGui.QLabel(""), 7,0)

        layout.addWidget(QtGui.QLabel("Showing Output"), 8,0)
        layout.addWidget(self.board, 8,1)

        self.setLayout(layout)
        self.setGeometry(300,300, 400,350)
        self.setWindowTitle("Push to Github Repo")

    # Real functions that are used to clone repository
    # and push files to repository
    def cloneRepo(self):
        gitUrl = self.cloneRepo_input.text()
        # saving repo name
        self.repoName = re.findall(r'/(.*).git', gitUrl)[0]

        # Using os.system to call command (git)
        os.system("git clone %s" % gitUrl)
        self.board.setText("Cloned in %s" % os.getcwd())

    def pushRepo(self):
        commitMsg = self.pushRepo_input.text()
        os.system('mv *.py %s && cd %s && git add * && git commit -m "%s" && git push -u origin master' \
                    % (self.repoName, self.repoName, commitMsg))
        # showing feedback
        self.board.append("Pushed files to '%s'" % self.repoName)
