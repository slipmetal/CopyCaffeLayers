# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './get_caffe.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Ui.CopyWindowUi import ClickLineEdit

class Ui_GetCaffeForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(282, 202)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 261, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.CaffelineEdit = ClickLineEdit(self.verticalLayoutWidget)
        self.CaffelineEdit.setObjectName("CaffelineEdit")
        self.verticalLayout.addWidget(self.CaffelineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.OKpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.OKpushButton.setObjectName("OKpushButton")
        self.horizontalLayout.addWidget(self.OKpushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Get Caffe"))
        self.label.setText(_translate("Form", "Please, choose the path to Caffe"))
        self.OKpushButton.setText(_translate("Form", "OK"))

