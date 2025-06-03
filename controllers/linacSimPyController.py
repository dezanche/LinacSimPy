# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: controllers\simacController.pyc
# Compiled at: 2016-09-13 08:58:27
import sys, os, random, numpy as np

class simacController:

    def __init__(self):
        self.simacUpdateLinacModel = False

    def setLinacModel(self, model):
        self.simacLinacModel = model

    def getLinacModel(self):
        return self.simacLinacModel

    def setMainView(self, mainView):
        self.simacMainView = mainView

    def setKlystronView(self, KlystronView):
        self.simacKlystronView = KlystronView

    def setAcceleratorView(self, AcceleratorView):
        self.simacAcceleratorView = AcceleratorView

    def setTreatmentHeadView(self, TreatementHeadView):
        self.simacTreatementHeadView = TreatementHeadView

    def updateLinacModelWithParameters(self, paramSetting):
        self.simacLinacModel.PRF = paramSetting.PRF
        self.simacLinacModel.Omega = paramSetting.Omega
        self.simacLinacModel.P_AC_Kly = paramSetting.P_AC_Kly
        self.simacLinacModel.v_Kly = paramSetting.v_Kly
        self.simacLinacModel.v_Gun = paramSetting.v_Gun
        self.simacLinacModel.Tau = paramSetting.Tau
        self.simacLinacModel.v_Grid = paramSetting.v_Grid
        self.simacLinacModel.i_Coil_BMag = paramSetting.i_Coil_BMag
        self.simacLinacModel.i_Pos_Rad = paramSetting.i_Pos_Rad
        self.simacLinacModel.i_Pos_Trans = paramSetting.i_Pos_Trans
        self.simacLinacModel.i_Ang_Rad = paramSetting.i_Ang_Rad
        self.simacLinacModel.i_Ang_Trans = paramSetting.i_Ang_Trans
        self.simacLinacModel.Rad_Jaw = paramSetting.Rad_Jaw
        self.simacLinacModel.Trans_Jaw = paramSetting.Trans_Jaw
        self.simacLinacModel.d_Tank = paramSetting.d_Tank
        if paramSetting.Energy == 0:
            self.simacLinacModel.Z_Acc = 0
            self.simacLinacModel.t_W = 0
            self.simacLinacModel.t_Cu = 0
            self.simacLinacModel.FilterDensity = 0
            self.simacLinacModel.r_Fil = 0
            self.simacLinacModel.t_Fil = 0
        elif paramSetting.Energy == 6:
            self.simacLinacModel.Z_Acc = 16.57
            self.simacLinacModel.t_W = 1.4437
            self.simacLinacModel.t_Cu = 1.792
            self.simacLinacModel.Factor = 1.0
            self.simacLinacModel.FilterCoefficients = self.simacLinacModel.Copper_murho
            self.simacLinacModel.FilterDensity = 8.92
            self.simacLinacModel.r_Fil = np.arange(0.0, 1.6, 0.1) * 2.54
            self.simacLinacModel.t_Fil = np.array([
             0.8676, 0.8647, 0.8292, 0.7704, 0.6908, 
             0.6415, 0.5489, 0.4862, 0.3906, 0.3245, 0.2535, 
             0.2131, 0.1501, 
             0.1065, 
             0.0593, 0.0]) * 2.54
        elif paramSetting.Energy == 15:
            self.simacLinacModel.Z_Acc = 47.88
            self.simacLinacModel.t_W = 1.925
            self.simacLinacModel.t_Cu = 7.168
            self.simacLinacModel.Factor = 1.0
            self.simacLinacModel.FilterCoefficients = self.simacLinacModel.Tungsten_murho
            self.simacLinacModel.FilterDensity = 16.9
            self.simacLinacModel.r_Fil = np.arange(0.0, 1.6, 0.1) * 2.54
            self.simacLinacModel.t_Fil = np.array([
             0.7832, 0.7482, 0.6556, 0.5403, 0.4617, 
             0.3932, 0.3451, 0.2513, 0.2054, 0.1517, 0.1289, 
             0.0835, 0.0566, 
             0.0281, 
             0.0193, 0.0415]) * 2.54
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_PRF(self, index):
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
        self.simacLinacModel.PRF = value
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_Energy(self, energyIndex):
        if energyIndex == 0:
            self.simacLinacModel.d_Tank = 0
            self.simacLinacModel.i_Coil_BMag = 0
            self.simacLinacModel.v_Gun = 0
            self.simacLinacModel.v_Kly = 0
            self.simacLinacModel.v_Grid = 0
            self.simacLinacModel.Z_Acc = 0
            self.simacLinacModel.t_W = 0
            self.simacLinacModel.t_Cu = 0
            self.simacLinacModel.FilterDensity = 0
            self.simacLinacModel.r_Fil = 0
            self.simacLinacModel.t_Fil = 0
            self.simacLinacModel.P_AC_Kly = 0
            self.simacUpdateLinacModel = False
        elif energyIndex == 1:
            self.simacLinacModel.d_Tank = 1.5
            self.simacLinacModel.i_Coil_BMag = 65.0
            self.simacLinacModel.v_Gun = 16.0
            self.simacLinacModel.v_Kly = 104.0
            self.simacLinacModel.v_Grid = 0.0
            self.simacLinacModel.Z_Acc = 16.57
            self.simacLinacModel.t_W = 1.4437
            self.simacLinacModel.t_Cu = 1.792
            self.simacLinacModel.Factor = 1.0
            self.simacLinacModel.FilterCoefficients = self.simacLinacModel.Copper_murho
            self.simacLinacModel.FilterDensity = 8.92
            self.simacLinacModel.r_Fil = np.arange(0.0, 1.6, 0.1) * 2.54
            self.simacLinacModel.t_Fil = np.array([
             0.8676, 0.8647, 0.8292, 0.7704, 0.6908, 
             0.6415, 0.5489, 0.4862, 0.3906, 0.3245, 0.2535, 
             0.2131, 0.1501, 
             0.1065, 
             0.0593, 0.0]) * 2.54
            self.simacLinacModel.P_AC_Kly = 182.0
            self.simacUpdateLinacModel = True
        elif energyIndex == 2:
            self.simacLinacModel.d_Tank = 3.0
            self.simacLinacModel.i_Coil_BMag = 155.0
            self.simacLinacModel.v_Gun = 10.0
            self.simacLinacModel.v_Kly = 125.0
            self.simacLinacModel.v_Grid = -10.6
            self.simacLinacModel.Z_Acc = 47.88
            self.simacLinacModel.t_W = 1.925
            self.simacLinacModel.t_Cu = 7.168
            self.simacLinacModel.Factor = 1.0
            self.simacLinacModel.FilterCoefficients = self.simacLinacModel.Tungsten_murho
            self.simacLinacModel.FilterDensity = 16.9
            self.simacLinacModel.r_Fil = np.arange(0.0, 1.6, 0.1) * 2.54
            self.simacLinacModel.t_Fil = np.array([
             0.7832, 0.7482, 0.6556, 0.5403, 0.4617, 
             0.3932, 0.3451, 0.2513, 0.2054, 0.1517, 0.1289, 
             0.0835, 0.0566, 
             0.0281, 
             0.0193, 0.0415]) * 2.54
            self.simacLinacModel.P_AC_Kly = 67.0
            self.simacUpdateLinacModel = True
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_Omega(self, omega):
        self.simacLinacModel.Omega = omega
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_P_AC_Kly(self, P_AC_Kly):
        self.simacLinacModel.P_AC_Kly = P_AC_Kly
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_v_Kly(self, v_Kly):
        self.simacLinacModel.v_Kly = v_Kly
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_Tau(self, Tau):
        self.simacLinacModel.Tau = Tau
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_v_Gun(self, v_Gun):
        self.simacLinacModel.v_Gun = v_Gun
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_v_Grid(self, v_Grid):
        self.simacLinacModel.v_Grid = v_Grid
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_i_Coil_BMag(self, i_Coil_BMag):
        self.simacLinacModel.i_Coil_BMag = i_Coil_BMag
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_i_Pos_Rad(self, i_Pos_Rad):
        self.simacLinacModel.i_Pos_Rad = i_Pos_Rad
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_i_Pos_Trans(self, i_Pos_Trans):
        self.simacLinacModel.i_Pos_Trans = i_Pos_Trans
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_i_Ang_Rad(self, i_Ang_Rad):
        self.simacLinacModel.i_Ang_Rad = i_Ang_Rad
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_i_Ang_Trans(self, i_Ang_Trans):
        self.simacLinacModel.i_Ang_Trans = i_Ang_Trans
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_Rad_Jaw(self, Rad_Jaw):
        self.simacLinacModel.Rad_Jaw = Rad_Jaw
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_Trans_Jaw(self, Trans_Jaw):
        self.simacLinacModel.Trans_Jaw = Trans_Jaw
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel_d_Tank(self, d_Tank):
        self.simacLinacModel.d_Tank = d_Tank
        self.updateLinacModel()
        self.updateViews()

    def updateLinacModel(self):
        if self.simacUpdateLinacModel:
            self.simacLinacModel.updateLinacModel()
        self.simacLinacModel.updateLinacModel()

    def updateViews(self):
        self.simacMainView.updateView()
        self.simacKlystronView.updateView()
        self.simacAcceleratorView.updateView()
        self.simacTreatementHeadView.updateView()
# okay decompiling simacController.pyc
