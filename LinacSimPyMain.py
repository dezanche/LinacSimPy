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


# ND changes
# changed from PyQt4 to PyQt5 (also in matplotlib.backends and in other files)
# changed "views" folder to "window_widgets" to avoid confusion with python views module
# added startup splash screen showing license logo

import csv, json, sys, pickle, webbrowser #math, os, random

# removed some unused imports
from PyQt5 import QtWidgets #QtGui, 
from PyQt5.QtCore import Qt  #QObject, 
from PyQt5.QtWidgets import QMainWindow, QApplication, QSplashScreen, QShortcut, QMessageBox, QFileDialog #was *
from PyQt5.QtGui import QKeySequence, QDoubleValidator, QPixmap #*
#import numpy as np, numpy.matlib
#from scipy import interpolate
#from scipy import special
#from array import array
#import matplotlib, matplotlib.pyplot as plt
#from matplotlib import rcParams
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
#from matplotlib.figure import Figure
from window_widgets import linacSimPyMainWidget
from window_widgets import linacSimPyKlystronForm
from window_widgets import linacSimPyAcceleratorForm
from window_widgets import linacSimPyTreatmentHeadForm
from window_widgets import linacSimPyConfigDialog

from controllers import linacSimPyController
from models import LinacModel

class linacSimPyMainForm(QMainWindow, linacSimPyMainWidget.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.formKlystron = linacSimPyKlystronForm.linacSimPyKlystronForm()
        self.formAccelerator = linacSimPyAcceleratorForm.linacSimPyAcceleratorForm()
        self.formTreatmentHead = linacSimPyTreatmentHeadForm.linacSimPyTreatmentHeadForm()
        self.formKlystron.show()
        self.formKlystron.hide()
        self.dialogConfigFile = linacSimPyConfigDialog.linacSimPyConfigDialog()
        self.linacSimPyLinacModel = LinacModel.LinacModel()
        self.linacSimPyController = linacSimPyController.linacSimPyController()
        self.linacSimPyController.setLinacModel(self.linacSimPyLinacModel)
        self.linacSimPyController.setMainView(self)
        self.formKlystron.setController(self.linacSimPyController)
        self.linacSimPyController.setKlystronView(self.formKlystron)
        self.formAccelerator.setController(self.linacSimPyController)
        self.linacSimPyController.setAcceleratorView(self.formAccelerator)
        self.formTreatmentHead.setController(self.linacSimPyController)
        self.linacSimPyController.setTreatmentHeadView(self.formTreatmentHead)
        self.formKlystron.updateCalculation()
        self.formAccelerator.updateCalculation()
        self.pushButton_Klystron.clicked.connect(self.showKlystronWidget)
        self.pushButton_Accelerator.clicked.connect(self.showAcceleratorWidget)
        self.pushButton_TreatmentHead.clicked.connect(self.showTreatmentHeadWidget)
        self.pushButton_BeamOn.toggled.connect(self.updateLinacModel_BeamOn)
        # easier way to add shortcut:
        self.pushButton_BeamOn.setShortcut("Ctrl+B")
        self.comboBox_Energy.currentIndexChanged.connect(self.updateLinacModel_Energy)
        self.pushButton_UpdateLinacModel.clicked.connect(self.updateLinacModel)
# updated keyboard shortcut
        # old Qt4 signaling updated like https://www.w3resource.com/python-exercises/pyqt/python-pyqt-connecting-signals-to-slots-exercise-15.php
        #QObject.connect(QShortcut(QKeySequence(Qt.CTRL + Qt.Key_C), self), SIGNAL('activated()'), self.updateLinacModel)
        # next 3 lines are updated version of one above
        shortcut = QKeySequence(Qt.CTRL + Qt.Key_C)
        self.shortcut = QShortcut(shortcut, self)
        self.shortcut.activated.connect(self.updateLinacModel)
# new keyboard shortcuts
        shortcut = QKeySequence(Qt.CTRL + Qt.Key_K)
        self.shortcut = QShortcut(shortcut, self)
        self.shortcut.activated.connect(self.showKlystronWidget)
        shortcut = QKeySequence(Qt.CTRL + Qt.Key_A)
        self.shortcut = QShortcut(shortcut, self)
        self.shortcut.activated.connect(self.showAcceleratorWidget)
        shortcut = QKeySequence(Qt.CTRL + Qt.Key_T)
        self.shortcut = QShortcut(shortcut, self)
        self.shortcut.activated.connect(self.showTreatmentHeadWidget)
        shortcut = QKeySequence(Qt.CTRL + Qt.Key_Q)
        self.shortcut = QShortcut(shortcut, self)
        self.shortcut.activated.connect(self.close)
# input scrollbars
        self.horizontalScrollBar_Omega.valueChanged.connect(self.updateLinacModel_Omega)
        self.horizontalScrollBar_P_AC_Kly.valueChanged.connect(self.updateLinacModel_P_AC_Kly)
        self.horizontalScrollBar_v_Kly.valueChanged.connect(self.updateLinacModel_v_Kly)
        self.horizontalScrollBar_Tau.valueChanged.connect(self.updateLinacModel_Tau)
        self.horizontalScrollBar_v_Gun.valueChanged.connect(self.updateLinacModel_v_Gun)
        self.horizontalScrollBar_v_Grid.valueChanged.connect(self.updateLinacModel_v_Grid)
        self.horizontalScrollBar_i_Coil_BMag.valueChanged.connect(self.updateLinacModel_i_Coil_BMag)
        self.horizontalScrollBar_i_Pos_Rad.valueChanged.connect(self.updateLinacModel_i_Pos_Rad)
        self.horizontalScrollBar_i_Pos_Trans.valueChanged.connect(self.updateLinacModel_i_Pos_Trans)
        self.horizontalScrollBar_i_Ang_Rad.valueChanged.connect(self.updateLinacModel_i_Ang_Rad)
        self.horizontalScrollBar_i_Ang_Trans.valueChanged.connect(self.updateLinacModel_i_Ang_Trans)
        self.horizontalScrollBar_Rad_Jaw.valueChanged.connect(self.updateLinacModel_Rad_Jaw)
        self.horizontalScrollBar_Trans_Jaw.valueChanged.connect(self.updateLinacModel_Trans_Jaw)
        self.horizontalScrollBar_d_Tank.valueChanged.connect(self.updateLinacModel_d_Tank)
        self.lineEdit_Omega.textEdited.connect(self.updateLinacModel_Omega_2)
        self.lineEdit_Omega.returnPressed.connect(self.updateLinacModel_Omega_3)
        self.lineEdit_Omega.setValidator(QDoubleValidator(2855.5, 2856.5, 2))

        self.lineEdit_P_AC_Kly.textEdited.connect(self.updateLinacModel_P_AC_Kly_2)
        self.lineEdit_P_AC_Kly.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_P_AC_Kly.setValidator(QDoubleValidator(0, 200, 0))

        self.lineEdit_v_Kly.textEdited.connect(self.updateLinacModel_v_Kly_2)
        self.lineEdit_v_Kly.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_v_Kly.setValidator(QDoubleValidator(0, 150, 0))

        self.lineEdit_Tau.textEdited.connect(self.updateLinacModel_Tau_2)
        self.lineEdit_Tau.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_Tau.setValidator(QDoubleValidator(2, 4, 0))

        self.lineEdit_v_Gun.textEdited.connect(self.updateLinacModel_v_Gun_2)
        self.lineEdit_v_Gun.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_v_Gun.setValidator(QDoubleValidator(0, 20, 0))

        self.lineEdit_v_Grid.textEdited.connect(self.updateLinacModel_v_Grid_2)
        self.lineEdit_v_Grid.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_v_Grid.setValidator(QDoubleValidator(-200, 0, 0))

        self.lineEdit_i_Coil_BMag.textEdited.connect(self.updateLinacModel_i_Coil_BMag_2)
        self.lineEdit_i_Coil_BMag.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_i_Coil_BMag.setValidator(QDoubleValidator(0, 200, 0))

        self.lineEdit_i_Pos_Rad.textEdited.connect(self.updateLinacModel_i_Pos_Rad_2)
        self.lineEdit_i_Pos_Rad.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_i_Pos_Rad.setValidator(QDoubleValidator(-200, 200, 0))

        self.lineEdit_i_Pos_Trans.textEdited.connect(self.updateLinacModel_i_Pos_Trans_2)
        self.lineEdit_i_Pos_Trans.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_i_Pos_Trans.setValidator(QDoubleValidator(200, 200, 0))

        self.lineEdit_i_Ang_Rad.textEdited.connect(self.updateLinacModel_i_Ang_Rad_2)
        self.lineEdit_i_Ang_Rad.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_i_Ang_Rad.setValidator(QDoubleValidator(-200, 200, 0))

        self.lineEdit_i_Ang_Trans.textEdited.connect(self.updateLinacModel_i_Ang_Trans_2)
        self.lineEdit_i_Ang_Trans.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_i_Ang_Trans.setValidator(QDoubleValidator(-200, 200, 0))

        self.lineEdit_Rad_Jaw.textEdited.connect(self.updateLinacModel_Rad_Jaw_2)
        self.lineEdit_Rad_Jaw.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_Rad_Jaw.setValidator(QDoubleValidator(3, 20, 0))

        self.lineEdit_Trans_Jaw.textEdited.connect(self.updateLinacModel_Trans_Jaw_2)
        self.lineEdit_Trans_Jaw.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_Trans_Jaw.setValidator(QDoubleValidator(3, 20, 0))

        self.lineEdit_d_Tank.textEdited.connect(self.updateLinacModel_d_Tank_2)
        self.lineEdit_d_Tank.returnPressed.connect(self.updateLinacModel)
        self.lineEdit_d_Tank.setValidator(QDoubleValidator(0, 30, 0))

        self.actionLoad_ini.triggered.connect(self.showLoad_ini)
        self.actionSave_ini.triggered.connect(self.showSave_ini)
        self.actionLoad_Exercise.triggered.connect(self.showLoad_Exercise)
        self.actionValidate_Exercise.triggered.connect(self.showValidate_Exercise)
        self.actionSave_Exercise.triggered.connect(self.showSave_Exercise)
        self.actionConvert_log_file.triggered.connect(self.showConvert_log_file)
        self.actionCreate_config_file.triggered.connect(self.showCreate_config_file)
        #added
        self.actionExit.triggered.connect(self.close)
        self.actionAbout_LinacSimPy.triggered.connect(self.showAboutLinacSimPy)
        self.actionLicense.triggered.connect(self.showLicense)
        self.actionTutorial.triggered.connect(self.showTutorial)
        self.actionTheory.triggered.connect(self.showTheory)
        self.strFormatter = '{0:.2f}'
        self.parameterLog = []

    def closeEvent(self, event):
        # Ask for confirmation before closing
        confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to close LinacSimPy?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.formKlystron.close()
            self.formAccelerator.close()
            self.formTreatmentHead.close()
            event.accept()  # Close
        else:
            event.ignore()  # Don't close

    def showLoad_ini(self):
        fname, _filter = QFileDialog.getOpenFileName(self, 'Load Linac status (.json)', '.', "(*.json)")
        if fname:
            with open(fname, 'r') as (f):
                initData = json.load(f)
            self.pushButton_BeamOn.setChecked(True)
            self.comboBox_PRF.setEnabled(True)
            self.comboBox_Energy.setEnabled(True)
            self.horizontalScrollBar_Omega.setEnabled(True)
            self.horizontalScrollBar_P_AC_Kly.setEnabled(True)
            self.horizontalScrollBar_v_Kly.setEnabled(True)
            self.horizontalScrollBar_Tau.setEnabled(True)
            self.horizontalScrollBar_v_Gun.setEnabled(True)
            self.horizontalScrollBar_i_Coil_BMag.setEnabled(True)
            self.horizontalScrollBar_i_Pos_Rad.setEnabled(True)
            self.horizontalScrollBar_i_Pos_Trans.setEnabled(True)
            self.horizontalScrollBar_i_Ang_Rad.setEnabled(True)
            self.horizontalScrollBar_i_Ang_Trans.setEnabled(True)
            self.horizontalScrollBar_Rad_Jaw.setEnabled(True)
            self.horizontalScrollBar_Trans_Jaw.setEnabled(True)
            self.horizontalScrollBar_d_Tank.setEnabled(True)
            energyCurrentIndex = 0
            if initData['Energy'] == 0:
                energyCurrentIndex = 0
            elif initData['Energy'] == 6:
                energyCurrentIndex = 1
            elif initData['Energy'] == 15:
                energyCurrentIndex = 2
            else:
                energyCurrentIndex = 0
            self.comboBox_Energy.setCurrentIndex(energyCurrentIndex)
            PRFCurrentIndex = 0
            if initData['PRF'] == 60:
                PRFCurrentIndex = 0
            elif initData['PRF'] == 120:
                PRFCurrentIndex = 1
            elif initData['PRF'] == 180:
                PRFCurrentIndex = 2
            elif initData['PRF'] == 240:
                PRFCurrentIndex = 3
            elif initData['PRF'] == 300:
                PRFCurrentIndex = 4
            elif initData['PRF'] == 360:
                PRFCurrentIndex = 5
            else:
                PRFCurrentIndex = 0
            self.comboBox_PRF.setCurrentIndex(PRFCurrentIndex)
            self.lineEdit_Omega.setText(self.strFormatter.format(initData['Omega']))
            self.lineEdit_P_AC_Kly.setText(self.strFormatter.format(initData['P_AC_Kly']))
            self.lineEdit_v_Kly.setText(self.strFormatter.format(initData['v_Kly']))
            self.lineEdit_Tau.setText(self.strFormatter.format(initData['Tau']))
            self.lineEdit_v_Gun.setText(self.strFormatter.format(initData['v_Gun']))
            self.lineEdit_v_Grid.setText(self.strFormatter.format(initData['v_Grid']))
            self.lineEdit_i_Coil_BMag.setText(self.strFormatter.format(initData['i_Coil_BMag']))
            self.lineEdit_i_Pos_Rad.setText(self.strFormatter.format(initData['i_Pos_Rad']))
            self.lineEdit_i_Pos_Trans.setText(self.strFormatter.format(initData['i_Pos_Trans']))
            self.lineEdit_i_Ang_Rad.setText(self.strFormatter.format(initData['i_Ang_Rad']))
            self.lineEdit_i_Ang_Trans.setText(self.strFormatter.format(initData['i_Ang_Trans']))
            self.lineEdit_Rad_Jaw.setText(self.strFormatter.format(initData['Rad_Jaw']))
            self.lineEdit_Trans_Jaw.setText(self.strFormatter.format(initData['Trans_Jaw']))
            self.lineEdit_d_Tank.setText(self.strFormatter.format(initData['d_Tank']))
            self.lineEdit_dD_Ion.setText(self.strFormatter.format(initData['dD_Ion']))
            self.setWindowTitle('LinacSimPy - ' + fname)

    def showSave_ini(self):
        if self.parameterLog.__len__() <= 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('No parameter set so far!')
            msg.setWindowTitle('LinacSimPy')
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            return
        paramSetting = self.parameterLog[-1]
        initData = {'Energy': paramSetting.Energy, 'PRF': paramSetting.PRF, 
           'P_AC_Kly': paramSetting.P_AC_Kly, 
           'Omega': paramSetting.Omega, 
           'v_Kly': paramSetting.v_Kly, 
           'Tau': paramSetting.Tau, 
           'v_Gun': paramSetting.v_Gun, 
           'v_Grid': paramSetting.v_Grid, 
           'i_Coil_BMag': paramSetting.i_Coil_BMag, 
           'i_Pos_Rad': paramSetting.i_Pos_Rad, 
           'i_Pos_Trans': paramSetting.i_Pos_Trans, 
           'i_Ang_Rad': paramSetting.i_Ang_Rad, 
           'Rad_Jaw': paramSetting.Rad_Jaw, 
           'i_Ang_Trans': paramSetting.i_Ang_Trans, 
           'Trans_Jaw': paramSetting.Trans_Jaw, 
           'd_Tank': paramSetting.d_Tank, 
           'dD_Ion': paramSetting.dD_Ion}
        fname, _filter = QFileDialog.getSaveFileName(self, 'Save Linac status (.json)', '.', "(*.json)")
        if fname:
            with open(fname, 'w') as (f):
                json.dump(initData, f)

    def showLoad_Exercise(self):
        fname, _filter = QFileDialog.getOpenFileName(self, 'Load exercise', '.')
        if fname:
            try: # TO DO: catch empty file name + missing exercise name below?
                with open(fname, 'r') as (f):
                    exerciseParams = pickle.load(f)
                    self.linacSimPyLinacModel.ExerciseName = exerciseParams[0]
                    self.linacSimPyLinacModel.Rad_Av_SMag = exerciseParams[1]
                    self.linacSimPyLinacModel.Trans_Av_SMag = exerciseParams[2]
                    self.linacSimPyLinacModel.dRad_Av_SMag = exerciseParams[3]
                    self.linacSimPyLinacModel.dTrans_Av_SMag = exerciseParams[4]
            except Exception as error:
                pass

    def showValidate_Exercise(self):
        if self.linacSimPyLinacModel.ExerciseName:# throws AttributeError: 'LinacModel' object has no attribute 'ExerciseName'
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(self.linacSimPyLinacModel.ExerciseName)
            msg.setWindowTitle('Current Exercise')
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            return

    def showSave_Exercise(self):
        if self.parameterLog.__len__() <= 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('No parameter set so far!')
            msg.setWindowTitle('LinacSimPy')
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            return
        fname, _filter = QFileDialog.getSaveFileName(self, 'Save exercise (binary)', '.')
        if fname:
            with open(fname, 'wb') as (f):
                pickle.dump(self.parameterLog, f, protocol=pickle.HIGHEST_PROTOCOL)

    def showConvert_log_file(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter Admin Password:')
        if text != 'starbucks':
            return
        fname, _filter = QFileDialog.getOpenFileName(self, 'Load binary exercise file', '.')
        paramList = []
        if fname:
            with open(fname, 'rb') as (f):
                paramList = pickle.load(f)
        else:
            return
        fname2, _filter = QFileDialog.getSaveFileName(self, 'Save exercise as csv', '.', "(*.csv)")
        if fname2:
            with open(fname2, 'w') as (f):
                writer = csv.writer(f)
                writer.writerow(['PRF', 'Tau', 'Energy', 'Omega', 'P_AC_Kly', 'v_Kly', 'v_Gun', 
                 'i_Coil_BMag', 'v_Grid', 
                 'i_Pos_Rad', 
                 'i_Pos_Trans', 'i_Ang_Rad', 'i_Ang_Trans', 
                 'Rad_Jaw', 'Trans_Jaw', 
                 'd_Tank', 
                 'dD_Ion'])
                for param in paramList:
                    writer.writerow([ # next line was throwing AttributeError: 'str' object has no attribute 'PRF'
                     param.PRF, param.Tau, param.Energy, param.Omega, param.P_AC_Kly, param.v_Kly, param.v_Gun,
                     param.i_Coil_BMag, param.v_Grid,
                     param.i_Pos_Rad, param.i_Pos_Trans, param.i_Ang_Rad, param.i_Ang_Trans, param.Rad_Jaw,
                     param.Trans_Jaw, param.d_Tank, param.dD_Ion])

        else:
            return

# this option doesn't show up in menu
    def showCreate_config_file(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter Admin Password:')
        if text != 'starbucks':
            return
        ret = self.dialogConfigFile.exec_()

    def showAboutLinacSimPy(self):
        file = open('./About_LinacSimPy.txt', 'r')
        msg = QMessageBox()
        msg.setTextFormat(Qt.RichText)      # displays hyperlinks but not actually functional; have to embed a QLabel or QTextBrowser within the QMessageBox
        #msg.setOpenExternalLinks(True)
        msg.setIcon(QMessageBox.Information)
        msg.setText(file.read())
        msg.setWindowTitle('About LinacSimPy')
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def showLicense(self):      # updated
        url = 'https://www.gnu.org/licenses/gpl-3.0.html'
        webbrowser.open(url, new=1)

    def showTutorial(self):
        url = 'https://www.youtube.com/watch?v=l84XlGtHGhk'
        webbrowser.open(url, new=1)

    def showTheory(self):
        url = 'https://doi.org/10.1120/jacmp.v16i3.5139'
        webbrowser.open(url, new=1)

    def showKlystronWidget(self):
        self.formKlystron.updateView()
        self.formKlystron.show()
        self.formKlystron.raise_()
        self.formKlystron.activateWindow()

    def showAcceleratorWidget(self):
        self.formAccelerator.updateView()
        self.formAccelerator.raise_()
        self.formAccelerator.show()

    def showTreatmentHeadWidget(self):
        self.formTreatmentHead.updateView()
        self.formTreatmentHead.raise_()
        self.formTreatmentHead.show()

    def updateView(self):
        linacModel = self.linacSimPyController.getLinacModel()
        self.lineEdit_S_Ion_R.setText(self.strFormatter.format(linacModel.S_Ion_R))
        self.lineEdit_S_Ion_T.setText(self.strFormatter.format(linacModel.S_Ion_T))
        self.lineEdit_Flatness_R.setText(self.strFormatter.format(linacModel.Flatness_R))
        self.lineEdit_Flatness_T.setText(self.strFormatter.format(linacModel.Flatness_T))
        self.lineEdit_dD_Ion.setText(self.strFormatter.format(linacModel.dD_Ion))
        self.lineEdit_Omega.setText(self.strFormatter.format(linacModel.Omega))
        self.lineEdit_P_AC_Kly.setText(self.strFormatter.format(linacModel.P_AC_Kly))
        self.lineEdit_v_Kly.setText(self.strFormatter.format(linacModel.v_Kly))
        self.lineEdit_Tau.setText(self.strFormatter.format(linacModel.Tau))
        self.lineEdit_v_Gun.setText(self.strFormatter.format(linacModel.v_Gun))
        self.lineEdit_v_Grid.setText(self.strFormatter.format(linacModel.v_Grid))
        self.lineEdit_i_Coil_BMag.setText(self.strFormatter.format(linacModel.i_Coil_BMag))
        self.lineEdit_i_Pos_Rad.setText(self.strFormatter.format(linacModel.i_Pos_Rad))
        self.lineEdit_i_Pos_Trans.setText(self.strFormatter.format(linacModel.i_Pos_Trans))
        self.lineEdit_i_Ang_Rad.setText(self.strFormatter.format(linacModel.i_Ang_Rad))
        self.lineEdit_i_Ang_Trans.setText(self.strFormatter.format(linacModel.i_Ang_Trans))
        self.lineEdit_Rad_Jaw.setText(self.strFormatter.format(linacModel.Rad_Jaw))
        self.lineEdit_Trans_Jaw.setText(self.strFormatter.format(linacModel.Trans_Jaw))
        self.lineEdit_d_Tank.setText(self.strFormatter.format(linacModel.d_Tank))
        self.lineEdit_i_Acc.setText(self.strFormatter.format(float(linacModel.i_Acc)))
        self.lineEdit_i_Tar.setText(self.strFormatter.format(linacModel.i_Tar))
        self.lineEdit_P_Acc.setText(self.strFormatter.format(linacModel.P_Acc))
        self.lineEdit_P_Kly_Refl.setText(self.strFormatter.format(linacModel.P_Kly_Refl))
        self.horizontalScrollBar_Omega.valueChanged.disconnect(self.updateLinacModel_Omega)
        self.horizontalScrollBar_P_AC_Kly.valueChanged.disconnect(self.updateLinacModel_P_AC_Kly)
        self.horizontalScrollBar_v_Kly.valueChanged.disconnect(self.updateLinacModel_v_Kly)
        self.horizontalScrollBar_Tau.valueChanged.disconnect(self.updateLinacModel_Tau)
        self.horizontalScrollBar_v_Gun.valueChanged.disconnect(self.updateLinacModel_v_Gun)
        self.horizontalScrollBar_v_Grid.valueChanged.disconnect(self.updateLinacModel_v_Grid)
        self.horizontalScrollBar_i_Coil_BMag.valueChanged.disconnect(self.updateLinacModel_i_Coil_BMag)
        self.horizontalScrollBar_i_Pos_Rad.valueChanged.disconnect(self.updateLinacModel_i_Pos_Rad)
        self.horizontalScrollBar_i_Pos_Trans.valueChanged.disconnect(self.updateLinacModel_i_Pos_Trans)
        self.horizontalScrollBar_i_Ang_Rad.valueChanged.disconnect(self.updateLinacModel_i_Ang_Rad)
        self.horizontalScrollBar_i_Ang_Trans.valueChanged.disconnect(self.updateLinacModel_i_Ang_Trans)
        self.horizontalScrollBar_Rad_Jaw.valueChanged.disconnect(self.updateLinacModel_Rad_Jaw)
        self.horizontalScrollBar_Trans_Jaw.valueChanged.disconnect(self.updateLinacModel_Trans_Jaw)
        self.horizontalScrollBar_d_Tank.valueChanged.disconnect(self.updateLinacModel_d_Tank)
        # added int() to fix "TypeError: setValue(self, int): argument 1 has unexpected type 'float'"
        self.horizontalScrollBar_Omega.setValue(int(self.linacSimPyLinacModel.Omega * 100))
        self.horizontalScrollBar_P_AC_Kly.setValue(int(self.linacSimPyLinacModel.P_AC_Kly))
        self.horizontalScrollBar_v_Kly.setValue(int(self.linacSimPyLinacModel.v_Kly))
        self.horizontalScrollBar_Tau.setValue(int(self.linacSimPyLinacModel.Tau * 10))
        self.horizontalScrollBar_v_Gun.setValue(int(self.linacSimPyLinacModel.v_Gun))
        self.horizontalScrollBar_v_Grid.setValue(int(self.linacSimPyLinacModel.v_Grid))
        self.horizontalScrollBar_i_Coil_BMag.setValue(int(self.linacSimPyLinacModel.i_Coil_BMag))
        self.horizontalScrollBar_i_Pos_Rad.setValue(int(self.linacSimPyLinacModel.i_Pos_Rad))
        self.horizontalScrollBar_i_Pos_Trans.setValue(int(self.linacSimPyLinacModel.i_Pos_Trans))
        self.horizontalScrollBar_i_Ang_Rad.setValue(int(self.linacSimPyLinacModel.i_Ang_Rad))
        self.horizontalScrollBar_i_Ang_Trans.setValue(int(self.linacSimPyLinacModel.i_Ang_Trans))
        self.horizontalScrollBar_Rad_Jaw.setValue(int(self.linacSimPyLinacModel.Rad_Jaw))
        self.horizontalScrollBar_Trans_Jaw.setValue(int(self.linacSimPyLinacModel.Trans_Jaw))
        self.horizontalScrollBar_d_Tank.setValue(int(self.linacSimPyLinacModel.d_Tank))
        self.horizontalScrollBar_Omega.valueChanged.connect(self.updateLinacModel_Omega)
        self.horizontalScrollBar_P_AC_Kly.valueChanged.connect(self.updateLinacModel_P_AC_Kly)
        self.horizontalScrollBar_v_Kly.valueChanged.connect(self.updateLinacModel_v_Kly)
        self.horizontalScrollBar_Tau.valueChanged.connect(self.updateLinacModel_Tau)
        self.horizontalScrollBar_v_Gun.valueChanged.connect(self.updateLinacModel_v_Gun)
        self.horizontalScrollBar_v_Grid.valueChanged.connect(self.updateLinacModel_v_Grid)
        self.horizontalScrollBar_i_Coil_BMag.valueChanged.connect(self.updateLinacModel_i_Coil_BMag)
        self.horizontalScrollBar_i_Pos_Rad.valueChanged.connect(self.updateLinacModel_i_Pos_Rad)
        self.horizontalScrollBar_i_Pos_Trans.valueChanged.connect(self.updateLinacModel_i_Pos_Trans)
        self.horizontalScrollBar_i_Ang_Rad.valueChanged.connect(self.updateLinacModel_i_Ang_Rad)
        self.horizontalScrollBar_i_Ang_Trans.valueChanged.connect(self.updateLinacModel_i_Ang_Trans)
        self.horizontalScrollBar_Rad_Jaw.valueChanged.connect(self.updateLinacModel_Rad_Jaw)
        self.horizontalScrollBar_Trans_Jaw.valueChanged.connect(self.updateLinacModel_Trans_Jaw)
        self.horizontalScrollBar_d_Tank.valueChanged.connect(self.updateLinacModel_d_Tank)

    def updateLinacModel_BeamOn(self):
        if self.pushButton_BeamOn.isChecked():
            self.comboBox_PRF.setEnabled(True)
            self.comboBox_Energy.setEnabled(True)
            self.horizontalScrollBar_Omega.setEnabled(True)
            self.horizontalScrollBar_P_AC_Kly.setEnabled(True)
            self.horizontalScrollBar_v_Kly.setEnabled(True)
            self.horizontalScrollBar_Tau.setEnabled(True)
            self.horizontalScrollBar_v_Gun.setEnabled(True)
            # missing v_Grid
            self.horizontalScrollBar_i_Coil_BMag.setEnabled(True)
            self.horizontalScrollBar_i_Pos_Rad.setEnabled(True)
            self.horizontalScrollBar_i_Pos_Trans.setEnabled(True)
            self.horizontalScrollBar_i_Ang_Rad.setEnabled(True)
            self.horizontalScrollBar_i_Ang_Trans.setEnabled(True)
            self.horizontalScrollBar_Rad_Jaw.setEnabled(True)
            self.horizontalScrollBar_Trans_Jaw.setEnabled(True)
            self.horizontalScrollBar_d_Tank.setEnabled(True)
            self.lineEdit_Omega.setEnabled(True)
            self.lineEdit_P_AC_Kly.setEnabled(True)
            self.lineEdit_v_Kly.setEnabled(True)
            self.lineEdit_Tau.setEnabled(True)
            self.lineEdit_v_Gun.setEnabled(True)
            # missing v_Grid
            self.lineEdit_i_Coil_BMag.setEnabled(True)
            self.lineEdit_i_Pos_Rad.setEnabled(True)
            self.lineEdit_i_Pos_Trans.setEnabled(True)
            self.lineEdit_i_Ang_Rad.setEnabled(True)
            self.lineEdit_i_Ang_Trans.setEnabled(True)
            self.lineEdit_Rad_Jaw.setEnabled(True)
            self.lineEdit_Trans_Jaw.setEnabled(True)
            self.lineEdit_d_Tank.setEnabled(True)
        else:
            # Show confirmation dialog (not needed with 3 reset lines below commented out)
            #confirmation = QMessageBox.question(
            #    self, 
            #    "Confirmation", 
            #    "Beam off will set Energy to Idle and reset some values. Are you sure?", 
            #    QMessageBox.Yes | QMessageBox.No
        #)
        
            #if confirmation == QMessageBox.No:
                # If user cancels, re-check the button to prevent deactivation
            #    self.pushButton_BeamOn.setChecked(True)
            #    return  # Stop further execution
            
            # Disable controls
            self.comboBox_PRF.setEnabled(False)
            self.comboBox_Energy.setEnabled(False)
            self.horizontalScrollBar_Omega.setEnabled(False)
            self.horizontalScrollBar_P_AC_Kly.setEnabled(False)
            self.horizontalScrollBar_v_Kly.setEnabled(False)
            self.horizontalScrollBar_Tau.setEnabled(False)
            self.horizontalScrollBar_v_Gun.setEnabled(False)
            self.horizontalScrollBar_v_Grid.setEnabled(False)
            self.horizontalScrollBar_i_Coil_BMag.setEnabled(False)
            self.horizontalScrollBar_i_Pos_Rad.setEnabled(False)
            self.horizontalScrollBar_i_Pos_Trans.setEnabled(False)
            self.horizontalScrollBar_i_Ang_Rad.setEnabled(False)
            self.horizontalScrollBar_i_Ang_Trans.setEnabled(False)
            self.horizontalScrollBar_Rad_Jaw.setEnabled(False)
            self.horizontalScrollBar_Trans_Jaw.setEnabled(False)
            self.horizontalScrollBar_d_Tank.setEnabled(False)
            self.lineEdit_Omega.setEnabled(False)
            self.lineEdit_P_AC_Kly.setEnabled(False)
            self.lineEdit_v_Kly.setEnabled(False)
            self.lineEdit_Tau.setEnabled(False)
            self.lineEdit_v_Gun.setEnabled(False)
            self.lineEdit_v_Grid.setEnabled(False)
            self.lineEdit_i_Coil_BMag.setEnabled(False)
            self.lineEdit_i_Pos_Rad.setEnabled(False)
            self.lineEdit_i_Pos_Trans.setEnabled(False)
            self.lineEdit_i_Ang_Rad.setEnabled(False)
            self.lineEdit_i_Ang_Trans.setEnabled(False)
            self.lineEdit_Rad_Jaw.setEnabled(False)
            self.lineEdit_Trans_Jaw.setEnabled(False)
            self.lineEdit_d_Tank.setEnabled(False)

        # Reset dropdowns and update model
        #self.comboBox_Energy.setCurrentIndex(0)
        #self.comboBox_PRF.setCurrentIndex(0)
        #self.updateLinacModel_Energy()

    def updateLinacModel_Energy(self):
        if self.comboBox_Energy.currentIndex() == 0:
            self.lineEdit_d_Tank.setText('0')
            self.lineEdit_i_Coil_BMag.setText('0')
            self.lineEdit_v_Gun.setText('0')
            self.lineEdit_v_Kly.setText('0')
            self.lineEdit_v_Grid.setText('0')
            self.lineEdit_P_AC_Kly.setText('0')
        elif self.comboBox_Energy.currentIndex() == 1:
            self.lineEdit_d_Tank.setText('1.5')
            self.lineEdit_i_Coil_BMag.setText('65.0')
            self.lineEdit_v_Gun.setText('16.0')
            self.lineEdit_v_Kly.setText('104.0')
            self.lineEdit_v_Grid.setText('0.0')
            self.lineEdit_P_AC_Kly.setText('182.0')
        elif self.comboBox_Energy.currentIndex() == 2:
            self.lineEdit_d_Tank.setText('3.0')
            self.lineEdit_i_Coil_BMag.setText('155.0')
            self.lineEdit_v_Gun.setText('10.0')
            self.lineEdit_v_Kly.setText('125.0')
            self.lineEdit_v_Grid.setText('-10.6')
            self.lineEdit_P_AC_Kly.setText('67.0')

    def updateLinacModel(self):
        if self.comboBox_Energy.currentIndex() == 0: # or ~self.pushButton_BeamOn.isChecked() needed but doesn't work
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('You must set beam ON and pick an energy first!')
            msg.setWindowTitle('LinacSimPy')
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        paramSetting = LinacModel.LinacSimPySetting()
        index = self.comboBox_PRF.currentIndex()
        if index == 0:
            value = 60
        elif index == 1:
            value = 120
        elif index == 2:
            value = 180
        elif index == 3:
            value = 240
        elif index == 4:
            value = 300
        elif index == 5:
            value = 360
        else:
            value = 0
        paramSetting.PRF = value
        paramSetting.Tau = float(self.lineEdit_Tau.text())
        paramSetting.Omega = float(self.lineEdit_Omega.text())
        paramSetting.P_AC_Kly = float(self.lineEdit_P_AC_Kly.text())
        paramSetting.v_Kly = float(self.lineEdit_v_Kly.text())
        paramSetting.v_Gun = float(self.lineEdit_v_Gun.text())
        paramSetting.i_Coil_BMag = float(self.lineEdit_i_Coil_BMag.text())
        paramSetting.v_Grid = float(self.lineEdit_v_Grid.text())
        paramSetting.i_Pos_Rad = float(self.lineEdit_i_Pos_Rad.text())
        paramSetting.i_Pos_Trans = float(self.lineEdit_i_Pos_Trans.text())
        paramSetting.i_Ang_Rad = float(self.lineEdit_i_Ang_Rad.text())
        paramSetting.i_Ang_Trans = float(self.lineEdit_i_Ang_Trans.text())
        paramSetting.Rad_Jaw = float(self.lineEdit_Rad_Jaw.text())
        paramSetting.Trans_Jaw = float(self.lineEdit_Trans_Jaw.text())
        paramSetting.d_Tank = float(self.lineEdit_d_Tank.text())
        paramSetting.dD_Ion = float(self.lineEdit_dD_Ion.text())
        if self.comboBox_Energy.currentIndex() == 0:
            paramSetting.Energy = 0
        elif self.comboBox_Energy.currentIndex() == 1:
            paramSetting.Energy = 6
        elif self.comboBox_Energy.currentIndex() == 2:
            paramSetting.Energy = 15
        else:
            paramSetting.Energy = 0
        if paramSetting.Energy == 0:
            pass
        else:
            self.linacSimPyController.updateLinacModelWithParameters(paramSetting)
        self.parameterLog.append(paramSetting)

    def updateLinacModel_Omega(self):
        self.lineEdit_Omega.setText(str(self.horizontalScrollBar_Omega.value() / 100.0))

    def updateLinacModel_P_AC_Kly(self):
        self.lineEdit_P_AC_Kly.setText(str(self.horizontalScrollBar_P_AC_Kly.value()))

    def updateLinacModel_v_Kly(self):
        self.lineEdit_v_Kly.setText(str(self.horizontalScrollBar_v_Kly.value()))

    def updateLinacModel_Tau(self):
        self.lineEdit_Tau.setText(str(self.horizontalScrollBar_Tau.value() / 10.0))

    def updateLinacModel_v_Gun(self):
        self.lineEdit_v_Gun.setText(str(self.horizontalScrollBar_v_Gun.value()))

    def updateLinacModel_v_Grid(self):
        self.lineEdit_v_Grid.setText(str(self.horizontalScrollBar_v_Grid.value()))

    def updateLinacModel_i_Coil_BMag(self):
        self.lineEdit_i_Coil_BMag.setText(str(self.horizontalScrollBar_i_Coil_BMag.value()))

    def updateLinacModel_i_Pos_Rad(self):
        self.lineEdit_i_Pos_Rad.setText(str(self.horizontalScrollBar_i_Pos_Rad.value()))

    def updateLinacModel_i_Pos_Trans(self):
        self.lineEdit_i_Pos_Trans.setText(str(self.horizontalScrollBar_i_Pos_Trans.value()))

    def updateLinacModel_i_Ang_Rad(self):
        self.lineEdit_i_Ang_Rad.setText(str(self.horizontalScrollBar_i_Ang_Rad.value()))

    def updateLinacModel_i_Ang_Trans(self):
        self.lineEdit_i_Ang_Trans.setText(str(self.horizontalScrollBar_i_Ang_Trans.value()))

    def updateLinacModel_Rad_Jaw(self):
        self.lineEdit_Rad_Jaw.setText(str(self.horizontalScrollBar_Rad_Jaw.value()))

    def updateLinacModel_Trans_Jaw(self):
        if self.lineEdit_Trans_Jaw.text() != str(self.horizontalScrollBar_Trans_Jaw.value()):
            self.lineEdit_Trans_Jaw.setText(str(self.horizontalScrollBar_Trans_Jaw.value()))

    def updateLinacModel_d_Tank(self):
        self.lineEdit_d_Tank.setText(str(self.horizontalScrollBar_d_Tank.value()))

    def updateLinacModel_Omega_2(self):
        value = float(self.lineEdit_Omega.text())
        if value >= 2855.5 and value <= 2856.5:
            self.horizontalScrollBar_Omega.setValue(float(self.lineEdit_Omega.text()) * 100)

    def updateLinacModel_Omega_3(self):
        value = float(self.lineEdit_Omega.text())
        if value >= 2855.5 and value <= 2856.5:
            self.updateLinacModel()
        else:
            self.lineEdit_Omega.setText(2856.0)
            self.horizontalScrollBar_Omega.setValue(float(self.lineEdit_Omega.text()) * 100)

    def updateLinacModel_P_AC_Kly_2(self):
        self.horizontalScrollBar_P_AC_Kly.setValue(float(self.lineEdit_P_AC_Kly.text()))

    def updateLinacModel_v_Kly_2(self):
        self.horizontalScrollBar_v_Kly.setValue(float(self.lineEdit_v_Kly.text()))

    def updateLinacModel_Tau_2(self):
        # looks wrong
        self.horizontalScrollBar_v_Gun.setValue(float(self.lineEdit_Tau.text()) * 10)

    def updateLinacModel_v_Gun_2(self):
        # looks wrong
        self.horizontalScrollBar_v_Grid.setValue(float(self.lineEdit_v_Gun.text()))

    def updateLinacModel_v_Grid_2(self):
        # looks wrong
        self.horizontalScrollBar_i_Coil_BMag.setValue(float(self.lineEdit_v_Grid.text()))

    def updateLinacModel_i_Coil_BMag_2(self):
        self.horizontalScrollBar_i_Coil_BMag.setValue(float(self.lineEdit_i_Coil_BMag.text()))

    def updateLinacModel_i_Pos_Rad_2(self):
        self.horizontalScrollBar_i_Pos_Rad.setValue(float(self.lineEdit_i_Pos_Rad.text()))

    def updateLinacModel_i_Pos_Trans_2(self):
        self.horizontalScrollBar_i_Pos_Trans.setValue(float(self.lineEdit_i_Pos_Trans.text()))

    def updateLinacModel_i_Ang_Rad_2(self):
        self.horizontalScrollBar_i_Ang_Rad.setValue(float(self.lineEdit_i_Ang_Rad.text()))

    def updateLinacModel_i_Ang_Trans_2(self):
        self.horizontalScrollBar_i_Ang_Trans.setValue(float(self.lineEdit_i_Ang_Trans.text()))

    def updateLinacModel_Rad_Jaw_2(self):
        self.horizontalScrollBar_Rad_Jaw.setValue(float(self.lineEdit_Rad_Jaw.text()))

    def updateLinacModel_Trans_Jaw_2(self):
        self.horizontalScrollBar_Trans_Jaw.setValue(float(self.lineEdit_Trans_Jaw.text()))

    def updateLinacModel_d_Tank_2(self):
        self.horizontalScrollBar_d_Tank.setValue(float(self.lineEdit_d_Tank.text()))


def main():
    print('© 2025 Alberta Health Services, Medical Physics\n'
          'This program comes with ABSOLUTELY NO WARRANTY\n'
          'LinacSimPy is free software, and you are welcome to redistribute it under certain conditions\n'
          'See the HELP menu for details')
    sys.stderr = open('error.log', 'w')
    sys.stdout = open('output.log', 'w')
    # was QtGui.QApplication but gives error
    app = QApplication(sys.argv)
    
    # ND added splash screen
    splash_pix = QPixmap('resources\images\gplv3-or-later.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.show()
    #time.sleep(3)   # unnecessary

    mainForm = linacSimPyMainForm()
    mainForm.show()
    #app.exec_() still worked but not current?
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
