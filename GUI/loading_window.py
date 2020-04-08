# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/cargando.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CargandoWindow(object):
    def setupUi(self, CargandoWindow):
        CargandoWindow.setObjectName("CargandoWindow")
        CargandoWindow.resize(705, 219)
        CargandoWindow.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"selection-color: rgb(179, 177, 177);")
        self.centralwidget = QtWidgets.QWidget(CargandoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 130, 130))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MovieScreen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.MovieScreen.setText("")
        self.MovieScreen.setScaledContents(True)
        self.MovieScreen.setObjectName("MovieScreen")
        self.verticalLayout.addWidget(self.MovieScreen)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(160, 129, 511, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(160, 90, 511, 31))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.InfoLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.InfoLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.InfoLabel.setObjectName("InfoLabel")
        self.verticalLayout_3.addWidget(self.InfoLabel)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(160, 30, 511, 31))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Info2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(14)
        self.Info2.setFont(font)
        self.Info2.setStyleSheet("color:rgb(255, 255, 255)")
        self.Info2.setObjectName("Info2")
        self.verticalLayout_4.addWidget(self.Info2)
        CargandoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CargandoWindow)
        QtCore.QMetaObject.connectSlotsByName(CargandoWindow)

    def retranslateUi(self, CargandoWindow):
        _translate = QtCore.QCoreApplication.translate
        CargandoWindow.setWindowTitle(_translate("CargandoWindow", "MainWindow"))
        self.InfoLabel.setText(_translate("CargandoWindow", "Info"))
        self.Info2.setText(_translate("CargandoWindow", "Importando Canciones"))
