# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\2022-1\graduate_design\RedPanda\RedPanda\widgets\LabelView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 640)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LeftArea = QtWidgets.QDockWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftArea.sizePolicy().hasHeightForWidth())
        self.LeftArea.setSizePolicy(sizePolicy)
        self.LeftArea.setFloating(False)
        self.LeftArea.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable)
        self.LeftArea.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.LeftArea.setObjectName("LeftArea")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.NotDataArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NotDataArea.sizePolicy().hasHeightForWidth())
        self.NotDataArea.setSizePolicy(sizePolicy)
        self.NotDataArea.setWidgetResizable(True)
        self.NotDataArea.setObjectName("NotDataArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 85, 85))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.NotDataArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.NotDataArea)
        self.DataArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataArea.sizePolicy().hasHeightForWidth())
        self.DataArea.setSizePolicy(sizePolicy)
        self.DataArea.setWidgetResizable(True)
        self.DataArea.setObjectName("DataArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 85, 395))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.DataArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.DataArea)
        self.LeftArea.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.LeftArea)
        self.RightArea = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightArea.sizePolicy().hasHeightForWidth())
        self.RightArea.setSizePolicy(sizePolicy)
        self.RightArea.setObjectName("RightArea")
        self.horizontalLayout.addWidget(self.RightArea)
        self.verticalLayout.addWidget(self.widget)
        self.ToolArea = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolArea.sizePolicy().hasHeightForWidth())
        self.ToolArea.setSizePolicy(sizePolicy)
        self.ToolArea.setObjectName("ToolArea")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ToolArea)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.SaveShape_bt = QtWidgets.QPushButton(self.ToolArea)
        self.SaveShape_bt.setObjectName("SaveShape_bt")
        self.horizontalLayout_2.addWidget(self.SaveShape_bt)
        self.verticalLayout.addWidget(self.ToolArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LeftArea.setWindowTitle(_translate("Dialog", "Argument"))
        self.SaveShape_bt.setText(_translate("Dialog", "save shape"))
