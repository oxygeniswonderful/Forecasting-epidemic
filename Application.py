import sys
from PyQt5 import QtWidgets
from MyWindow import MyWindow
from Ui_MainWindow import Ui_MainWindow

if __name__ == "__main__":

    stylesheet = """
            QMainWindow {
                background-image: url("/Users/admin/Desktop/Projects/Epidemic/EpidemicFon.jpeg"); 
                background-repeat: no-repeat; 
                background-position: center;
            }
        """

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    win = MyWindow()
    win.show()

    sys.exit(app.exec_())

