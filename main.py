from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtWidgets import QListWidget
from PySide6.QtCore import Qt

from main_ui import Ui_MainWindow

import sys

from search import searchDmhyXml
from search import searchResult

import pyperclip


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.copyButton.clicked.connect(self.copyToClipboard)
        self.searchModule = searchDmhyXml("")

    def getResultByWidget(self, widget: QListWidgetItem) -> searchResult:
        for i in self.searchModule.searchResult:
            if (i.widget == widget):
                return i
        return None

    def search(self):
        print('search')
        self.ui.searchResultList.clear()

        self.searchModule.searchStr = self.ui.searchInput.text()
        self.searchModule.doSearch()

        for i in self.searchModule.searchResult:
            qitem = QListWidgetItem()
            qitem.setText(i.title)
            qitem.setFlags(qitem.flags() | Qt.ItemIsUserCheckable)
            qitem.setCheckState(Qt.Unchecked)
            i.widget = qitem
            self.ui.searchResultList.addItem(qitem)

        self.ui.searchResultList.changeEvent

    def dataChanged(self, item):
        print(item)

    def save(self):
        print('save')

    def copyToClipboard(self):
        print('copy to clipboard')
        resultTorrents = []
        for r in self.searchModule.searchResult:
            if (r.widget is not None):
                if (r.widget.checkState() == Qt.Checked):
                    resultTorrents.append(r.torrent)
                    resultTorrents.append('\n')
                    resultTorrents.append('\n')
        cpyStr = ''.join(resultTorrents)
        print(cpyStr)
        pyperclip.copy(cpyStr)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    win = MainWindow()
    win.setWindowTitle("DMHY_torrent_Downloader")
    win.setWindowIcon(QtGui.QIcon("icon.png"))
    win.show()
    app.exit(app.exec_())
