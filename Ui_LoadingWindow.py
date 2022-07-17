from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QToolTip


class Ui_LoadingWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 900)

        QToolTip.setFont(QFont('Times', 14))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(330, 340, 300, 40))
        self.showButton.setStyleSheet("QPushButton{\n"
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
                                      "background-color: rgba(0, 50, 50, 0.7);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "color: #CD853F ;\n"
                                      "}")
        self.showButton.setIcon(QIcon('/Users/admin/Desktop/covid.png'))
        self.showButton.setIconSize(QSize(100, 100))
        self.showButton.setObjectName("showButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 220, 300, 80))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label.setToolTip("Here you can view the predict frequency of infection")
        self.label.setStyleSheet("QLabel{\n"
                                 "font: 25pt \"Times\";\n"
                                 "color:#00FFFF ;\n"
                                 "border: none;\n"
                                 "}")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(610, 220, 300, 80))
        self.label2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label2.setObjectName("label")
        self.label2.setToolTip("Here you can view the predict frequency of infection")
        self.label2.setStyleSheet("QLabel{\n"
                                 "font: 25pt \"Times\";\n"
                                 "color:#00FFFF ;\n"
                                 "border: none;\n"
                                 "}")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showButton.setText(_translate("MainWindow", "Show"))
        self.label.setText(_translate("MainWindow", "Коэффициент заражения: "))
        self.label2.setText(_translate("MainWindow", " "))