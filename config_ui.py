# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(585, 404)
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(350, 360, 93, 28))
        self.save.setObjectName("save")
        self.return_2 = QtWidgets.QPushButton(Dialog)
        self.return_2.setGeometry(QtCore.QRect(460, 360, 93, 28))
        self.return_2.setObjectName("return_2")
        self.radioButton_1 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_1.setGeometry(QtCore.QRect(20, 10, 115, 19))
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 110, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 210, 115, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 40, 534, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 1, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 140, 534, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 3, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 3, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 1, 3, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 2, 3, 1, 1)
        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(50, 240, 41, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(Dialog)
        self.label_29.setGeometry(QtCore.QRect(30, 290, 91, 16))
        self.label_29.setObjectName("label_29")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(130, 290, 61, 16))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(20)
        self.spinBox.setProperty("value", 2)
        self.spinBox.setObjectName("spinBox")
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(40, 320, 91, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setGeometry(QtCore.QRect(40, 350, 91, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(Dialog)
        self.label_32.setGeometry(QtCore.QRect(240, 230, 91, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(Dialog)
        self.label_33.setGeometry(QtCore.QRect(240, 260, 91, 16))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(Dialog)
        self.label_34.setGeometry(QtCore.QRect(210, 290, 111, 16))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(Dialog)
        self.label_35.setGeometry(QtCore.QRect(200, 320, 121, 16))
        self.label_35.setObjectName("label_35")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 320, 61, 16))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(100000)
        self.spinBox_2.setProperty("value", 200)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(130, 350, 61, 16))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(100)
        self.spinBox_3.setProperty("value", 30)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(320, 230, 61, 16))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(10000)
        self.spinBox_4.setProperty("value", 1000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(320, 260, 61, 16))
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(10000)
        self.spinBox_5.setProperty("value", 1000)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(320, 290, 61, 16))
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(100000)
        self.spinBox_6.setProperty("value", 100)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_7.setGeometry(QtCore.QRect(320, 320, 61, 16))
        self.spinBox_7.setMinimum(1)
        self.spinBox_7.setMaximum(10000)
        self.spinBox_7.setProperty("value", 10)
        self.spinBox_7.setObjectName("spinBox_7")
        self.label_36 = QtWidgets.QLabel(Dialog)
        self.label_36.setGeometry(QtCore.QRect(390, 230, 101, 16))
        self.label_36.setObjectName("label_36")
        self.spinBox_8 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_8.setGeometry(QtCore.QRect(490, 230, 81, 16))
        self.spinBox_8.setMinimum(1)
        self.spinBox_8.setMaximum(100000000)
        self.spinBox_8.setProperty("value", 42)
        self.spinBox_8.setObjectName("spinBox_8")
        self.label_37 = QtWidgets.QLabel(Dialog)
        self.label_37.setGeometry(QtCore.QRect(390, 260, 146, 15))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(Dialog)
        self.label_38.setGeometry(QtCore.QRect(390, 290, 146, 15))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(Dialog)
        self.label_39.setGeometry(QtCore.QRect(390, 320, 146, 15))
        self.label_39.setObjectName("label_39")
        self.spinBox_9 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_9.setGeometry(QtCore.QRect(490, 260, 81, 16))
        self.spinBox_9.setMinimum(1)
        self.spinBox_9.setMaximum(100000000)
        self.spinBox_9.setProperty("value", 42)
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_10 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_10.setGeometry(QtCore.QRect(490, 290, 81, 16))
        self.spinBox_10.setMinimum(1)
        self.spinBox_10.setMaximum(10000)
        self.spinBox_10.setProperty("value", 100)
        self.spinBox_10.setObjectName("spinBox_10")
        self.spinBox_11 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_11.setGeometry(QtCore.QRect(490, 320, 81, 16))
        self.spinBox_11.setMinimum(1)
        self.spinBox_11.setMaximum(100000000)
        self.spinBox_11.setProperty("value", 10000000)
        self.spinBox_11.setObjectName("spinBox_11")
        self.checkBox_1 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_1.setGeometry(QtCore.QRect(100, 240, 91, 19))
        self.checkBox_1.setChecked(True)
        self.checkBox_1.setObjectName("checkBox_1")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(100, 260, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.buttonGroup.addButton(self.checkBox_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.save.setText(_translate("Dialog", "应用修改"))
        self.return_2.setText(_translate("Dialog", "返回上一层"))
        self.radioButton_1.setText(_translate("Dialog", "预设配置1"))
        self.radioButton_2.setText(_translate("Dialog", "预设配置2"))
        self.radioButton_3.setText(_translate("Dialog", "自定义配置"))
        self.label_9.setText(_translate("Dialog", "场地长度：1000"))
        self.label_7.setText(_translate("Dialog", "场地宽度：1000"))
        self.label_11.setText(_translate("Dialog", "垃圾最大重量：100"))
        self.label_22.setText(_translate("Dialog", "迭代上限/次：10000000"))
        self.label_10.setText(_translate("Dialog", "最大计算时间/s：25"))
        self.label_8.setText(_translate("Dialog", "垃圾数量：40"))
        self.label_6.setText(_translate("Dialog", "载重上限：无穷"))
        self.label_23.setText(_translate("Dialog", "模型随机种子：42"))
        self.label_24.setText(_translate("Dialog", "刷新间隔/ms：100"))
        self.label_12.setText(_translate("Dialog", "数据随机种子：42"))
        self.label_5.setText(_translate("Dialog", "垃圾车数量：1"))
        self.label_4.setText(_translate("Dialog", "内核：组内交换"))
        self.label_13.setText(_translate("Dialog", "场地长度：1000"))
        self.label_14.setText(_translate("Dialog", "最大计算时间/s：40"))
        self.label_15.setText(_translate("Dialog", "场地宽度：1000"))
        self.label_16.setText(_translate("Dialog", "垃圾最大重量：100"))
        self.label_17.setText(_translate("Dialog", "垃圾数量：60"))
        self.label_18.setText(_translate("Dialog", "内核：组间调整"))
        self.label_19.setText(_translate("Dialog", "数据随机种子：42"))
        self.label_20.setText(_translate("Dialog", "垃圾车数量：6"))
        self.label_21.setText(_translate("Dialog", "载重上限：1000"))
        self.label_25.setText(_translate("Dialog", "迭代上限/次：5000000"))
        self.label_26.setText(_translate("Dialog", "模型随机种子：42"))
        self.label_27.setText(_translate("Dialog", "刷新间隔/ms：100"))
        self.label_28.setText(_translate("Dialog", "内核："))
        self.label_29.setText(_translate("Dialog", "垃圾车数量："))
        self.label_30.setText(_translate("Dialog", "载重上限："))
        self.label_31.setText(_translate("Dialog", "垃圾数量："))
        self.label_32.setText(_translate("Dialog", "场地宽度："))
        self.label_33.setText(_translate("Dialog", "场地长度："))
        self.label_34.setText(_translate("Dialog", "垃圾最大重量："))
        self.label_35.setText(_translate("Dialog", "最大计算时间/s："))
        self.label_36.setText(_translate("Dialog", "数据随机种子："))
        self.label_37.setText(_translate("Dialog", "模型随机种子："))
        self.label_38.setText(_translate("Dialog", "刷新间隔/ms:"))
        self.label_39.setText(_translate("Dialog", "迭代上限/次："))
        self.checkBox_1.setText(_translate("Dialog", "组内交换"))
        self.checkBox_2.setText(_translate("Dialog", "组间调整"))
