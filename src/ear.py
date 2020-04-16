import sys
from PyQt5.QtCore import pyqtSlot, QRegExp
from PyQt5.QtGui import QColor, QRegExpValidator, QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtWidgets import (
    QApplication,
    QLineEdit,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)


class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super(SyntaxHighlighter, self).__init__(parent)
        self._highlight_lines = dict()

    def highlight_line(self, line, fmt):
        if isinstance(line, int) and line >= 0 and isinstance(fmt, QTextCharFormat):
            self._highlight_lines[line] = fmt
            tb = self.document().findBlockByLineNumber(line)
            self.rehighlightBlock(tb)

    def clear_highlight(self):
        self._highlight_lines = dict()
        self.rehighlight()

    def highlightBlock(self, text):
        line = self.currentBlock().blockNumber()
        fmt = self._highlight_lines.get(line)
        if fmt is not None:
            self.setFormat(0, len(text), fmt)


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self._lineedit = QLineEdit(textChanged=self.onTextChanged)
        regex_validator = QRegExpValidator(QRegExp(r"[0-9 ]+"))
        self._lineedit.setValidator(regex_validator)

        self._plaintextedit = QPlainTextEdit()

        self._highlighter = SyntaxHighlighter(self._plaintextedit.document())

        lay = QVBoxLayout(self)
        lay.addWidget(self._lineedit)
        lay.addWidget(self._plaintextedit)

        for i in range(10):
            self._plaintextedit.appendPlainText("line %d" % i)

        self.resize(720, 720)

    @pyqtSlot(str)
    def onTextChanged(self, text):
        fmt = QTextCharFormat()
        fmt.setBackground(QColor("yellow"))
        self._highlighter.clear_highlight()
        for e in text.split():
            line = int(e)
            self._highlighter.highlight_line(line, fmt)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())