# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\2022-1\graduate_design\RedPanda\RedPanda\widgets\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logic_View = qtViewer3d(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.logic_View.sizePolicy().hasHeightForWidth())
        self.logic_View.setSizePolicy(sizePolicy)
        self.logic_View.setObjectName("logic_View")
        self.verticalLayout_2.addWidget(self.logic_View)
        self.logic_View2d = qtViewer2d(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.logic_View2d.sizePolicy().hasHeightForWidth())
        self.logic_View2d.setSizePolicy(sizePolicy)
        self.logic_View2d.setObjectName("logic_View2d")
        self.verticalLayout_2.addWidget(self.logic_View2d)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 23))
        self.menubar.setObjectName("menubar")
        self.start = QtWidgets.QMenu(self.menubar)
        self.start.setObjectName("start")
        self.menuopen = QtWidgets.QMenu(self.start)
        self.menuopen.setObjectName("menuopen")
        self.menuNew = QtWidgets.QMenu(self.start)
        self.menuNew.setObjectName("menuNew")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.object_widget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_widget.sizePolicy().hasHeightForWidth())
        self.object_widget.setSizePolicy(sizePolicy)
        self.object_widget.setObjectName("object_widget")
        self.logic_Construct = Logic_ConstructView()
        self.logic_Construct.setObjectName("logic_Construct")
        self.object_widget.setWidget(self.logic_Construct)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.object_widget)
        self.view_message_widget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_message_widget.sizePolicy().hasHeightForWidth())
        self.view_message_widget.setSizePolicy(sizePolicy)
        self.view_message_widget.setObjectName("view_message_widget")
        self.logic_ViewData = Logic_ScreenData()
        self.logic_ViewData.setObjectName("logic_ViewData")
        self.view_message_widget.setWidget(self.logic_ViewData)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.view_message_widget)
        self.document_widget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.document_widget.sizePolicy().hasHeightForWidth())
        self.document_widget.setSizePolicy(sizePolicy)
        self.document_widget.setObjectName("document_widget")
        self.logic_DocData = Logic_DocView()
        self.logic_DocData.setObjectName("logic_DocData")
        self.document_widget.setWidget(self.logic_DocData)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.document_widget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionstep = QtWidgets.QAction(MainWindow)
        self.actionstep.setObjectName("actionstep")
        self.actionxml = QtWidgets.QAction(MainWindow)
        self.actionxml.setObjectName("actionxml")
        self.actionBox = QtWidgets.QAction(MainWindow)
        self.actionBox.setObjectName("actionBox")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.menuopen.addAction(self.actionstep)
        self.menuNew.addAction(self.actionxml)
        self.start.addAction(self.menuNew.menuAction())
        self.start.addAction(self.menuopen.menuAction())
        self.menubar.addAction(self.start.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setTitle(_translate("MainWindow", "开始"))
        self.menuopen.setTitle(_translate("MainWindow", "open"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menu.setTitle(_translate("MainWindow", "建模"))
        self.object_widget.setWindowTitle(_translate("MainWindow", "construct_and_change"))
        self.view_message_widget.setWindowTitle(_translate("MainWindow", "可视化信息"))
        self.document_widget.setWindowTitle(_translate("MainWindow", "document"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionstep.setText(_translate("MainWindow", "step"))
        self.actionxml.setText(_translate("MainWindow", "xml"))
        self.actionBox.setText(_translate("MainWindow", "Box"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
from RedPanda.widgets.Logic_ConstructView import Logic_ConstructView
from RedPanda.widgets.Logic_DocView import Logic_DocView
from RedPanda.widgets.Logic_ScreenData import Logic_ScreenData
from RedPanda.widgets.Logic_Viewer import qtViewer3d
from RedPanda.widgets.Logic_Viewer2d import qtViewer2d
