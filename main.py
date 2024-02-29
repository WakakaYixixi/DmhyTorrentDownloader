from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtCore import QStringListModel

from main_ui import Ui_MainWindow

import sys

from search import SearchDmhyXml
from search import SearchResult

from save_data import SaveData

import pyperclip


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.dataManager = SaveData('save_data.cfg')
        self.dataManager.readData()
        self.searchModule = SearchDmhyXml("")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.copyButton.clicked.connect(self.copyToClipboard)
        self.ui.deleteButton.clicked.connect(self.remove)

        self.listModel = QStringListModel(self.dataManager.data)
        self.ui.saveList.setModel(self.listModel)
        self.ui.saveList.doubleClicked.connect(self.onDoubleClicked)

    def getResultByWidget(self, widget: QListWidgetItem) -> SearchResult:
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
            qitem.setCheckState(Qt.Checked)
            i.widget = qitem
            self.ui.searchResultList.addItem(qitem)

    def save(self):
        newItem = self.ui.searchInput.text()
        if (newItem):
            if newItem not in self.dataManager.data:
                print('save')
                self.dataManager.data.append(newItem)
                self.listModel.setStringList(self.dataManager.data)
            self.dataManager.writeData()
        else:
            print('save failed: text empty')

    def remove(self):
        indexes = self.ui.saveList.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.dataManager.data[index.row()]
            self.listModel.setStringList(self.dataManager.data)
            self.dataManager.writeData()

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

    def onDoubleClicked(self, index):
        itemText = self.listModel.data(index)
        print(f"Double clicked on {itemText}")
        self.ui.searchInput.setText(itemText)
        self.search()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    win = MainWindow()
    win.setWindowTitle("DMHY_torrent_Downloader")
    win.setWindowIcon(QtGui.QIcon("icon.png"))
    win.show()
    app.exit(app.exec_())
