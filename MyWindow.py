import catboost as cb
import pandas as pd
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog
import Preprocessing
from LoadingWindow import LoadingWindow
from Preprocessing import *
from Ui_MainWindow import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Main Window")

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton.clicked.connect(self.openDialog)
        self.pushButton.clicked.connect(self.load_data)
        #self.showButton.clicked.connect(self.show_results)

    def openDialog(self):
        self.dialog = LoadingWindow(self)
        self.dialog.show()

    def load_data(self):

        filename_covid_train = "covid_data_train.csv"
        fullpath_covid_train = QtCore.QDir.current().absoluteFilePath(filename_covid_train)
        data_covid_train = pd.read_csv("/Users/admin/Desktop/covid_data_train.csv")

        preprocessing = Preprocessing(data_covid_train)
        y, X, mean, std = preprocessing.data_preprocess(data_covid_train)

        file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                  "",
                                                  "All Files (*);;Python Files (*.py);;Text Files (*.txt);;CSV Files (*.csv)")

        data_val = pd.read_csv(file)
        preprocessing_val = Preprocessing(data_val)
        X_val = preprocessing_val.data_preprocess(data_val, test=True, mean=mean, std=std)

        cat_features = ['region_x']
        model = cb.CatBoostRegressor(loss_function='RMSE', cat_features=cat_features)
        model.fit(X, y, verbose=False)
        Y_val = model.predict(X_val)

        file = open("/Users/admin/Desktop/predict.txt", "w")
        file.write(str(Y_val[0]) + "\n")
        file.close()
