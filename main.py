from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtWidgets import QListView
from PySide6.QtCore import Qt
from PySide6.QtCore import QStringListModel
from PySide6.QtCore import QThread, Signal
from PySide6.QtCore import QTimer


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
        self.ui.selectAllButton.clicked.connect(self.selectAll)
        self.ui.selectNoneButton.clicked.connect(self.selectNone)

        self.listModel = QStringListModel(self.dataManager.data)
        self.ui.saveList.setModel(self.listModel)
        self.ui.saveList.doubleClicked.connect(self.onDoubleClicked)
        self.ui.saveList.setEditTriggers(QListView.NoEditTriggers)

        self.isSearching = False
        self.ui.copyLabel.setText("")
        self.ui.InfoLabel.setText("")

    def getResultByWidget(self, widget: QListWidgetItem) -> SearchResult:
        for i in self.searchModule.searchResult:
            if (i.widget == widget):
                return i
        return None

    # def search(self):
    #     print('search')
    #     self.ui.searchResultList.clear()

    #     self.searchModule.searchStr = self.ui.searchInput.text()
    #     self.searchModule.doSearch()

    #     for i in self.searchModule.searchResult:
    #         qitem = QListWidgetItem()
    #         qitem.setText(i.title)
    #         qitem.setFlags(qitem.flags() | Qt.ItemIsUserCheckable)
    #         qitem.setCheckState(Qt.Checked)
    #         i.widget = qitem
    #         self.ui.searchResultList.addItem(qitem)

    def search(self):
        if not self.isSearching:
            self.isSearching = True
            self.ui.searchResultList.clear()
            self.ui.InfoLabel.setText("搜索中…")

            self.searchThread = SearchThread(self.searchModule)
            self.searchThread.finished.connect(self.onSearchFinished)
            self.searchThread.failed.connect(self.onSearchFailed)
            self.searchModule.searchStr = self.ui.searchInput.text()
            self.searchThread.start()

    def onSearchFinished(self, searchResult):
        self.isSearching = False
        self.ui.InfoLabel.setText("搜索完成")
        for i in searchResult:
            qitem = QListWidgetItem(i.title)
            qitem.setFlags(qitem.flags() | Qt.ItemIsUserCheckable)
            qitem.setCheckState(Qt.Checked)
            i.widget = qitem
            self.ui.searchResultList.addItem(qitem)

    def onSearchFailed(self):
        self.isSearching = False
        self.ui.InfoLabel.setText("搜索失败")

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
        self.ui.copyLabel.setText("复制成功")
        QTimer.singleShot(1500, self.resetInfoLabel)

    def resetInfoLabel(self):
        self.ui.copyLabel.setText("")

    def onDoubleClicked(self, index):
        if not self.isSearching:
            itemText = self.listModel.data(index)
            print(f"Double clicked on {itemText}")
            self.ui.searchInput.setText(itemText)
            self.search()

    def selectAll(self):
        for r in self.searchModule.searchResult:
            if (r.widget is not None):
                r.widget.setCheckState(Qt.Checked)

    def selectNone(self):
        for r in self.searchModule.searchResult:
            if (r.widget is not None):
                r.widget.setCheckState(Qt.Unchecked)


class SearchThread(QThread):
    finished = Signal(list)
    failed = Signal()  # 使用PySide6的Signal

    def __init__(self, searchModule):
        super(SearchThread, self).__init__()
        self.searchModule = searchModule

    def run(self):
        if not self.searchModule.doSearch():
            self.failed.emit()
        else:
            self.finished.emit(self.searchModule.searchResult)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    win = MainWindow()
    win.setWindowTitle("DMHY_torrent_Downloader")
    win.setWindowIcon(QtGui.QIcon("icon.png"))
    win.show()
    app.exit(app.exec_())
