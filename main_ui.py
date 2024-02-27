# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QSize(960, 540))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.verticalLayout_2.addWidget(self.deleteButton)

        self.saveList = QListView(self.centralwidget)
        self.saveList.setObjectName(u"saveList")
        self.saveList.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveList.sizePolicy().hasHeightForWidth())
        self.saveList.setSizePolicy(sizePolicy)
        self.saveList.setMinimumSize(QSize(300, 0))

        self.verticalLayout_2.addWidget(self.saveList)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchInput = QLineEdit(self.centralwidget)
        self.searchInput.setObjectName(u"searchInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchInput.sizePolicy().hasHeightForWidth())
        self.searchInput.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.searchInput)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy1.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.searchButton)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy1.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.saveButton)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.searchResultList = QListWidget(self.centralwidget)
        self.searchResultList.setObjectName(u"searchResultList")

        self.verticalLayout.addWidget(self.searchResultList)

        self.copyButton = QPushButton(self.centralwidget)
        self.copyButton.setObjectName(u"copyButton")

        self.verticalLayout.addWidget(self.copyButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u8bb0\u5f55", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8bb0\u5f55", None))
        self.copyButton.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u78c1\u529b\u94fe\u63a5", None))
    # retranslateUi

