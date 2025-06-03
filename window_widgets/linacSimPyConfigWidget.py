# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: views\simacConfigWidget.pyc
# Compiled at: 2016-09-20 08:28:14
from PyQt5 import QtCore, QtGui, QtWidgets
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)


except AttributeError:

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_Dialog_configFile(object):

    def setupUi(self, Dialog_configFile):
        Dialog_configFile.setObjectName(_fromUtf8('Dialog_configFile'))
        Dialog_configFile.resize(432, 250)
        Dialog_configFile.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_configFile)
        self.gridLayout.setObjectName(_fromUtf8('gridLayout'))
        self.label = QtWidgets.QLabel(Dialog_configFile)
        self.label.setObjectName(_fromUtf8('label'))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit_ExerciseName = QtWidgets.QLineEdit(Dialog_configFile)
        self.lineEdit_ExerciseName.setObjectName(_fromUtf8('lineEdit_ExerciseName'))
        self.gridLayout.addWidget(self.lineEdit_ExerciseName, 0, 1, 1, 1)
        self.pushButton_Save = QtWidgets.QPushButton(Dialog_configFile)
        self.pushButton_Save.setObjectName(_fromUtf8('pushButton_Save'))
        self.gridLayout.addWidget(self.pushButton_Save, 0, 2, 1, 1)
        self.pushButton_Cancel = QtWidgets.QPushButton(Dialog_configFile)
        self.pushButton_Cancel.setObjectName(_fromUtf8('pushButton_Cancel'))
        self.gridLayout.addWidget(self.pushButton_Cancel, 2, 2, 1, 1)
        self.doubleSpinBox_Rad_Av_SMag = QtWidgets.QDoubleSpinBox(Dialog_configFile)
        self.doubleSpinBox_Rad_Av_SMag.setMinimum(-0.1)
        self.doubleSpinBox_Rad_Av_SMag.setMaximum(0.1)
        self.doubleSpinBox_Rad_Av_SMag.setSingleStep(0.01)
        self.doubleSpinBox_Rad_Av_SMag.setObjectName(_fromUtf8('doubleSpinBox_Rad_Av_SMag'))
        self.gridLayout.addWidget(self.doubleSpinBox_Rad_Av_SMag, 2, 1, 1, 1)
        self.doubleSpinBox_Trans_Av_SMag = QtWidgets.QDoubleSpinBox(Dialog_configFile)
        self.doubleSpinBox_Trans_Av_SMag.setMinimum(-0.1)
        self.doubleSpinBox_Trans_Av_SMag.setMaximum(0.1)
        self.doubleSpinBox_Trans_Av_SMag.setSingleStep(0.01)
        self.doubleSpinBox_Trans_Av_SMag.setObjectName(_fromUtf8('doubleSpinBox_Trans_Av_SMag'))
        self.gridLayout.addWidget(self.doubleSpinBox_Trans_Av_SMag, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog_configFile)
        self.label_4.setObjectName(_fromUtf8('label_4'))
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.doubleSpinBox_dRad_Av_SMag = QtWidgets.QDoubleSpinBox(Dialog_configFile)
        self.doubleSpinBox_dRad_Av_SMag.setDecimals(4)
        self.doubleSpinBox_dRad_Av_SMag.setMinimum(-0.01)
        self.doubleSpinBox_dRad_Av_SMag.setMaximum(0.01)
        self.doubleSpinBox_dRad_Av_SMag.setSingleStep(0.001)
        self.doubleSpinBox_dRad_Av_SMag.setObjectName(_fromUtf8('doubleSpinBox_dRad_Av_SMag'))
        self.gridLayout.addWidget(self.doubleSpinBox_dRad_Av_SMag, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog_configFile)
        self.label_5.setObjectName(_fromUtf8('label_5'))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.doubleSpinBox_dTrans_Av_SMag = QtWidgets.QDoubleSpinBox(Dialog_configFile)
        self.doubleSpinBox_dTrans_Av_SMag.setDecimals(4)
        self.doubleSpinBox_dTrans_Av_SMag.setMinimum(-0.01)
        self.doubleSpinBox_dTrans_Av_SMag.setMaximum(0.01)
        self.doubleSpinBox_dTrans_Av_SMag.setSingleStep(0.0001)
        self.doubleSpinBox_dTrans_Av_SMag.setObjectName(_fromUtf8('doubleSpinBox_dTrans_Av_SMag'))
        self.gridLayout.addWidget(self.doubleSpinBox_dTrans_Av_SMag, 8, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog_configFile)
        self.label_3.setObjectName(_fromUtf8('label_3'))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog_configFile)
        self.label_2.setObjectName(_fromUtf8('label_2'))
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.retranslateUi(Dialog_configFile)
        QtCore.QMetaObject.connectSlotsByName(Dialog_configFile)

    def retranslateUi(self, Dialog_configFile):
        Dialog_configFile.setWindowTitle(_translate('Dialog_configFile', 'Create Exercise File', None))
        self.label.setText(_translate('Dialog_configFile', 'Rad_Av_SMag:', None))
        self.pushButton_Save.setText(_translate('Dialog_configFile', 'Save', None))
        self.pushButton_Cancel.setText(_translate('Dialog_configFile', 'Cancel', None))
        self.label_4.setText(_translate('Dialog_configFile', 'dTrans_Av_SMag:', None))
        self.label_5.setText(_translate('Dialog_configFile', 'Exercise Name:', None))
        self.label_3.setText(_translate('Dialog_configFile', 'Trans_Av_SMag:', None))
        self.label_2.setText(_translate('Dialog_configFile', 'dRad_Av_SMag:', None))
        return
# okay decompiling simacConfigWidget.pyc
