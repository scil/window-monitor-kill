# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui',
# licensing of 'widget.ui' applies.
#
# Created: Thu Sep  5 08:44:49 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(416, 281)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 351, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.restartBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.restartBtn.setText("")
        self.restartBtn.setObjectName("restartBtn")
        self.horizontalLayout.addWidget(self.restartBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.processSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processSlider.sizePolicy().hasHeightForWidth())
        self.processSlider.setSizePolicy(sizePolicy)
        self.processSlider.setOrientation(QtCore.Qt.Horizontal)
        self.processSlider.setObjectName("processSlider")
        self.verticalLayout.addWidget(self.processSlider)
        self.timeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout.addWidget(self.timeLabel)
        self.infoLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.timeLabel.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))

