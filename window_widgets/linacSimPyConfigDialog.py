# probably unused because config dialog doesn't work

#import sys, os, random
#from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QFileDialog #was*
#from PyQt5.QtCore import *
import pickle
from window_widgets import linacSimPyConfigWidget #, linacSimPyDoubleValidator unused
#from array import array

class linacSimPyConfigDialog(QDialog, linacSimPyConfigWidget.Ui_Dialog_configFile):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton_Save.clicked.connect(self.saveData)
        self.pushButton_Cancel.clicked.connect(self.cancelData)
        self.exerciseParams = []

    def saveData(self):
        Rad_Av_SMag = self.doubleSpinBox_Rad_Av_SMag.value()
        Trans_Av_SMag = self.doubleSpinBox_Trans_Av_SMag.value()
        dRad_Av_SMag = self.doubleSpinBox_dRad_Av_SMag.value()
        dTrans_Av_SMag = self.doubleSpinBox_dTrans_Av_SMag.value()
        self.exerciseParams = []
        self.exerciseParams.append(self.lineEdit_ExerciseName.text())
        self.exerciseParams.append(Rad_Av_SMag)
        self.exerciseParams.append(Trans_Av_SMag)
        self.exerciseParams.append(dRad_Av_SMag)
        self.exerciseParams.append(dTrans_Av_SMag)
        fname, _filter = QFileDialog.getSaveFileName(self, 'Create exercise', '.')
        if fname:
            with open(fname, 'wb') as (f):
                pickle.dump(self.exerciseParams, f, protocol=pickle.HIGHEST_PROTOCOL)
        self.close()

    def cancelData(self):
        self.close()

