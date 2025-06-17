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


# ND removed some unused imports

import math, numpy as np, numpy.matlib  #sys, os, random, 
#from scipy import special
#from scipy import interpolate
#import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
#from matplotlib import rcParams
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget  #was*
#from PyQt5.QtCore import *
#from PyQt5 import QtGui
from window_widgets import linacSimPyTreatmentHeadWidget

class linacSimPyTreatmentHeadForm(QWidget, linacSimPyTreatmentHeadWidget.Ui_Form):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.createdFigures = False
        self.strFormatter = '{0:.2f}'

    def setController(self, controller):
        self.linacSimPyController = controller

    def createFigures(self):
        self.createBLGraph()
        self.createBRGraph()
        self.createdFigures = True

    def updateView(self):
        if self.createdFigures == False:
            self.createFigures()
        linacModel = self.linacSimPyController.getLinacModel()
        self.lineEdit_T_Av_Tar.setText(self.strFormatter.format(linacModel.T_Av_Tar))
        self.lineEdit_i_Tar.setText(self.strFormatter.format(linacModel.i_Tar))
        self.lineEdit_Eff_Tar.setText(self.strFormatter.format(linacModel.Eff_Tar))
        self.lineEdit_L_Pos_Rad.setText(self.strFormatter.format(linacModel.Half_Dose_Rad_Left))
        self.lineEdit_R_Pos_Rad.setText(self.strFormatter.format(linacModel.Half_Dose_Rad_Right))
        self.lineEdit_L_Pos_Trans.setText(self.strFormatter.format(linacModel.Half_Dose_Trans_Left))
        self.lineEdit_R_Pos_Trans.setText(self.strFormatter.format(linacModel.Half_Dose_Trans_Right))
        self.lineEdit_d_Tank.setText(self.strFormatter.format(linacModel.d_Tank))
        self.lineEdit_Rad_Jaw.setText(self.strFormatter.format(linacModel.Rad_Jaw))
        self.lineEdit_Trans_Jaw.setText(self.strFormatter.format(linacModel.Trans_Jaw))
        self.lineEdit_S_Ion_R.setText(self.strFormatter.format(linacModel.S_Ion_R))
        self.lineEdit_S_Ion_T.setText(self.strFormatter.format(linacModel.S_Ion_T))
        self.lineEdit_Flatness_R.setText(self.strFormatter.format(linacModel.Flatness_R))
        self.lineEdit_Flatness_T.setText(self.strFormatter.format(linacModel.Flatness_T))
        self.lineEdit_dD_Ion.setText(self.strFormatter.format(linacModel.dD_Ion))
        self.updateBLGraph()
        self.updateBRGraph()

    def createBLGraph(self):
        self.dpi = 100
        self.figure_BL = Figure((2.0, 1.0), dpi=self.dpi)
        self.canvas_BL = FigureCanvas(self.figure_BL)
        self.gridLayout_BL.addWidget(self.canvas_BL)
        iN_Points = 100
        linacModel = self.linacSimPyController.getLinacModel()
        self.Rad_Tar = np.arange(-8 * linacModel.Rad_StDev_SMag, 8 * linacModel.Rad_StDev_SMag, 16 * linacModel.Rad_StDev_SMag / (iN_Points - 1))
        self.Trans_Tar = np.arange(-8 * linacModel.Trans_StDev_SMag, 8 * linacModel.Trans_StDev_SMag, 16 * linacModel.Trans_StDev_SMag / (iN_Points - 1))
        self.dRad_Tar = np.arange(-24 * linacModel.dRad_StDev_SMag, 24 * linacModel.dRad_StDev_SMag, 48 * linacModel.dRad_StDev_SMag / (iN_Points - 1))
        self.dTrans_Tar = np.arange(-24 * linacModel.dTrans_StDev_SMag, 24 * linacModel.dTrans_StDev_SMag, 48 * linacModel.dTrans_StDev_SMag / (iN_Points - 1))
        self.Rad_Tar, self.Trans_Tar = np.meshgrid(self.Rad_Tar, self.Trans_Tar)
        self.dRad_Tar, self.dTrans_Tar = np.meshgrid(self.dRad_Tar, self.dTrans_Tar)
        self.I_Pos = 1 / (2 * math.pi * np.sqrt(linacModel.Rad_StDev_SMag * linacModel.Trans_StDev_SMag)) * np.exp(-(1.0 / 2.0) * (np.power(self.Rad_Tar / linacModel.Rad_StDev_SMag, 2) + np.power(self.Trans_Tar / linacModel.Trans_StDev_SMag, 2)))
        self.I_Ang = 1 / (2 * math.pi * np.sqrt(linacModel.dRad_StDev_SMag * linacModel.dTrans_StDev_SMag)) * np.exp(-(1.0 / 2.0) * (np.power(self.dRad_Tar / linacModel.dRad_StDev_SMag, 2) + np.power(self.dTrans_Tar / linacModel.dTrans_StDev_SMag, 2)))
        self.axes_BL1 = self.figure_BL.add_subplot(211)
        self.axes_BL1.set_title('Beam Position at Target', fontsize=7)
        self.axes_BL1.set_xlabel('Radial Position [cm]', fontsize=8)
        self.axes_BL1.set_ylabel('Transverse Position [cm]', fontsize=8)
        #self.axes_BL1.autoscale(True)
        #self.axes_BL1.axis('equal')    #added
        self.axes_BL1.set_xlim([-0.25, 0.25])
        self.axes_BL1.set_ylim([-0.25, 0.25])
        self.axes_BL1.xaxis.set_major_locator(MultipleLocator(0.1))
        self.axes_BL1.yaxis.set_major_locator(MultipleLocator(0.1)) # was 0.2; changed also below
        self.pc_BL1 = self.axes_BL1.pcolormesh(self.Rad_Tar, self.Trans_Tar, self.I_Pos)
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BL1.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BL1.xaxis.get_major_ticks() ]
        # replaced with:
        self.axes_BL1.tick_params(axis='x', labelsize=7)
        self.axes_BL1.tick_params(axis='y', labelsize=7)
        self.axes_BL2 = self.figure_BL.add_subplot(212)
        self.axes_BL2.set_title('Beam Angle at Target', fontsize=7)
        self.axes_BL2.set_xlabel('Radial Angle [rad]', fontsize=8)
        self.axes_BL2.set_ylabel('Transverse Angle [rad]', fontsize=8)
        #self.axes_BL2.axis('equal')    #added
        self.axes_BL2.set_xlim([-0.02, 0.02])
        self.axes_BL2.set_ylim([-0.02, 0.02])
        self.axes_BL2.xaxis.set_major_locator(MultipleLocator(0.01))
        self.axes_BL2.yaxis.set_major_locator(MultipleLocator(0.01))    # was 0.02; changed also below
        self.axes_BL2.pcolormesh(self.dRad_Tar, self.dTrans_Tar, self.I_Ang)
        self.axes_BL2.grid(True)
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BL2.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BL2.xaxis.get_major_ticks() ]
        self.axes_BL2.tick_params(axis='x', labelsize=7)
        self.axes_BL2.tick_params(axis='y', labelsize=7)
        self.figure_BL.patch.set_facecolor('white')
        self.canvas_BL.draw()

    def updateBLGraph(self):
        """ Redraws the figure
        """
        linacModel = self.linacSimPyController.getLinacModel()
        majorFormatter = FormatStrFormatter('%1.2f')
        self.axes_BL1.cla()
        self.axes_BL1.set_title('Beam Position at Target', fontsize=7)
        self.axes_BL1.set_xlabel('Radial Position [cm]', fontsize=8)
        self.axes_BL1.set_ylabel('Transverse Position [cm]', fontsize=8)
        self.axes_BL1.autoscale(False)
        self.axes_BL1.set_xlim([-0.25, 0.25])
        self.axes_BL1.set_ylim([-0.25, 0.25])
        # these 2 lines don't seem to be required while for BL2 they are
        #self.axes_BL1.xaxis.set_major_locator(MultipleLocator(0.1))
        #self.axes_BL1.yaxis.set_major_locator(MultipleLocator(0.1))
        self.axes_BL1.pcolormesh(self.Rad_Tar + linacModel.PrincipalRay_Tar[0], self.Trans_Tar + linacModel.PrincipalRay_Tar[2], self.I_Pos)
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BL1.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BL1.xaxis.get_major_ticks() ]
        self.axes_BL1.tick_params(axis='x', labelsize=7)
        self.axes_BL1.tick_params(axis='y', labelsize=7)
        self.axes_BL2.cla()
        self.axes_BL2.set_title('Beam Angle at Target', fontsize=7)
        self.axes_BL2.set_xlabel('Radial Angle [rad]', fontsize=8)
        self.axes_BL2.set_ylabel('Transverse Angle [rad]', fontsize=8)
        self.axes_BL2.set_xlim([-0.02, 0.02])
        self.axes_BL2.set_ylim([-0.02, 0.02])
        self.axes_BL2.xaxis.set_major_locator(MultipleLocator(0.01))
        self.axes_BL2.yaxis.set_major_locator(MultipleLocator(0.01))
        self.axes_BL2.yaxis.set_major_formatter(majorFormatter)
        self.axes_BL2.pcolormesh(self.dRad_Tar + linacModel.PrincipalRay_Tar[1], self.dTrans_Tar + linacModel.PrincipalRay_Tar[3], self.I_Ang)
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BL2.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BL2.xaxis.get_major_ticks() ]
        self.axes_BL2.tick_params(axis='x', labelsize=7)
        self.axes_BL2.tick_params(axis='y', labelsize=7)
        self.canvas_BL.draw()

    def createBRGraph(self):
        self.dpi = 100
        self.figure_BR = Figure((2.0, 1.0), dpi=self.dpi)
        self.canvas_BR = FigureCanvas(self.figure_BR)
        self.gridLayout_BR.addWidget(self.canvas_BR)
        self.axes_BR1 = self.figure_BR.add_subplot(211)
        self.axes_BR1.set_title('Radial Dose Profile', fontsize=7)
        self.axes_BR1.set_xlabel('Radial Position [cm]', fontsize=7)
        self.axes_BR1.set_ylabel('Dose Rate [cGy/min]', fontsize=7)
        self.axes_BR1.grid(True)
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BR1.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BR1.xaxis.get_major_ticks() ]
        self.axes_BR1.tick_params(axis='x', labelsize=7)
        self.axes_BR1.tick_params(axis='y', labelsize=7)
        self.axes_BR2 = self.figure_BR.add_subplot(212)
        self.axes_BR2.set_title('Transverse Dose Profile', fontsize=7)
        self.axes_BR2.set_xlabel('Transverse Position [cm]', fontsize=7)
        self.axes_BR2.set_ylabel('Dose Rate [cGy/min]', fontsize=7)
        self.axes_BR2.grid(True)
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BR2.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BR2.xaxis.get_major_ticks() ]
        self.axes_BR2.tick_params(axis='x', labelsize=7)
        self.axes_BR2.tick_params(axis='y', labelsize=7)
        self.figure_BR.patch.set_facecolor('white')

    def updateBRGraph(self):
        """ Redraws the figure
        """
        linacModel = self.linacSimPyController.getLinacModel()
        self.axes_BR1.cla()
        majorLocatorX = MultipleLocator(10)
        majorLocatorY = MultipleLocator(1000)
        self.axes_BR1.set_title('Radial Profile', fontsize=7)
        self.axes_BR1.set_xlabel('Radial Position [cm]', fontsize=7)
        self.axes_BR1.set_ylabel('Dose Rate [cGy/min]', fontsize=7)
        self.axes_BR1.grid(True)
        self.axes_BR1.set_xlim([-25, 25])
        self.axes_BR1.xaxis.set_major_locator(majorLocatorX)
        self.axes_BR1.yaxis.set_major_locator(majorLocatorY) # changed from BL1 to BR1
        self.axes_BR1.plot(linacModel.Rad_Fine, linacModel.Dose_Rad)
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BR1.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BR1.xaxis.get_major_ticks() ]
        self.axes_BR1.tick_params(axis='x', labelsize=7)
        self.axes_BR1.tick_params(axis='y', labelsize=7)
        self.axes_BR2.cla()
        self.axes_BR2.set_title('Transverse Profile', fontsize=7)
        self.axes_BR2.set_xlabel('Transverse Position [cm]', fontsize=7)
        self.axes_BR2.set_ylabel('Dose Rate [cGy/min]', fontsize=7)
        self.axes_BR2.grid(True)
        self.axes_BR2.set_xlim([-25, 25])
        self.axes_BR2.xaxis.set_major_locator(majorLocatorX)
        self.axes_BR2.yaxis.set_major_locator(majorLocatorY) # changed from BL2 to BR2
        self.axes_BR2.plot(linacModel.Trans_Fine, linacModel.Dose_Trans)
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BR2.yaxis.get_major_ticks() ]
        #zed = [ tick.label.set_fontsize(7) for tick in self.axes_BR2.xaxis.get_major_ticks() ]
        self.axes_BR2.tick_params(axis='x', labelsize=7)
        self.axes_BR2.tick_params(axis='y', labelsize=7)
        self.canvas_BR.draw()

