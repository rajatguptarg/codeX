from PyQt4 import QtGui, QtCore

class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.darkBlue)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)

        keywordPatterns = ["\\band\\b", "\\bdel\\b", "\\bfrom\\b",
                "\\bnot\\b", "\\bwhile\\b", "\\bas\\b", "\\belif\\b",
                "\\bglobal\\b", "\\bor\\b", "\\bwith\\b", "\\bassert\\b",
                "\\belse\\b", "\\bif\\b", "\\bpass\\b",
                "\\byield\\b", "\\bbreak\\b", "\\bexcept\\b", "\\bimport\\b",
                "\\bprint\\b", "\\bclass\\b", "\\bexec\\b",
                "\\bin\\b", "\\braise\\b", "\\bcontinue\\b",
                "\\bfinally\\b", "\\bis\\b", "\\breturn\\b", "\\bdef\\b",
                "\\bfor\\b", "\\blambda\\b", "\\btry\\b", "\\bbreak\\b"]

        self.highlightingRules = [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        # Single Line Comment #
        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setFontItalic(True)
        singleLineCommentFormat.setForeground(QtCore.Qt.black)
        self.highlightingRules.append((QtCore.QRegExp("#[^\n]*"),
                singleLineCommentFormat))

        # Decorator @
        decoratorFormat = QtGui.QTextCharFormat()
        decoratorFormat.setFontItalic(True)
        decoratorFormat.setForeground(QtCore.Qt.black)
        self.highlightingRules.append((QtCore.QRegExp("@[^\n]*"),
                decoratorFormat))

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

        # Triple Quotation
        # (Using three single quotes)
        triple_quotationFormat_single = QtGui.QTextCharFormat()
        triple_quotationFormat_single.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((QtCore.QRegExp("'''.*'''"),
                triple_quotationFormat_single))

        # (Using three double quotes)
        triple_quotationFormat_double = QtGui.QTextCharFormat()
        triple_quotationFormat_double.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((QtCore.QRegExp("\"\"\".*\"\"\""),
                triple_quotationFormat_double))

        # Function highlighting (def)
        functionFormat = QtGui.QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        # Class highlighting (class)
        classFormat = QtGui.QTextCharFormat()
        classFormat.setFontWeight(QtGui.QFont.Bold)
        classFormat.setForeground(QtCore.Qt.darkMagenta)
        self.highlightingRules.append((QtCore.QRegExp("\\bclass [A-Za-z]+\\b"),
                classFormat))

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
