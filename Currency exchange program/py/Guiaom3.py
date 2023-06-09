# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Guiaom.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Guiaom(object):
    def __init__(self, num):
        self.num = num
        print(num)
    def money(self):
        result = self.lineEdit.text()
        self.lineEdit.setText("")
        num = self.num
        change = float(num) * float(result)
        print(change)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.appendPlainText(f"\tYour money from THB = {str(change)}")
        change_type = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
        for t in change_type:
            if change >= t:
                self.plainTextEdit.appendPlainText(f"\t{t} THB = {int(change / t)}")
                change = change % t
        self.plainTextEdit.appendPlainText("\tthankyou see you soon")
    def setupUi(self, Guiaom):
        Guiaom.setObjectName("Guiaom")
        Guiaom.resize(1200, 800)
        Guiaom.setMaximumSize(QtCore.QSize(1200, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/3743e35ed787b84af56132056fcf166e.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Guiaom.setWindowIcon(icon)
        Guiaom.setStyleSheet("background-image: url(:/A1/141894_00_2x.jpg);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Guiaom)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 480, 351, 271))
        self.frame.setStyleSheet("background-image: url(:/A1/c24f248f8280a0035d193db844eebaec.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 30, 456, 269))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-image: url(:/A1/abstract-halftone-background_23-2148583453.jpg);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMaximumSize(QtCore.QSize(500, 60))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-image: url(:/A1/1876a4e9d6b9ba091d2516b3eab92db7.jpg);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("background-image: url(:/A1/abstract-halftone-background_23-2148583453.jpg);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.money)
        self.verticalLayout.addWidget(self.pushButton)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(540, 30, 621, 271))
        self.plainTextEdit.setStyleSheet("background-image: url(:/A1/1876a4e9d6b9ba091d2516b3eab92db7.jpg);\n"
"color: rgb(170, 0, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 370, 191, 101))
        self.frame_2.setStyleSheet("image: url(:/A4/15755222747183.jpg);\n"
"image: url(:/A1/images.jfif);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(550, 370, 181, 101))
        self.frame_3.setStyleSheet("image: url(:/A4/6w7gqo.jpg);\n"
"image: url(:/A1/_100325862_100_17f--1.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(760, 380, 181, 91))
        self.frame_5.setStyleSheet("\n"
"image: url(:/A1/6w7gqo.jpg);\n"
"image: url(:/A1/6w7gqo.jpg);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(640, 500, 211, 101))
        self.frame_4.setStyleSheet("image: url(:/A4/unnamed.jpg);\n"
"image: url(:/A1/AL15_b1000f2.gif);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(380, 500, 211, 101))
        self.frame_6.setStyleSheet("image: url(:/A4/AL15_b1000f2.gif);\n"
"border-image: url(:/A1/unnamed.jpg);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(463, 640, 371, 71))
        self.pushButton_2.setStyleSheet("background-image: url(:/A1/abstract-halftone-background_23-2148583453.jpg);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        Guiaom.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Guiaom)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        Guiaom.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Guiaom)
        self.statusbar.setObjectName("statusbar")
        Guiaom.setStatusBar(self.statusbar)

        self.retranslateUi(Guiaom)
        QtCore.QMetaObject.connectSlotsByName(Guiaom)

    def retranslateUi(self, Guiaom):
        _translate = QtCore.QCoreApplication.translate
        Guiaom.setWindowTitle(_translate("Guiaom", "Currency exchange program"))
        self.label.setText(_translate("Guiaom", "Please enter your amount"))
        self.pushButton.setText(_translate("Guiaom", "Enter"))
import imaom_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Guiaom = QtWidgets.QMainWindow()
    ui = Ui_Guiaom()
    ui.setupUi(Guiaom)
    Guiaom.show()
    sys.exit(app.exec_())
