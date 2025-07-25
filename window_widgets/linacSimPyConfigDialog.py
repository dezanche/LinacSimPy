# LinacSimPy is an interactive model of a medical linear accelerator (LINAC)

# © 2025 Alberta Health Services, Medical Physics

# This file is part of LinacSimPy.
# LinacSimPy is free software: you can redistribute it and/or modify it under the terms 
# of the GNU General Public License as published by the Free Software Foundation, either 
# version 3 of the License, or (at your option) any later version.
# LinacSimPy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with LinacSimPy. 
# If not, see <https://www.gnu.org/licenses/>.

# This material is intended for general information only and is provided on an "as is", "where is" 
# basis. Although reasonable efforts were made to confirm the accuracy of the information, 
# Alberta Health Services does not make any representation or warranty, express, implied or 
# statutory, as to the accuracy, reliability, completeness, applicability or fitness for a particular 
# purpose of such information. This material is not a substitute for the advice of a qualified health 
# professional. Alberta Health Services expressly disclaims all liability for the use of these 
# materials, and for any claims, actions, demands or suits arising from such use.



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

