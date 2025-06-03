
import sys, os, random, math, numpy as np, numpy.matlib
from scipy import special
from scipy import interpolate
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import rcParams
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from window_widgets import linacSimPyAcceleratorWidget

class linacSimPyAcceleratorForm(QWidget, linacSimPyAcceleratorWidget.Ui_Form):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.i_BMag_Beam_Ref = np.arange(0.0, 0.31, 0.05)
        self.P_Acc_Ref = np.array([1.0, 3.0, 5.0, 7.0, 9.0])
        self.P_Acc_Ref.shape = (5, 1)
        self.P_AC_Kly_Ref = np.arange(1, 201, 1)
        self.P_AC_Kly_Ref.shape = (1, 200)
        self.currentChannelA = True
        self.dDiv_Time = 1
        self.createGraph()
        self.createOscilloscoptGraph()
        self.radioButton_ChA_1.setChecked(True)
        self.radioButton_ChB_1.setChecked(True)
        self.radioButton_ChA_1.clicked.connect(self.updateChannelA)
        self.radioButton_ChA_2.clicked.connect(self.updateChannelA)
        self.radioButton_ChA_3.clicked.connect(self.updateChannelA)
        self.radioButton_ChB_1.clicked.connect(self.updateChannelB)
        self.radioButton_ChB_2.clicked.connect(self.updateChannelB)
        self.radioButton_ChB_3.clicked.connect(self.updateChannelB)
        self.comboBox_VDiv_AChan.currentIndexChanged.connect(self.updateVDivChannelA)
        self.comboBox_VDiv_BChan.currentIndexChanged.connect(self.updateVDivChannelB)
        self.comboBox_TDiv.currentIndexChanged.connect(self.updateTDiv)
        self.strFormatter = '{0:.2f}'

    def setController(self, controller):
        self.linacSimPyController = controller

    def updateCalculation(self):
        self.calculateChannelA()
        self.calculateChannelB()
        self.calculateVDivChannelA()
        self.calcualteVDivChannelB()
        self.calculateTDiv()

    def updateChannelA(self):
        self.calculateChannelA()
        self.calculateChannelB()
        self.updateOscilloscopeGraph()

    def calculateChannelA(self):
        linacModel = self.linacSimPyController.getLinacModel()
        if self.radioButton_ChA_1.isChecked():
            self.sample = np.loadtxt('resources/parameters/LDPWR216.txt')
            self.typicalValue = 0.0
            self.singalLevel = linacModel.P_Acc / 5.63
            self.noiseLevel = 0.013883341 * self.singalLevel
        elif self.radioButton_ChA_2.isChecked():
            self.sample = np.loadtxt('resources/parameters/GunI16.txt')
            self.typicalValue = 0.0
            self.singalLevel = linacModel.i_Acc / 178.08
            self.noiseLevel = 0.005172272 * self.singalLevel
        elif self.radioButton_ChA_3.isChecked():
            self.sample = np.loadtxt('resources/parameters/TarI16.txt')
            self.typicalValue = 0.0
            self.singalLevel = linacModel.i_Tar / 37.2
            self.noiseLevel = 0.014203911 * self.singalLevel
        self.currentChannelA = True

    def updateChannelB(self):
        self.calculateChannelA()
        self.calculateChannelB()
        self.updateOscilloscopeGraph()

    def calculateChannelB(self):
        linacModel = self.linacSimPyController.getLinacModel()
        if self.radioButton_ChB_1.isChecked():
            self.sampleB = np.loadtxt('resources/parameters/LDPWR216.txt')
            self.typicalValueB = 0.0
            self.singalLevelB = linacModel.P_Acc / 5.63
            self.noiseLevelB = 0.013883341 * self.singalLevelB
        elif self.radioButton_ChB_2.isChecked():
            self.sampleB = np.loadtxt('resources/parameters/GunI16.txt')
            self.typicalValueB = 0.0
            self.singalLevelB = linacModel.i_Acc / 178.08
            self.noiseLevelB = 0.005172272 * self.singalLevelB
        elif self.radioButton_ChB_3.isChecked():
            self.sampleB = np.loadtxt('resources/parameters/TarI16.txt')
            self.typicalValueB = 0.0
            self.singalLevelB = linacModel.i_Tar / 37.2
            self.noiseLevelB = 0.014203911 * self.singalLevelB
        self.currentChannelA = False

    def updateVDivChannelA(self):
        self.calculateVDivChannelA()
        self.updateOscilloscopeGraph()

    def calculateVDivChannelA(self):
        iValue_VoltageA = self.comboBox_VDiv_AChan.currentIndex() + 1
        dExp2 = int(math.floor((iValue_VoltageA + 1) / 3)) - 3
        if iValue_VoltageA % 3 == 0:
            self.dMax_VoltageA = 2 * (2 * math.pow(10, dExp2))
        elif iValue_VoltageA % 3 == 1:
            self.dMax_VoltageA = 2 * (5 * math.pow(10, dExp2))
        elif iValue_VoltageA % 3 == 2:
            self.dMax_VoltageA = 2 * (1 * math.pow(10, dExp2))

    def updateVDivChannelB(self):
        self.calcualteVDivChannelB()
        self.updateOscilloscopeGraph()

    def calcualteVDivChannelB(self):
        iValue_VoltageB = self.comboBox_VDiv_BChan.currentIndex() + 1
        dExp3 = int(math.floor((iValue_VoltageB + 1) / 3)) - 3
        if iValue_VoltageB % 3 == 0:
            self.dMax_VoltageB = 2 * (2 * math.pow(10, dExp3))
        elif iValue_VoltageB % 3 == 1:
            self.dMax_VoltageB = 2 * (5 * math.pow(10, dExp3))
        elif iValue_VoltageB % 3 == 2:
            self.dMax_VoltageB = 2 * (1 * math.pow(10, dExp3))

    def updateTDiv(self):
        self.calculateTDiv()
        self.updateOscilloscopeGraph()

    def calculateTDiv(self):
        linacModel = self.linacSimPyController.getLinacModel()
        iValue_Time = self.comboBox_TDiv.currentIndex() + 1
        dExp = int(math.floor((iValue_Time - 1) / 3)) - 6
        if (iValue_Time - 1) % 3 == 0:
            self.dDiv_Time = 1 * math.pow(10, dExp)
        elif (iValue_Time - 1) % 3 == 1:
            self.dDiv_Time = 2 * math.pow(10, dExp)
        elif (iValue_Time - 1) % 3 == 2:
            self.dDiv_Time = 5 * math.pow(10, dExp)
        self.dStep_Time = min(linacModel.Tau * 1e-06, self.dDiv_Time / 1000.0)

    def updateView(self):
        linacModel = self.linacSimPyController.getLinacModel()
        self.lineEdit_P_Acc.setText(self.strFormatter.format(float(linacModel.P_Acc)))
        self.lineEdit_i_Acc.setText(self.strFormatter.format(float(linacModel.i_Acc)))
        self.lineEdit_i_Tar.setText(self.strFormatter.format(linacModel.i_Tar))
        self.lineEdit_Tau.setText(self.strFormatter.format(linacModel.Tau))
        self.lineEdit_v_Gun.setText(self.strFormatter.format(linacModel.v_Gun))
        self.lineEdit_v_Grid.setText(self.strFormatter.format(linacModel.v_Grid))
        self.lineEdit_i_Coil_BMag.setText(self.strFormatter.format(linacModel.i_Coil_BMag))
        self.lineEdit_T_Av_Tar.setText(self.strFormatter.format(linacModel.T_Av_Tar))
        self.lineEdit_T_Av_BMag.setText(self.strFormatter.format(linacModel.T_Av_BMag))
        self.lineEdit_P_Beam_Acc.setText(self.strFormatter.format(linacModel.P_Beam_Acc))
        self.lineEdit_Eff_Acc.setText(self.strFormatter.format(linacModel.Eff_Acc))
        self.updateGraph()
        self.updateCalculation()
        self.updateOscilloscopeGraph()

    def createGraph(self):
        rcParams.update({'figure.autolayout': True})
        self.dpi = 100
        self.figure = Figure((2.0, 1.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout_BR.addWidget(self.canvas)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_title('Beam Characteristic Curves', fontsize=8)       # change here too? (set again below)
        self.axes.set_xlabel('Beam Current [A]', fontsize=8)
        self.axes.set_ylabel('Beam Energy [MeV]', fontsize=8)
        self.axes.grid(True)
        self.figure.patch.set_facecolor('white')
        #zed = [ tick.label.set_fontsize(8) for tick in self.axes.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(8) for tick in self.axes.xaxis.get_major_ticks() ]
        self.axes.tick_params(axis='x', labelsize=8)
        self.axes.tick_params(axis='y', labelsize=8)
        Z_Acc = 48.77
        self.T_Av_BMag_Ref = np.matlib.repmat(np.sqrt(self.P_Acc_Ref * Z_Acc), 1, self.i_BMag_Beam_Ref.size) - np.matlib.repmat(Z_Acc * (self.i_BMag_Beam_Ref / 2.0), self.P_Acc_Ref.size, 1)
        self.i_BMag_Beam_Ref.shape = (7, 1)
        for i in range(5):
            temp = self.T_Av_BMag_Ref[i, :]
            temp.shape = (7, 1)
            self.axes.plot(self.i_BMag_Beam_Ref, temp)

    def updateGraph(self):
        """ Redraws the figure
        """
        linacModel = self.linacSimPyController.getLinacModel()
        self.axes.cla()
        self.axes.grid(True)
        self.axes.set_title('Accelerator Characteristic Curves (Load Lines)', fontsize=8)    # changed title text
        self.axes.set_xlabel('Beam Current [A]', fontsize=8)
        self.axes.set_ylabel('Beam Energy [MeV]', fontsize=8)
        temp1 = np.matlib.repmat(np.sqrt(self.P_Acc_Ref * linacModel.Z_Acc), 1, self.i_BMag_Beam_Ref.size)
        temp1.shape = (35, 1)
        temp2 = np.matlib.repmat(linacModel.Z_Acc * (self.i_BMag_Beam_Ref / 2.0), self.P_Acc_Ref.size, 1)
        temp2.shape = (35, 1)
        self.T_Av_BMag_Ref = temp1 - temp2
        self.T_Av_BMag_Ref.shape = (5, 7)
        self.i_BMag_Beam_Ref.shape = (7, 1)
        for i in range(5):
            temp = self.T_Av_BMag_Ref[i, :]
            temp.shape = (7, 1)
            self.axes.plot(self.i_BMag_Beam_Ref, temp)

        LoadLine = np.sqrt(linacModel.P_Acc * linacModel.Z_Acc) - linacModel.Z_Acc * (self.i_BMag_Beam_Ref / 2.0)
        self.axes.set_xlim([0, 0.3])
        self.axes.set_ylim([0, 25])
        self.axes.plot([linacModel.i_BMag_Beam / 1000, linacModel.i_BMag_Beam / 1000], [0, 25])
        self.axes.plot([0, 0.5], [linacModel.T_Av_BMag, linacModel.T_Av_BMag])
        self.axes.plot(self.i_BMag_Beam_Ref, LoadLine)
        self.axes.plot(linacModel.i_BMag_Beam / 1000, linacModel.T_Av_BMag, marker='o', markersize=6, markeredgewidth=1, markeredgecolor='b', markerfacecolor='None')
        #zed = [ tick.label.set_fontsize(8) for tick in self.axes.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(8) for tick in self.axes.xaxis.get_major_ticks() ]
        self.axes.tick_params(axis='x', labelsize=8)
        self.axes.tick_params(axis='y', labelsize=8)
        self.canvas.draw()

    def createOscilloscoptGraph(self):
        self.dpi = 100
        self.figure_scope = Figure((2.0, 1.0), dpi=self.dpi)
        self.canvas_scope = FigureCanvas(self.figure_scope)
        self.gridLayout_scope.addWidget(self.canvas_scope)
        rect = (0, 0, 1, 1)
        self.axes_scope = self.figure_scope.add_axes(rect)
        self.axes_scope.grid(True)
        self.axes_scope.grid(color='green', alpha=1.0)
        #set_facecolor replaces set_axis_bgcolor
        self.axes_scope.set_facecolor('black')
        self.axes_scope.spines['bottom'].set_color('green')
        self.axes_scope.spines['top'].set_color('green')
        self.axes_scope.spines['left'].set_color('green')
        self.axes_scope.spines['right'].set_color('green')
        self.axes_scope.spines['bottom'].set_linewidth(4)
        self.axes_scope.spines['top'].set_linewidth(4)
        self.axes_scope.spines['left'].set_linewidth(4)
        self.axes_scope.spines['right'].set_linewidth(4)
        self.axes_scope.grid(color='green', alpha=1.0, linewidth='2')

    def updateOscilloscopeGraph(self):
        linacModel = self.linacSimPyController.getLinacModel()
        dVector_TimeA, dVector_VoltageA = linacModel.updateSingal(self.typicalValue, self.singalLevel, self.noiseLevel, self.sample, self.dMax_VoltageA, self.dStep_Time, self.dDiv_Time)
        dVector_TimeB, dVector_VoltageB = linacModel.updateSingal(self.typicalValueB, self.singalLevelB, self.noiseLevelB, self.sampleB, self.dMax_VoltageB, self.dStep_Time, self.dDiv_Time)
        self.axes_scope.cla()
        self.axes_scope.grid(True)
        self.axes_scope.set_xlim([-4 * self.dDiv_Time, 4 * self.dDiv_Time])
        self.axes_scope.set_ylim([-1, 1])
        self.axes_scope.plot(dVector_TimeA, dVector_VoltageA + 0.25, color='green')
        self.axes_scope.plot(dVector_TimeB, dVector_VoltageB - 0.25, color='green')
        self.axes_scope.grid(color='green', alpha=1.0, linewidth='2')
        self.canvas_scope.draw()

