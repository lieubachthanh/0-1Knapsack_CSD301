# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UIDesign/random_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dgRandom(object):
    def setupUi(self, dgRandom):
        dgRandom.setObjectName("dgRandom")
        dgRandom.resize(500, 300)
        dgRandom.setMinimumSize(QtCore.QSize(500, 300))
        dgRandom.setMaximumSize(QtCore.QSize(500, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(dgRandom)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wg_maxWeight = QtWidgets.QWidget(dgRandom)
        self.wg_maxWeight.setEnabled(True)
        self.wg_maxWeight.setObjectName("wg_maxWeight")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wg_maxWeight)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_maximumWeight = QtWidgets.QLabel(self.wg_maxWeight)
        self.lb_maximumWeight.setEnabled(True)
        self.lb_maximumWeight.setObjectName("lb_maximumWeight")
        self.horizontalLayout.addWidget(self.lb_maximumWeight)
        self.spb_maximumWeight = QtWidgets.QSpinBox(self.wg_maxWeight)
        self.spb_maximumWeight.setEnabled(True)
        self.spb_maximumWeight.setMaximum(1000000)
        self.spb_maximumWeight.setProperty("value", 1000)
        self.spb_maximumWeight.setObjectName("spb_maximumWeight")
        self.horizontalLayout.addWidget(self.spb_maximumWeight)
        self.verticalLayout.addWidget(self.wg_maxWeight)
        self.wg_maxPrice = QtWidgets.QWidget(dgRandom)
        self.wg_maxPrice.setEnabled(True)
        self.wg_maxPrice.setObjectName("wg_maxPrice")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.wg_maxPrice)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb_maximumPrice = QtWidgets.QLabel(self.wg_maxPrice)
        self.lb_maximumPrice.setEnabled(True)
        self.lb_maximumPrice.setObjectName("lb_maximumPrice")
        self.horizontalLayout_4.addWidget(self.lb_maximumPrice)
        self.spb_maximumPrice = QtWidgets.QSpinBox(self.wg_maxPrice)
        self.spb_maximumPrice.setEnabled(True)
        self.spb_maximumPrice.setMaximum(1000000)
        self.spb_maximumPrice.setProperty("value", 1000)
        self.spb_maximumPrice.setObjectName("spb_maximumPrice")
        self.horizontalLayout_4.addWidget(self.spb_maximumPrice)
        self.verticalLayout.addWidget(self.wg_maxPrice)
        self.wg_count = QtWidgets.QWidget(dgRandom)
        self.wg_count.setEnabled(True)
        self.wg_count.setObjectName("wg_count")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wg_count)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_count = QtWidgets.QLabel(self.wg_count)
        self.lb_count.setEnabled(True)
        self.lb_count.setObjectName("lb_count")
        self.horizontalLayout_2.addWidget(self.lb_count)
        self.spb_count = QtWidgets.QSpinBox(self.wg_count)
        self.spb_count.setEnabled(True)
        self.spb_count.setMaximum(10000)
        self.spb_count.setProperty("value", 100)
        self.spb_count.setObjectName("spb_count")
        self.horizontalLayout_2.addWidget(self.spb_count)
        self.verticalLayout.addWidget(self.wg_count)
        self.wg_createOption = QtWidgets.QWidget(dgRandom)
        self.wg_createOption.setEnabled(True)
        self.wg_createOption.setObjectName("wg_createOption")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wg_createOption)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_weightOnly = QtWidgets.QCheckBox(self.wg_createOption)
        self.cb_weightOnly.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cb_weightOnly.setObjectName("cb_weightOnly")
        self.verticalLayout_2.addWidget(self.cb_weightOnly)
        self.cb_clearExisted = QtWidgets.QCheckBox(self.wg_createOption)
        self.cb_clearExisted.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cb_clearExisted.setChecked(True)
        self.cb_clearExisted.setObjectName("cb_clearExisted")
        self.verticalLayout_2.addWidget(self.cb_clearExisted)
        self.verticalLayout.addWidget(self.wg_createOption)
        self.line = QtWidgets.QFrame(dgRandom)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.buttonBox = QtWidgets.QDialogButtonBox(dgRandom)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dgRandom)
        self.buttonBox.accepted.connect(dgRandom.accept) # type: ignore
        self.buttonBox.rejected.connect(dgRandom.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dgRandom)

    def retranslateUi(self, dgRandom):
        _translate = QtCore.QCoreApplication.translate
        dgRandom.setWindowTitle(_translate("dgRandom", "Random"))
        self.lb_maximumWeight.setText(_translate("dgRandom", "Maximum weight:"))
        self.lb_maximumPrice.setText(_translate("dgRandom", "Maximum price:"))
        self.lb_count.setText(_translate("dgRandom", "Count:"))
        self.cb_weightOnly.setText(_translate("dgRandom", "Only random weights"))
        self.cb_clearExisted.setText(_translate("dgRandom", "Clear existed inputs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dgRandom = QtWidgets.QDialog()
    ui = Ui_dgRandom()
    ui.setupUi(dgRandom)
    dgRandom.show()
    sys.exit(app.exec_())
