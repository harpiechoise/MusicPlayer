# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pybar2000(object):
    def setupUi(self, Pybar2000):
        Pybar2000.setObjectName("Pybar2000")
        Pybar2000.resize(1050, 957)
        Pybar2000.setAutoFillBackground(False)
        Pybar2000.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"selection-color: rgb(179, 177, 177);")
        self.centralwidget = QtWidgets.QWidget(Pybar2000)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: #4a4a4a")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ToggleAudio = QtWidgets.QToolButton(self.centralwidget)
        self.ToggleAudio.setStyleSheet("")
        self.ToggleAudio.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/UI/altavoz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToggleAudio.setIcon(icon)
        self.ToggleAudio.setIconSize(QtCore.QSize(32, 20))
        self.ToggleAudio.setObjectName("ToggleAudio")
        self.horizontalLayout_8.addWidget(self.ToggleAudio)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Volumen = QtWidgets.QSlider(self.centralwidget)
        self.Volumen.setOrientation(QtCore.Qt.Horizontal)
        self.Volumen.setObjectName("Volumen")
        self.horizontalLayout_7.addWidget(self.Volumen)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.Atras = QtWidgets.QPushButton(self.centralwidget)
        self.Atras.setStyleSheet("")
        self.Atras.setObjectName("Atras")
        self.gridLayout_2.addWidget(self.Atras, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Explorer = QtWidgets.QListWidget(self.centralwidget)
        self.Explorer.setStyleSheet("background-color: rgb(86, 85, 84);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(54, 133, 181);")
        self.Explorer.setObjectName("Explorer")
        self.horizontalLayout.addWidget(self.Explorer)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Canciones = QtWidgets.QListWidget(self.centralwidget)
        self.Canciones.setStyleSheet("background-color: rgb(86, 85, 84);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(54, 133, 181);")
        self.Canciones.setObjectName("Canciones")
        self.horizontalLayout_2.addWidget(self.Canciones)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Information = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Information.sizePolicy().hasHeightForWidth())
        self.Information.setSizePolicy(sizePolicy)
        self.Information.setStyleSheet("background-color: rgb(86, 85, 84);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(54, 133, 181);")
        self.Information.setObjectName("Information")
        self.Information.setColumnCount(0)
        self.Information.setRowCount(0)
        self.Information.horizontalHeader().setSortIndicatorShown(False)
        self.Information.horizontalHeader().setStretchLastSection(True)
        self.Information.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.Information)
        self.Imagen = QtWidgets.QGraphicsView(self.centralwidget)
        self.Imagen.setStyleSheet("background-color: rgb(86, 85, 84);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(54, 133, 181);")
        self.Imagen.setObjectName("Imagen")
        self.verticalLayout.addWidget(self.Imagen)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 3, 1, 1)
        self.Progress = QtWidgets.QSlider(self.centralwidget)
        self.Progress.setOrientation(QtCore.Qt.Horizontal)
        self.Progress.setObjectName("Progress")
        self.gridLayout_2.addWidget(self.Progress, 3, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Prev = QtWidgets.QToolButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/UI/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Prev.setIcon(icon1)
        self.Prev.setIconSize(QtCore.QSize(32, 32))
        self.Prev.setObjectName("Prev")
        self.gridLayout.addWidget(self.Prev, 0, 0, 1, 1)
        self.Stop = QtWidgets.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("GUI/UI/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Stop.setIcon(icon2)
        self.Stop.setIconSize(QtCore.QSize(64, 64))
        self.Stop.setObjectName("Stop")
        self.gridLayout.addWidget(self.Stop, 0, 1, 1, 1)
        self.Play = QtWidgets.QToolButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("GUI/UI/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play.setIcon(icon3)
        self.Play.setIconSize(QtCore.QSize(64, 64))
        self.Play.setObjectName("Play")
        self.gridLayout.addWidget(self.Play, 0, 2, 1, 1)
        self.Next = QtWidgets.QToolButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("GUI/UI/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next.setIcon(icon4)
        self.Next.setIconSize(QtCore.QSize(32, 32))
        self.Next.setObjectName("Next")
        self.gridLayout.addWidget(self.Next, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 2, 1, 1)
        Pybar2000.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pybar2000)
        QtCore.QMetaObject.connectSlotsByName(Pybar2000)

    def retranslateUi(self, Pybar2000):
        _translate = QtCore.QCoreApplication.translate
        Pybar2000.setWindowTitle(_translate("Pybar2000", "JcPlayer2020"))
        self.Atras.setText(_translate("Pybar2000", "<<"))
        self.Prev.setText(_translate("Pybar2000", "..."))
        self.Stop.setText(_translate("Pybar2000", "..."))
        self.Play.setText(_translate("Pybar2000", "..."))
        self.Next.setText(_translate("Pybar2000", "..."))
