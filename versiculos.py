# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'versiculos.ui'
#
# Created by: Lucash Sanjivala
# Version: 2.4.1
# Company: LSoft Corporation
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 431)
        MainWindow.setMinimumSize(QtCore.QSize(689, 431))
        MainWindow.setMaximumSize(QtCore.QSize(689, 431))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/Holy Bible.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background: transparent;")
        MainWindow.setIconSize(QtCore.QSize(25, 25))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 20, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(49)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.txtVersiculo = QtWidgets.QLabel(self.centralwidget)
        self.txtVersiculo.setGeometry(QtCore.QRect(120, 90, 451, 251))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.txtVersiculo.setFont(font)
        self.txtVersiculo.setStyleSheet(
            "background: rgba(255, 255, 255, .01);border-radius: 5px;padding: 0 8px;color: #fff;")
        self.txtVersiculo.setTextFormat(QtCore.Qt.AutoText)
        self.txtVersiculo.setScaledContents(True)
        self.txtVersiculo.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.txtVersiculo.setWordWrap(True)
        self.txtVersiculo.setOpenExternalLinks(False)
        self.txtVersiculo.setObjectName("txtVersiculo")
        self.btnAnterior = QtWidgets.QPushButton(self.centralwidget)
        self.btnAnterior.setGeometry(QtCore.QRect(30, 180, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnAnterior.setFont(font)
        self.btnAnterior.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAnterior.setStyleSheet(
            "QPushButton {border-radius: 30px;border: none;background: rgba(255,255,255,.05);"
            "}QPushButton:hover {background: rgba(255,255,255,.3);color: #f9f9f9;}")
        self.btnAnterior.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("files/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAnterior.setIcon(icon1)
        self.btnAnterior.setIconSize(QtCore.QSize(60, 60))
        self.btnAnterior.setObjectName("btnAnterior")
        self.btnProximo = QtWidgets.QPushButton(self.centralwidget)
        self.btnProximo.setGeometry(QtCore.QRect(600, 180, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnProximo.setFont(font)
        self.btnProximo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProximo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnProximo.setAutoFillBackground(False)
        self.btnProximo.setStyleSheet("QPushButton {border-radius: 30px;border: none;background:rgba(255,255,255,.05);"
                                      "}QPushButton:hover {background: rgba(255,255,255,.3);color: #f9f9f9;}")
        self.btnProximo.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("files/Forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProximo.setIcon(icon2)
        self.btnProximo.setIconSize(QtCore.QSize(60, 60))
        self.btnProximo.setObjectName("btnProximo")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-3, 330, 691, 16))
        self.line_2.setStyleSheet("background: transparent;color: #fff;")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-4, 350, 701, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setMouseTracking(True)
        self.label_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_3.setAcceptDrops(False)
        self.label_3.setStyleSheet("color: #f9f9f9;\nbackground:transparent;")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 691, 251))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("files/club.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 340, 691, 91))
        self.label_4.setStyleSheet("background: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(69, 77, 14, "
                                   "255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), "
                                   "stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), "
                                   "stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), "
                                   "stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), "
                                   "stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), "
                                   "stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), "
                                   "stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));color: #fff;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("files/club.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 691, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("files/club.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 80, 691, 16))
        self.line_3.setStyleSheet("background: transparent;\ncolor: #fff;")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.txtVersiculo.raise_()
        self.btnAnterior.raise_()
        self.btnProximo.raise_()
        self.line_2.raise_()
        self.label_3.raise_()
        self.line_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lista = []
        self.aleatorio = random.randint
        self.numero = 0
        self.antes = 0
        self.ficheiro = open('versiculos.txt', 'r')

        self.leitor()

        self.btnProximo.clicked.connect(self.proximo)
        self.btnAnterior.clicked.connect(self.anterior)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Leitor de Versículos v2.4.1"))
        self.label.setText(_translate("MainWindow", "Leitor de Versículos"))
        self.txtVersiculo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" "
                                                           "font-size:10pt;\">Aquele que habita no esconderijo do "
                                                           "Altíssimo, à sombra do Omnipotente "
                                                           "descansará.</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Porque Deus amou o mundo de tal maneira que deu o Seu Filho "
                                                      "Unigénito, para que todo aquele que nEle crê não pereça, "
                                                      "mas tenha a vida eterna"))

    def leitor(self):
        contador = 0
        for item in self.ficheiro:
            self.lista.append(item.replace('->', '\n\n\t'))
            # print(contador, ' -> ', item)
            contador += 1
        if len(self.lista) == 0 or contador == 0:
            pass
        else:
            self.antes = self.aleatorio(0, len(self.lista) - 1)
            self.txtVersiculo.setText(self.lista[self.antes])
            # print('Lista: ', len(self.lista) - 1)
            # print('Antes: ', self.antes)

    def proximo(self):
        tamanho_lista = len(self.lista) - 1
        if self.numero == 0:
            self.numero = self.aleatorio(0, tamanho_lista)
            self.txtVersiculo.setText(self.lista[self.numero])
        else:
            self.antes = self.numero
            self.numero = self.aleatorio(0, tamanho_lista)
            self.txtVersiculo.setText(self.lista[self.numero])
        # print('Número: ', self.numero)
        # print('Antes: ', self.antes)

    def anterior(self):
        if self.numero == 0:
            self.antes = self.aleatorio(0, self.aleatorio(0, len(self.lista) - 1))
            self.txtVersiculo.setText(self.lista[self.antes])
        elif self.numero != 0:
            self.txtVersiculo.setText(self.lista[self.antes])
            self.numero = 0
        # print('Antes: ', self.antes)


if __name__ == "__main__":
    import sys

    arquivo = open('versiculos.txt', 'r')
    arquivo.close()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
