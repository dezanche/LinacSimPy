# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: views\simacKlystronForm.pyc
# Compiled at: 2016-06-14 13:13:49
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
from window_widgets import simacKlystronWidget

class simacKlystronForm(QWidget, simacKlystronWidget.Ui_Form):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
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
        self.radioButton_ChA_4.clicked.connect(self.updateChannelA)
        self.radioButton_ChA_5.clicked.connect(self.updateChannelA)
        self.radioButton_ChA_6.clicked.connect(self.updateChannelA)
        self.radioButton_ChB_1.clicked.connect(self.updateChannelB)
        self.radioButton_ChB_2.clicked.connect(self.updateChannelB)
        self.radioButton_ChB_3.clicked.connect(self.updateChannelB)
        self.radioButton_ChB_4.clicked.connect(self.updateChannelB)
        self.radioButton_ChB_5.clicked.connect(self.updateChannelB)
        self.radioButton_ChB_6.clicked.connect(self.updateChannelB)
        self.comboBox_VDiv_AChan.currentIndexChanged.connect(self.updateVDivChannelA)
        self.comboBox_VDiv_BChan.currentIndexChanged.connect(self.updateVDivChannelB)
        self.comboBox_TDiv.currentIndexChanged.connect(self.updateTDiv)
        self.strFormatter = '{0:.2f}'

    def setController(self, controller):
        self.simacController = controller

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
        linacModel = self.simacController.getLinacModel()
        if self.radioButton_ChA_1.isChecked():
            self.sample = np.loadtxt('resources/parameters/RFDRPWR16.txt')
            self.typicalValue = 0.0
            self.singalLevel = linacModel.P_AC_Kly / 67.0
            self.noiseLevel = 0.007197373 * self.singalLevel
        elif self.radioButton_ChA_2.isChecked():
            self.sample = np.loadtxt('resources/parameters/KlyV16.txt')
            self.typicalValue = 0.0
            self.singalLevel = linacModel.v_Kly / 125.0
            self.noiseLevel = 0.030774429 * self.singalLevel
        elif self.radioButton_ChA_3.isChecked():
            self.sample = np.loadtxt('resources/parameters/LDPWR216.txt')
            self.typicalValue = 0.0
            self.singalLevel = linacModel.P_Acc / 5.63
            self.noiseLevel = 0.013883341 * self.singalLevel
        elif self.radioButton_ChA_4.isChecked():
            self.sample = np.loadtxt('resources/parameters/KlyI16.txt')
            self.typicalValue = 0.0
            self.singalLevel = linacModel.i_Kly / 92.81
            self.noiseLevel = 0.034191775 * self.singalLevel
        elif self.radioButton_ChA_5.isChecked():
            self.sample = np.loadtxt('resources/parameters/PFNV16.txt')
            self.singalLevel = linacModel.v_PFN / (250 / 4)
            self.typicalValue = -7.434 * self.singalLevel
            self.noiseLevel = 0.030774429 * self.singalLevel
        elif self.radioButton_ChA_6.isChecked():
            self.sample = np.loadtxt('resources/parameters/HVPSI16.txt')
            self.typicalValue = 0.0
            self.singalLevel = linacModel.i_HVPS / 1.07
            self.noiseLevel = 0.029602535 * self.singalLevel
        elif self.radioButton_ChA_7.isChecked():
            self.sample = np.loadtxt('resources/parameters/GunI16.txt')
            self.typicalValue = 0.0
            self.singalLevel = linacModel.i_Acc / 178.08
            self.noiseLevel = 0.005172272 * self.singalLevel
        elif self.radioButton_ChA_8.isChecked():
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
        linacModel = self.simacController.getLinacModel()
        if self.radioButton_ChB_1.isChecked():
            self.sampleB = np.loadtxt('resources/parameters/RFDRPWR16.txt')
            self.typicalValueB = 0.0
            self.singalLevelB = linacModel.P_AC_Kly / 67.0
            self.noiseLevelB = 0.007197373 * self.singalLevelB
        elif self.radioButton_ChB_2.isChecked():
            self.sampleB = np.loadtxt('resources/parameters/KlyV16.txt')
            self.typicalValueB = 0.0
            self.singalLevelB = linacModel.v_Kly / 125.0
            self.noiseLevelB = 0.030774429 * self.singalLevelB
        elif self.radioButton_ChB_3.isChecked():
            self.sampleB = np.loadtxt('resources/parameters/LDPWR216.txt')
            self.typicalValueB = 0.0
            self.singalLevelB = linacModel.P_Acc / 5.63
            self.noiseLevelB = 0.013883341 * self.singalLevelB
        elif self.radioButton_ChB_4.isChecked():
            self.sampleB = np.loadtxt('resources/parameters/KlyI16.txt')
            self.typicalValueB = 0.0
            self.singalLevelB = linacModel.i_Kly / 92.81
            self.noiseLevelB = 0.034191775 * self.singalLevelB
        elif self.radioButton_ChB_5.isChecked():
            self.sampleB = np.loadtxt('resources/parameters/PFNV16.txt')
            self.singalLevelB = linacModel.v_PFN / (250 / 4)
            self.typicalValueB = -7.434 * self.singalLevelB
            self.noiseLevelB = 0.030774429 * self.singalLevelB
        elif self.radioButton_ChB_6.isChecked():
            self.sampleB = np.loadtxt('resources/parameters/HVPSI16.txt')
            self.typicalValueB = 0.0
            self.singalLevelB = linacModel.i_HVPS / 1.07
            self.noiseLevelB = 0.029602535 * self.singalLevelB
        elif self.radioButton_ChB_7.isChecked():
            self.sampleB = np.loadtxt('resources/parameters/GunI16.txt')
            self.typicalValueB = 0.0
            self.singalLevelB = linacModel.i_Acc / 178.08
            self.noiseLevelB = 0.005172272 * self.singalLevelB
        elif self.radioButton_ChB_8.isChecked():
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
        linacModel = self.simacController.getLinacModel()
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
        linacModel = self.simacController.getLinacModel()
        self.lineEdit_P_AC_Kly.setText(self.strFormatter.format(linacModel.P_AC_Kly))
        self.lineEdit_v_Kly.setText(self.strFormatter.format(linacModel.v_Kly))
        self.lineEdit_P_Acc.setText(self.strFormatter.format(linacModel.P_Acc))
        self.lineEdit_i_Kly.setText(self.strFormatter.format(linacModel.i_Kly))
        self.lineEdit_v_PFN.setText(self.strFormatter.format(linacModel.v_PFN))
        self.lineEdit_I_HVPS.setText(self.strFormatter.format(linacModel.i_HVPS))
        self.lineEdit_Omega.setText(self.strFormatter.format(linacModel.Omega))
        self.lineEdit_k_Kly.setText(self.strFormatter.format(linacModel.k_Kly))
        self.lineEdit_P_Kly_Refl.setText(self.strFormatter.format(linacModel.P_Kly_Refl))
        self.lineEdit_P_AC_Kly.setText(self.strFormatter.format(linacModel.P_AC_Kly))
        self.lineEdit_Efficiency.setText(self.strFormatter.format(linacModel.Efficiency))
        self.updateGraph()
        self.updateCalculation()
        self.updateOscilloscopeGraph()

    def createGraph(self):
        rcParams.update({'figure.autolayout': True})
        self.dpi = 100
        self.figure = Figure((1.0, 1.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout_BR.addWidget(self.canvas)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_title('Klystron Characteristic Curves', fontsize=8)
        self.axes.set_xlabel('RF Power In [W]', fontsize=8)
        self.axes.set_ylabel('RF Power Out [MW]', fontsize=8)
        self.axes.grid(True)
        self.figure.patch.set_facecolor('white')
        self.axes.set_xlim([0, 200])
        self.axes.set_ylim([0, 6])
        # AttributeError: 'YTick' object has no attribute 'label'.
        #zed = [ tick.label.set_fontsize(8) for tick in self.axes.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(8) for tick in self.axes.xaxis.get_major_ticks() ]
        self.axes.tick_params(axis='x', labelsize=8)
        self.axes.tick_params(axis='y', labelsize=8)
        v_Kly_Ref = np.array([95, 100, 105, 110, 115, 120, 125])
        v_Kly_Ref.shape = (7, 1)
        P_AC_Kly_C_Ref = 2226.7 / (v_Kly_Ref - 91.765)
        P_AC_Kly_C_Ref[P_AC_Kly_C_Ref < 0.0] = float('inf')
        P_Acc_Max_Ref = 0.12 * v_Kly_Ref - 9.37
        P_Acc_Max_Ref[P_Acc_Max_Ref < 0.0] = 0.0
        Chi = 1 / np.sqrt(P_AC_Kly_C_Ref) * np.sqrt(self.P_AC_Kly_Ref) * 1.84
        k_Kly_Ref = np.multiply(np.matlib.repmat(P_Acc_Max_Ref / P_AC_Kly_C_Ref, 1, self.P_AC_Kly_Ref.size), 10 * np.power(np.divide(special.jv(1, Chi), Chi), 2))
        self.P_Acc_Ref = np.matlib.repmat(self.P_AC_Kly_Ref, v_Kly_Ref.size, 1) * k_Kly_Ref
        self.P_AC_Kly_Ref.shape = (200, 1)
        for i in range(7):
            temp = self.P_Acc_Ref[i, :]
            temp.shape = (200, 1)
            self.axes.plot(self.P_AC_Kly_Ref, temp, linestyle='-', linewidth=1)

    def updateGraph(self):
        """ Redraws the figure
        """
        linacModel = self.simacController.getLinacModel()
        self.axes.cla()
        self.axes.set_title('Klystron Characteristic Curves', fontsize=8)
        self.axes.set_xlabel('RF Power In [W]', fontsize=8)
        self.axes.set_ylabel('RF Power Out [MW]', fontsize=8)
        #zed = [ tick.label.set_fontsize(8) for tick in self.axes.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(8) for tick in self.axes.xaxis.get_major_ticks() ]
        self.axes.tick_params(axis='x', labelsize=8)
        self.axes.tick_params(axis='y', labelsize=8)
        self.axes.grid(True)
        if linacModel.P_AC_Kly_C == 0:
            k_Kly = 0
        else:
            Chi = 1 / np.sqrt(linacModel.P_AC_Kly_C) * np.sqrt(self.P_AC_Kly_Ref) * 1.84
            k_Kly = np.multiply(np.matlib.repmat(linacModel.P_Acc_Max / linacModel.P_AC_Kly_C, 1, self.P_AC_Kly_Ref.size), 10.0 * np.power(special.jv(1, Chi) / Chi, 2))
        P_Acc_Loadline = np.multiply(np.multiply(1 - linacModel.R_Coeff * linacModel.R_Coeff, k_Kly), self.P_AC_Kly_Ref)
        self.axes.set_xlim([0, 200])
        self.axes.set_ylim([0, 6])
        for i in range(7):
            temp = self.P_Acc_Ref[i, :]
            temp.shape = (200, 1)
            self.axes.plot(self.P_AC_Kly_Ref, temp, linestyle='-', linewidth=1)

        self.axes.plot([linacModel.P_AC_Kly, linacModel.P_AC_Kly], [0, 6], linestyle='-', linewidth=1)
        self.axes.plot([0, 200], [linacModel.P_Acc, linacModel.P_Acc], linestyle='-', linewidth=1)
        self.axes.plot(self.P_AC_Kly_Ref, P_Acc_Loadline, linestyle='-', linewidth=1)
        self.axes.plot([linacModel.P_AC_Kly, linacModel.P_AC_Kly], [linacModel.P_Acc, linacModel.P_Acc], marker='o', markersize=6, markeredgewidth=1, markeredgecolor='b', markerfacecolor='None')
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
        #self.axes_scope.set_axis_bgcolor('black')
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
        fig_size = self.figure_scope.get_size_inches()
        w, h = fig_size[0], fig_size[1]
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

    def updateOscilloscopeGraph(self):
        linacModel = self.simacController.getLinacModel()
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
# okay decompiling simacKlystronForm.pyc
