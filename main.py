import sys
import re
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from ext import find, about, gitpush
from syntax import syntaxPack, syntaxPython

def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


class Main(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.filename = ""

        self.syntaxBox = QtGui.QComboBox(self)

        self.initUI()

    # Functions below are used to show user interface on program

    def initMenubar(self):
        menubar = self.menuBar()

        File = menubar.addMenu("File")
        Edit = menubar.addMenu("Edit")
        View = menubar.addMenu("View")
        About = menubar.addMenu("About")

        File.addAction(self.newAction)
        File.addAction(self.openAction)
        File.addAction(self.saveAction)
        File.addAction(self.gitpush)
        File.addAction(self.printAction)

        Edit.addAction(self.findAction)
        Edit.addAction(self.redoAction)
        Edit.addAction(self.undoAction)

        View.addAction(self.previewAction)
        View.addAction(self.statusbarAction)

        About.addAction(self.about)

    def initToolbar(self):

        # File Management Functions
        # (newAction, openAction, saveAction)
        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.New)

        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.Open)

        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.Save)

        # Printing Function (printAction, previewAction)
        self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"), "Print document", self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.Print)

        self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"), "Page view", self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.Preview)

        # Copy/Paste , Undo/Redo functions
        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"), "Cut to clipboard", self)
        self.cutAction.setStatusTip("Delete and copy text to clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"), "Copy to clipboard", self)
        self.copyAction.setStatusTip("Copy text to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"), "Paste from clipboard", self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"), "Undo last action", self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"), "Redo last undone thing", self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        self.findAction = QtGui.QAction(QtGui.QIcon("icons/find.png"),"Find and replace",self)
        self.findAction.setStatusTip("Find and replace words in your document")
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.triggered.connect(find.Find(self).show)

        self.about = QtGui.QAction(QtGui.QIcon("icons/about.png"), "About us", self)
        self.about.setStatusTip("About CodeX")
        self.about.triggered.connect(about.About(self).show)

        self.gitpush = QtGui.QAction(QtGui.QIcon("icons/git.ico"), "Upload to Github", self)
        self.gitpush.setStatusTip("Upload to GitHub")
        self.gitpush.setShortcut("Ctrl+G")
        self.gitpush.triggered.connect(gitpush.Gitpush(self).show)

        self.statusbarAction = QtGui.QAction("Toggle Status Bar", self)
        self.statusbarAction.triggered.connect(self.toggleStatusbar)


        # Adding to toolbar
        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)
        self.toolbar.addAction(self.findAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.gitpush)

        self.toolbar.addSeparator()

        self.toolbar.addWidget(self.syntaxBox)

    def initUI(self):
        font = QtGui.QFont()
        font.setFixedPitch(True)
        font.setPointSize(12)
        self.text = QtGui.QTextEdit(self)
        self.text.setFont(font)

        # Adding drop-down menu bar to choose syntax
        for language in syntaxPack.List:
            self.syntaxBox.addItem(language)
        self.syntaxBox.activated[str].connect(self.syntaxActivated)

        #self.highlighter = syntaxPython.Highlighter(self.text.document())

        self.setCentralWidget(self.text)
        self.initToolbar()
        self.initMenubar()

        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # x and y coordinates on the screen, width, height
        self.setGeometry(100,100,800,450)
        self.setWindowTitle("CodeX (beta version)")
        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))


    # Functions below are behind the sence
    # You cannot see them on UI but they are the real functions for
    # opening, saving and creating new files
    def New(self):
        spawn = Main(self)
        spawn.show()

    def Open(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*)")
        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())

    def Save(self):
        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
        with open(self.filename,"wt") as file:
            lines = str(self.text.toHtml())

            # Removing unnecessary HTML tags
            lines = re.sub(r'<!DOCTYPE (.*)>', "", lines)
            lines = re.sub(r'<html>(.*)type="text/css">', "", lines)
            lines = re.sub(r'p, li(.*)}', "", lines)
            lines = re.sub(r'</style>(.*)">', "", lines)
            lines = re.sub(r'<p (.*)">', "", lines)

            # Removing end tags
            lines = re.sub(r'</p>', "", lines)
            lines = re.sub(r'<br />', "", lines)
            lines = re.sub(r'</body>', "", lines)
            lines = re.sub(r'</html>', "", lines)

            # Replacing &quot; with "
            lines = re.sub(r'&quot;', '"', lines)

            file.write(lines)

    def Print(self):
        #  Open printing dialog
        dialog = QtGui.QPrintDialog()

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def Preview(self):
        # Open preview dialog
        preview = QtGui.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))
        preview.exec_()

    def toggleStatusbar(self):
        # Toggle Status bar to Hide/Show
        state = self.statusbar.isVisible()
        self.statusbar.setVisible(not state)

    def syntaxActivated(self, lang):
        if lang == 'Python':
            self.highlighter = syntaxPython.Highlighter(self.text.document())

if __name__ == "__main__":
    main()