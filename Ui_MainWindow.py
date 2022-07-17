from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QToolTip

class Ui_MainWindow(object):

    def setupUi(self, MyWindow):
        MyWindow.setObjectName("ResultWindow")
        MyWindow.resize(901, 900)

        QToolTip.setFont(QFont('Times', 14))
        self.centralwidget = QtWidgets.QWidget(MyWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(585, 10, 101, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 20pt \"Times\";")
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{\n"
                                 "font: 22pt \"Times\";\n"
                                 "color:#00FFFF ;\n"
                                 "border: none;\n"
                                 "}")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 280, 300, 40))
        self.pushButton.setToolTip("Click here to load data")
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "font: 22pt \"Times\";\n"
                                      "color:#00FFFF ;\n"
                                      "min-width: 180px; \n"
                                      "max-width: 180px; \n"
                                      "min-height: 180px; \n"
                                      "max-height: 180px; \n"
                                      "border-radius: 90px; \n"
                                      "background-color: rgba(0, 50, 50, 0.7);\n"
                                      "border: none ;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "color:#7CFC00 ;\n"
                                      "background-color: rgba(0, 50, 50, 0.8);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "color: #CD853F ;\n"
                                      "}")
        self.pushButton.setIcon(QIcon('/Users/admin/Desktop/covid.png'))
        self.pushButton.setIconSize(QSize(80, 80))
        self.pushButton.setObjectName("pushButton")

        self.statusbar = QtWidgets.QStatusBar(MyWindow)
        self.statusbar.setObjectName("statusbar")
        MyWindow.setStatusBar(self.statusbar)

        MyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi2(MyWindow)
        QtCore.QMetaObject.connectSlotsByName(MyWindow)

    def retranslateUi2(self, MyWindow):
        _translate = QtCore.QCoreApplication.translate
        MyWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Load data"))

