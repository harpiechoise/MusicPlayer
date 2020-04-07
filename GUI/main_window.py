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
        Pybar2000.resize(1142, 862)
        Pybar2000.setAutoFillBackground(False)
        Pybar2000.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.centralwidget = QtWidgets.QWidget(Pybar2000)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: #4a4a4a")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Volumen = QtWidgets.QSlider(self.centralwidget)
        self.Volumen.setOrientation(QtCore.Qt.Horizontal)
        self.Volumen.setObjectName("Volumen")
        self.horizontalLayout_7.addWidget(self.Volumen)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 2, 1, 4)
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
        self.gridLayout.addLayout(self.verticalLayout, 1, 8, 3, 2)
        self.Atras = QtWidgets.QPushButton(self.centralwidget)
        self.Atras.setStyleSheet("")
        self.Atras.setObjectName("Atras")
        self.gridLayout.addWidget(self.Atras, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Explorer = QtWidgets.QListWidget(self.centralwidget)
        self.Explorer.setStyleSheet("background-color: rgb(86, 85, 84);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(54, 133, 181);")
        self.Explorer.setObjectName("Explorer")
        self.horizontalLayout.addWidget(self.Explorer)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Canciones = QtWidgets.QListWidget(self.centralwidget)
        self.Canciones.setStyleSheet("background-color: rgb(86, 85, 84);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(54, 133, 181);")
        self.Canciones.setObjectName("Canciones")
        self.horizontalLayout_2.addWidget(self.Canciones)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 5, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Progress = QtWidgets.QSlider(self.centralwidget)
        self.Progress.setOrientation(QtCore.Qt.Horizontal)
        self.Progress.setObjectName("Progress")
        self.horizontalLayout_3.addWidget(self.Progress)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 10)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Prev = QtWidgets.QPushButton(self.centralwidget)
        self.Prev.setObjectName("Prev")
        self.horizontalLayout_10.addWidget(self.Prev)
        self.gridLayout.addLayout(self.horizontalLayout_10, 5, 0, 1, 3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setObjectName("Stop")
        self.horizontalLayout_6.addWidget(self.Stop)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 3, 1, 3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setObjectName("Play")
        self.horizontalLayout_4.addWidget(self.Play)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 6, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setObjectName("Pause")
        self.horizontalLayout_5.addWidget(self.Pause)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 7, 1, 2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setObjectName("Next")
        self.horizontalLayout_9.addWidget(self.Next)
        self.gridLayout.addLayout(self.horizontalLayout_9, 5, 9, 1, 1)
        Pybar2000.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pybar2000)
        QtCore.QMetaObject.connectSlotsByName(Pybar2000)

    def retranslateUi(self, Pybar2000):
        _translate = QtCore.QCoreApplication.translate
        Pybar2000.setWindowTitle(_translate("Pybar2000", "JcPlayer2020"))
        self.Atras.setText(_translate("Pybar2000", "<<"))
        self.Prev.setText(_translate("Pybar2000", "<< Anterior"))
        self.Stop.setText(_translate("Pybar2000", "Parar"))
        self.Play.setText(_translate("Pybar2000", "Reproducir"))
        self.Pause.setText(_translate("Pybar2000", "Pausar"))
        self.Next.setText(_translate("Pybar2000", "Siguiente >>"))
