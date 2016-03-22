from PyQt4 import QtGui, QtCore

class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.darkBlue)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)

        keywordPatterns = ["\\bauto\\b", "\\bbreak\\b", "\\bcase\\b",
                "\\bchar\\b", "\\bconst\\b", "\\bcontinue\\b", "\\bdefault\\b",
                "\\bdo\\b", "\\bdouble\\b", "\\belse\\b", "\\benum\\b",
                "\\bextern\\b", "\\bfloat\\b", "\\bfor\\b",
                "\\bgoto\\b", "\\bif\\b", "\\bint\\b", "\\blong\\b",
                "\\bregister\\b", "\\breturn\\b", "\\bshort\\b",
                "\\bsigned\\b", "\\bsizeof\\b", "\\bstatic\\b",
                "\\bstruct\\b", "\\bswitch\\b", "\\btypedef\\b", "\\bunion\\b",
                "\\bunsigned\\b", "\\bvoid\\b", "\\bvolatile\\b", "\\bwhile\\b"]

        self.highlightingRules = [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        signFormat = QtGui.QTextCharFormat()
        signFormat.setFontWeight(QtGui.QFont.Bold)
        signFormat.setForeground(QtCore.Qt.darkMagenta)
        self.highlightingRules.append((QtCore.QRegExp("[+-*/%]"),
                signFormat))

        # include highlight (#)
        includeFormat = QtGui.QTextCharFormat()
        includeFormat.setFontWeight(QtGui.QFont.Bold)
        includeFormat.setForeground(QtCore.Qt.darkMagenta)
        self.highlightingRules.append((QtCore.QRegExp("#include"),
                includeFormat))

        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setForeground(QtCore.Qt.black)
        self.highlightingRules.append((QtCore.QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QtGui.QTextCharFormat()
        self.multiLineCommentFormat.setForeground(QtCore.Qt.black)

        quotationFormat = QtGui.QTextCharFormat()
        quotationFormat.setForeground(QtCore.Qt.red)
        self.highlightingRules.append((QtCore.QRegExp("\".*\""),
                quotationFormat))

        functionFormat = QtGui.QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression = QtCore.QRegExp("/\\*")
        self.commentEndExpression = QtCore.QRegExp("\\*/")

        # Single Quotation
        single_quotationFormat = QtGui.QTextCharFormat()
        single_quotationFormat.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((QtCore.QRegExp("'.*'"),
                single_quotationFormat))

        # Double Quotation
        double_quotationFormat = QtGui.QTextCharFormat()
        double_quotationFormat.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((QtCore.QRegExp("\".*\""),
                double_quotationFormat))

        # Function highlighting ()
        functionFormat = QtGui.QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
