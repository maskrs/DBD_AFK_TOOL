# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DebugTool.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DebugDialog(object):
    def setupUi(self, DebugDialog):
        DebugDialog.setObjectName("DebugDialog")
        DebugDialog.resize(255, 335)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DebugDialog.sizePolicy().hasHeightForWidth())
        DebugDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(DebugDialog)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(DebugDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lb_coord = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_coord.sizePolicy().hasHeightForWidth())
        self.lb_coord.setSizePolicy(sizePolicy)
        self.lb_coord.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lb_coord.setObjectName("lb_coord")
        self.gridLayout_2.addWidget(self.lb_coord, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.le_coord = QtWidgets.QLineEdit(self.widget_3)
        self.le_coord.setMinimumSize(QtCore.QSize(100, 0))
        self.le_coord.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_coord.setText("")
        self.le_coord.setObjectName("le_coord")
        self.gridLayout_2.addWidget(self.le_coord, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.pb_selection_region = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_selection_region.sizePolicy().hasHeightForWidth())
        self.pb_selection_region.setSizePolicy(sizePolicy)
        self.pb_selection_region.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_selection_region.setMaximumSize(QtCore.QSize(75, 75))
        self.pb_selection_region.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pb_selection_region.setObjectName("pb_selection_region")
        self.horizontalLayout.addWidget(self.pb_selection_region)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(DebugDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_keywords = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_keywords.sizePolicy().hasHeightForWidth())
        self.lb_keywords.setSizePolicy(sizePolicy)
        self.lb_keywords.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lb_keywords.setObjectName("lb_keywords")
        self.gridLayout.addWidget(self.lb_keywords, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.pb_test = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_test.sizePolicy().hasHeightForWidth())
        self.pb_test.setSizePolicy(sizePolicy)
        self.pb_test.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pb_test.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pb_test.setObjectName("pb_test")
        self.gridLayout.addWidget(self.pb_test, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.le_keywords = QtWidgets.QLineEdit(self.widget_2)
        self.le_keywords.setMinimumSize(QtCore.QSize(100, 0))
        self.le_keywords.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_keywords.setObjectName("le_keywords")
        self.gridLayout.addWidget(self.le_keywords, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(DebugDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(9, 0, 10, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pe_result = QtWidgets.QPlainTextEdit(self.widget_4)
        self.pe_result.setMinimumSize(QtCore.QSize(0, 200))
        self.pe_result.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pe_result.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pe_result.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pe_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.pe_result.setReadOnly(True)
        self.pe_result.setPlainText("")
        self.pe_result.setOverwriteMode(False)
        self.pe_result.setMaximumBlockCount(0)
        self.pe_result.setBackgroundVisible(False)
        self.pe_result.setCenterOnScroll(False)
        self.pe_result.setObjectName("pe_result")
        self.verticalLayout_2.addWidget(self.pe_result)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(DebugDialog)
        QtCore.QMetaObject.connectSlotsByName(DebugDialog)

    def retranslateUi(self, DebugDialog):
        _translate = QtCore.QCoreApplication.translate
        DebugDialog.setWindowTitle(_translate("DebugDialog", "调试工具"))
        self.lb_coord.setText(_translate("DebugDialog", "识别范围："))
        self.pb_selection_region.setText(_translate("DebugDialog", "选择\n"
"区域"))
        self.lb_keywords.setText(_translate("DebugDialog", "识别关键字："))
        self.pb_test.setText(_translate("DebugDialog", "测试"))
