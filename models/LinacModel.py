# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: models\LinacModel.pyc
# Compiled at: 2016-09-19 09:17:08
import math, numpy as np
from scipy import special
from scipy import interpolate
#import sys

class SimacSetting:

    def __init__(self):
        self.PRF = 60.0
        self.Tau = 3.0
        self.Energy = 0
        self.Omega = 2856.0
        self.P_AC_Kly = 0.0
        self.v_Kly = 0.0
        self.v_Gun = 0.0
        self.i_Coil_BMag = 0.0
        self.v_Grid = 0.0
        self.i_Pos_Rad = 0.0
        self.i_Pos_Trans = 0.0
        self.i_Ang_Rad = 0.0
        self.i_Ang_Trans = 0.0
        self.Rad_Jaw = 15.0
        self.Trans_Jaw = 15.0
        self.d_Tank = 0.0
        self.dD_Ion = 0.0


class LinacModel:

    def __init__(self):
        self.iN_Points = 101
        self.Mod_Energies = 2
        self.iN_Points_Cross = 10001
        self.m_e = 0.511
        self.Perveance_Kly = 2.1e-06 * math.pow(1000, 1.5)
        self.Omega_0 = 2856.0
        self.Q_Kly = 2856.0 / 5.0
        self.Q_Acc = 2856.0 / 0.5
        self.k_Amp = 100
        self.Perveance_Acc = 2.11e-07 * math.pow(1000, 1.5)
        self.k_Acc = 1.0 / 3.0
        self.dPos = 35.0
        self.dAng = 5.0
        self.DelT_BMag = 0.0337
        self.DelT_BMag_Slit = 0.03
        self.k_BMag_Coil = 0.1
        self.Tungsten_S = np.loadtxt('resources/parameters/TungstenStoppingPowers.txt')
        self.Tungsten_murho = np.loadtxt('resources/parameters/TungstenMassAttenuationCoefficients.txt')
        self.Copper_S = np.loadtxt('resources/parameters/CopperStoppingPowers.txt')
        self.Copper_murho = np.loadtxt('resources/parameters/CopperMassAttenuationCoefficients.txt')
        self.d_Fil = 12.53
        self.d_Patient = 100.0
        self.Max_Patient = 25.0
        self.Energies = np.array([0.01, 0.015, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.1, 0.15, 0.2, 
         0.3, 0.4, 0.5, 0.55, 0.662, 0.8, 1, 1.25, 1.5, 2, 3, 
         4, 5, 6, 8, 10, 15, 20, 30, 40])
        self.MassCoefficients = np.array([5.066, 1.568, 0.7613, 0.3612, 0.2629, 0.2245, 0.2046, 0.1833, 0.1706, 
         0.1505, 0.137, 0.1187, 0.1061, 0.0969, 0.093, 0.0857, 0.0787, 
         0.0707, 0.0632, 0.0575, 0.0494, 0.0397, 0.034, 0.0303, 
         0.0276, 0.0242, 0.0222, 0.0193, 0.0182, 0.0171, 0.0167])
        self.AbsorptionCoefficients = np.array([4.684, 1.269, 0.5016, 0.1411, 0.0637, 0.0396, 0.0305, 0.0255, 0.0253, 
         0.0276, 0.0297, 0.032, 0.0328, 0.033, 0.0329, 0.0326, 0.0321, 
         0.031, 0.0297, 0.0283, 0.0261, 0.0228, 0.0207, 0.0192, 
         0.018, 0.0165, 0.0157, 0.0144, 0.0139, 0.0134, 0.0131])
        self.Rho_Water = 1.0
        self.Rad_Av_SMag = 0.0
        self.dRad_Av_SMag = 0.0
        self.Trans_Av_SMag = 0.0
        self.dTrans_Av_SMag = 0.0
        self.Rad_StDev_SMag = 0.07
        self.dRad_StDev_SMag = 0.1 * math.pi / 180.0
        self.Trans_StDev_SMag = 0.07
        self.dTrans_StDev_SMag = 0.1 * math.pi / 180.0
        self.PRF = 60.0
        self.Tau = 3.0
        self.Omega = 2856.0
        self.P_AC_Kly = 0.0
        self.v_Kly = 0.0
        self.v_Gun = 0.0
        self.i_Coil_BMag = 0.0
        self.v_Grid = 0.0
        self.Z_Acc = 47.88
        self.i_Pos_Rad = 0.0
        self.i_Pos_Trans = 0.0
        self.i_Ang_Rad = 0.0
        self.i_Ang_Trans = 0.0
        self.t_W = 0.0
        self.t_Cu = 0.0
        self.Factor = 1.0
        self.r_Fil = np.array([0.0, 1.5]) * 2.54
        self.t_Fil = np.array([0.0, 0.0])
        self.FilterCoefficients = 0.0
        self.FilterDensity = 0.0
        self.Rad_Jaw = 15.0
        self.Trans_Jaw = 15.0
        self.d_Tank = 0.0
        self.P_Acc = 0.0
        self.i_Acc = 0.0
        self.T_Av_BMag = 0.0
        self.T_Av_Tar = 0.0
        self.i_Tar = 0.0
        self.dD_Ion = 0.0
        self.S_Ion_R = 0.0
        self.S_Ion_T = 0.0
        self.Flatness_R = 0.0
        self.Flatness_T = 0.0
        self.P_AC_Kly_C = 0.0
        self.P_Acc_Max = 0.0
        self.Chi = 0.0
        self.k_Kly = 0.0
        self.P_DC_Kly = 0.0
        self.Efficiency = 0.0
        self.v_PFN = 0.0
        self.i_HVPS = 0.0
        self.i_Kly = 0.0
        self.R_Coeff = 0.0
        self.P_Kly_Refl = 0.0
        self.P_Beam_Acc = 0.0
        self.i_BMag_Beam = 0.0
        self.Eff_Acc = 0.0
        self.DutyCycle = 0.0
        self.PrincipalRay_Tar = 0.0
        self.Eff_Tar = 0.0
        self.I_Tar = 0.0
        self.Angles = 0.0
        self.E_Tar = 0.0
        self.E_Fil = 0.0
        self.Coefficient = 0.0
        self.I_Fil_Rad = 0.0
        self.I_Fil_Trans = 0.0
        self.Rad_Fil = 0.0
        self.Trans_Fil = 0.0
        self.Rad_Patient = 0.0
        self.Trans_Patient = 0.0
        self.Rad_Fine = 0.0
        self.Trans_Fine = 0.0
        self.ACoefficient = 0.0
        self.MCoefficient = 0.0
        self.Dose_E_Rad = 0.0
        self.Dose_E_Trans = 0.0
        self.Dose_Rad = 0.0
        self.Dose_Trans = 0.0
        self.Half_Dose_Rad_Left = 0.0
        self.Half_Dose_Rad_Right = 0.0
        self.Half_Dose_Trans_Left = 0.0
        self.Half_Dose_Trans_Right = 0.0
        self.PrincipalRay_Tar = np.array([self.Rad_Av_SMag, self.dRad_Av_SMag, self.Trans_Av_SMag, self.dTrans_Av_SMag])
        self.FilterCoefficients = self.Copper_murho

    def updateLinacModel(self):
        self.klystron()
        self.accelerator_structure()
        self.steering_magnets()
        self.bending_magnet()
        self.target()
        self.Filter()
        self.Patient()

    def klystron(self):
        self.P_AC_Kly_C = 2226.7 / (self.v_Kly - 91.765)
        if self.P_AC_Kly_C < 0.0:
            self.P_AC_Kly_C = float('inf')
        self.P_Acc_Max = 0.12 * self.v_Kly - 9.37
        if self.P_Acc_Max < 0.0:
            self.P_Acc_Max = 0.0
        self.Chi = 1.0 / math.sqrt(self.P_AC_Kly_C) * math.sqrt(self.P_AC_Kly) * 1.84
        if math.isinf(self.P_AC_Kly_C):
            self.k_Kly = float('nan')
            self.P_Acc = float('nan')
        else:
            self.k_Kly = 10.0 * math.log10(self.P_Acc_Max * math.pow(10.0, 6) / self.P_AC_Kly_C * (10.0 * math.pow(special.jv(1, self.Chi) / self.Chi, 2)))
            self.P_Acc = math.pow(10.0, self.k_Kly / 10.0) * math.pow(10.0, -6) * self.P_AC_Kly
        if math.isnan(self.P_Acc):
            self.P_Acc = 0.0
        Z_Source = math.sqrt(1.0 + 4.0 * math.pow(self.Q_Kly, 2.0) * math.pow(self.Omega / self.Omega_0 - 1.0, 2))
        Z_Load = math.sqrt(1.0 + 4.0 * math.pow(self.Q_Acc, 2.0) * math.pow(self.Omega / self.Omega_0 - 1.0, 2))
        self.R_Coeff = (Z_Load - Z_Source) / (Z_Load + Z_Source)
        self.P_Kly_Refl = math.pow(self.R_Coeff, 2.0) * self.P_Acc
        self.P_Acc = self.P_Acc - self.P_Kly_Refl
        self.i_Kly = self.Perveance_Kly * math.pow(self.v_Kly, 3.0 / 2.0)
        self.P_DC_Kly = self.Perveance_Kly * math.pow(self.v_Kly, 3.0 / 2.0) * self.v_Kly / 1000.0
        if self.P_DC_Kly != 0.0:
            self.Efficiency = self.P_Acc / self.P_DC_Kly * 100.0
        else:
            self.Efficiency = 0.0
        self.v_PFN = self.v_Kly * 2.0 / 4.0
        self.i_HVPS = self.v_PFN * 6.0 / 5.0 / 70.0

    def accelerator_structure(self):
        self.DutyCycle = self.Tau * self.PRF * math.pow(10.0, -6.0)
        self.i_Acc = np.real(self.Perveance_Acc * math.pow(self.v_Gun + self.k_Amp * self.v_Grid / 1000.0, 3.0 / 2.0) * 1000.0)
        self.i_BMag_Beam = self.k_Acc * self.i_Acc
        self.T_Av_BMag = math.sqrt(self.P_Acc * self.Z_Acc) - self.Z_Acc * (self.i_BMag_Beam / 1000.0) / 2.0
        if self.T_Av_BMag < 0.0:
            self.T_Av_BMag = 0.0
        self.P_Beam_Acc = self.T_Av_BMag * (self.i_BMag_Beam / 1000.0)
        if self.P_Acc != 0.0:
            self.Eff_Acc = 100.0 * self.P_Beam_Acc / self.P_Acc * self.Tau / 5.0
        else:
            self.Eff_Acc = 0.0

    def steering_magnets(self):
        DelTheta_Pos_Rad = self.i_Pos_Rad / 500.0 * (math.pi / 180.0 / 2.0)
        DelTheta_Ang_Rad = self.i_Ang_Rad / 500.0 * (2.0 * math.pi / 180.0)
        DelTheta_Pos_Trans = self.i_Pos_Trans / 500.0 * (math.pi / 180.0 / 2.0)
        DelTheta_Ang_Trans = self.i_Ang_Trans / 500.0 * (2.0 * math.pi / 180.0)
        Pos_Rad = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, DelTheta_Pos_Rad], [0.0, 0.0, 1.0]])
        Pos_Trans = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, DelTheta_Pos_Trans], [0.0, 0.0, 1.0]])
        D1 = np.array([[1.0, self.dPos, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        Ang_Rad = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, DelTheta_Ang_Rad], [0.0, 0.0, 1.0]])
        Ang_Trans = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, DelTheta_Ang_Trans], [0.0, 0.0, 1.0]])
        PrincipalRay_BMag_Rad = np.dot(np.dot(np.dot(Ang_Rad, D1), Pos_Rad), np.array([self.Rad_Av_SMag, self.dRad_Av_SMag, 1.0]))
        PrincipalRay_BMag_Trans = np.dot(np.dot(np.dot(Ang_Trans, D1), Pos_Trans), np.array([self.Trans_Av_SMag, self.dTrans_Av_SMag, 1.0]))
        PrincipalRay_Tar_Rad = PrincipalRay_BMag_Rad
        PrincipalRay_Tar_Trans = PrincipalRay_BMag_Trans
        self.PrincipalRay_Tar = np.concatenate((PrincipalRay_Tar_Rad[0:2], PrincipalRay_Tar_Trans[0:2]), axis=0)

    def bending_magnet(self):
        self.T_Av_Tar = math.sqrt(math.pow(self.k_BMag_Coil * self.i_Coil_BMag, 2) + math.pow(self.m_e, 2)) - self.m_e
        if self.T_Av_BMag != 0.0:
            Max = (self.T_Av_Tar - self.T_Av_BMag + self.DelT_BMag_Slit * self.T_Av_Tar) / (self.DelT_BMag * self.T_Av_BMag)
            Min = (self.T_Av_Tar - self.T_Av_BMag - self.DelT_BMag_Slit * self.T_Av_Tar) / (self.DelT_BMag * self.T_Av_BMag)
            k_BMag = 1.0 / 2.0 * (special.erf(Max / math.sqrt(2.0)) - special.erf(Min / math.sqrt(2.0)))
            if math.isnan(k_BMag):
                k_BMag = 0.0
            self.i_Tar = k_BMag * self.i_BMag_Beam * self.DutyCycle * 1000.0
        else:
            self.i_Tar = 0.0

    def target(self):
        Max = 0.4
        Step = Max / (self.iN_Points - 1.0)
        self.Angles = np.arange(0.0, Max + 0.001, Step)
        self.Angles.shape = (1, 101)
        if self.T_Av_Tar <= 0.01:
            self.E_Tar = np.ones(((self.iN_Points - 1.0) / self.Mod_Energies, 1.0)) * 0.01
        else:
            self.E_Tar = np.arange(0.01, self.T_Av_Tar, self.T_Av_Tar / ((self.iN_Points - 1.0) / self.Mod_Energies))
        self.E_Tar.shape = (50, 1)
        murho_W = interpolate.pchip_interpolate(self.Tungsten_murho[:, 0], self.Tungsten_murho[:, 1], self.E_Tar)
        murho_W.shape = (50, 1)
        murho_Cu = interpolate.pchip_interpolate(self.Copper_murho[:, 0], self.Copper_murho[:, 1], self.E_Tar)
        murho_Cu.shape = (50, 1)
        self.I_Tar = np.zeros((self.E_Tar.size, self.Angles.size))
        Points = 200
        N_A_x_a = 0.0066242
        Z_W = 74.0
        A_W = 183.84
        b = 0.83
        X_0_W = 6.76
        E_s = 13.6 * math.sqrt(2.0)
        CurrentE = self.T_Av_Tar
        t_WVec = np.arange(0, self.t_W + self.t_W / (Points - 1), self.t_W / (Points - 1))
        t_WVec = np.power(t_WVec / self.t_W, 3.0) * self.t_W
        Ener = np.zeros(self.E_Tar.shape)
        for iIndex in range(0, t_WVec.size - 1):
            x = t_WVec[iIndex]
            if CurrentE <= 0.01:
                break
            Theta_b = self.Factor * self.m_e / (CurrentE + self.m_e)
            Theta_e = 0.0
            if x == 0.0:
                Theta_e = 0.0
            else:
                Theta_e = E_s / (self.m_e + self.T_Av_Tar) * math.sqrt(x / X_0_W) * (1 + 0.038 * math.log(x / X_0_W))
            if Theta_e < 0.0:
                Theta_e = 0.0
            if Theta_e > 0.8:
                Theta_e = 0.8
            pchip_interpolator = interpolate.interp1d(self.Tungsten_S[:, 0], self.Tungsten_S[:, 3])
            S = pchip_interpolator(CurrentE)
            Addition = (t_WVec[iIndex + 1] - t_WVec[iIndex]) * N_A_x_a / A_W * np.power(Z_W, 2) * np.exp(-murho_Cu * self.t_Cu) * np.exp(-murho_W * (self.t_W - x)) * (1 - b * self.E_Tar / CurrentE) * 1 / (math.pi * (np.power(Theta_b, 2) + np.power(Theta_e, 2))) * np.exp(-np.power(self.Angles, 2) / (np.power(Theta_b, 2) + np.power(Theta_e, 2)))
            A2 = (t_WVec[iIndex + 1] - t_WVec[iIndex]) * N_A_x_a / A_W * np.power(Z_W, 2) * np.exp(-murho_Cu * self.t_Cu) * np.exp(-murho_W * (self.t_W - x)) * (1 - b * self.E_Tar / CurrentE)
            A2[A2 < 0] = 0.0
            Addition[Addition < 0] = 0.0
            self.I_Tar = self.I_Tar + Addition
            Ener = Ener + A2
            CurrentE = CurrentE - (t_WVec[iIndex + 1] - t_WVec[iIndex]) * S

        X_0_Cu = 12.86
        Z_Cu = 29
        A_Cu = 63.55
        for x in np.arange(self.t_W, self.t_W + self.t_Cu, self.t_Cu / Points):
            if CurrentE <= 0.01:
                break
            Theta_b = self.Factor * self.m_e / (CurrentE + self.m_e)
            Theta_e = E_s / (self.m_e + self.T_Av_Tar) * math.sqrt(self.t_W / X_0_W + (x - self.t_W) / X_0_Cu) * (1 + 0.038 * np.log(self.t_W / X_0_W + (x - self.t_W) / X_0_Cu))
            if math.isnan(Theta_e):
                Theta_e = 0
            if Theta_e < 0:
                Theta_e = 0
            if Theta_e > 0.8:
                Theta_e = 0.8
            pchip_interpolator2 = interpolate.interp1d(self.Copper_S[:, 0], self.Copper_S[:, 1])
            S = pchip_interpolator2(CurrentE)
            Addition = self.t_Cu / Points * N_A_x_a / A_Cu * np.power(Z_Cu, 2) * np.exp(-murho_Cu * (self.t_W + self.t_Cu - x)) * (1 - b * self.E_Tar / CurrentE) * 1 / (math.pi * (Theta_b * Theta_b + Theta_e * Theta_e)) * np.exp(-self.Angles * self.Angles / (Theta_b * Theta_b + Theta_e * Theta_e))
            A2 = self.t_Cu / Points * N_A_x_a / A_Cu * np.power(Z_Cu, 2) * np.exp(-murho_Cu * (self.t_W + self.t_Cu - x)) * (1 - b * self.E_Tar / CurrentE)
            A2[A2 < 0] = 0.0
            Addition[Addition < 0] = 0.0
            self.I_Tar = self.I_Tar + Addition
            Ener = Ener + A2
            CurrentE = CurrentE - self.t_Cu / Points * S

        self.I_Tar = 1000000 * self.I_Tar * self.i_Tar / 1000000
        Ener = Ener * self.i_Tar
        self.Eff_Tar = np.sum(Ener) * self.T_Av_Tar / ((self.iN_Points - 1) / self.Mod_Energies) / (self.i_Tar * self.T_Av_Tar) * 100

    def Filter(self):
        self.Rad_Patient = np.arange(-self.Max_Patient, self.Max_Patient + 0.001, 2 * self.Max_Patient / (self.iN_Points - 1))
        self.Trans_Patient = np.arange(-self.Max_Patient, self.Max_Patient + 0.001, 2 * self.Max_Patient / (self.iN_Points - 1))
        self.Rad_Fil = self.PrincipalRay_Tar[0] + (self.Rad_Patient - self.PrincipalRay_Tar[0]) * self.d_Fil / self.d_Patient
        self.Trans_Fil = self.PrincipalRay_Tar[2] + (self.Trans_Patient - self.PrincipalRay_Tar[2]) * self.d_Fil / self.d_Patient
        Theta_Rad = np.arctan((self.Rad_Fil - self.PrincipalRay_Tar[0]) / self.d_Fil) - self.PrincipalRay_Tar[1]
        Theta_Trans = np.arctan((self.Trans_Fil - self.PrincipalRay_Tar[2]) / self.d_Fil) - self.PrincipalRay_Tar[3]
        Angles_Rad = np.arctan(np.sqrt(np.tan(Theta_Rad) * np.tan(Theta_Rad) + np.tan(Theta_Trans[math.ceil(Theta_Trans.size / 2.0)]) * np.tan(Theta_Trans[math.ceil(Theta_Trans.size / 2.0)])))
        Angles_Trans = np.arctan(np.sqrt(np.tan(Theta_Rad[math.ceil(Theta_Rad.size / 2.0)]) * np.tan(Theta_Rad[math.ceil(Theta_Rad.size / 2.0)]) + np.tan(Theta_Trans) * np.tan(Theta_Trans)))
        self.Angles.shape = 101
        interpolator_I_Fil_Rad = interpolate.interp1d(self.Angles, self.I_Tar)
        self.I_Fil_Rad = interpolator_I_Fil_Rad(Angles_Rad)
        interpolator_I_Fil_Trans = interpolate.interp1d(self.Angles, self.I_Tar)
        self.I_Fil_Trans = interpolator_I_Fil_Trans(Angles_Trans)
        self.Rad_Fil, self.E_Fil = np.meshgrid(self.Rad_Fil, self.E_Tar)
        self.Trans_Fil, self.E_Fil = np.meshgrid(self.Trans_Fil, self.E_Tar)
        Thickness_Rad = interpolate.pchip_interpolate(self.r_Fil, self.t_Fil, np.sqrt(self.Rad_Fil * self.Rad_Fil))
        Thickness_Trans = interpolate.pchip_interpolate(self.r_Fil, self.t_Fil, np.sqrt(self.Trans_Fil * self.Trans_Fil))
        self.Coefficient = interpolate.pchip_interpolate(self.FilterCoefficients[:, 0], self.FilterCoefficients[:, 1], self.E_Fil)
        self.Coefficient[0, :] = 0.0
        self.I_Fil_Rad = self.I_Fil_Rad * np.exp(-self.Coefficient * Thickness_Rad * self.FilterDensity)
        self.I_Fil_Trans = self.I_Fil_Trans * np.exp(-self.Coefficient * Thickness_Trans * self.FilterDensity)
        self.I_Fil_Rad = self.I_Fil_Rad * self.d_Fil / np.power(self.d_Fil * self.d_Fil + np.power(self.Rad_Fil - self.PrincipalRay_Tar[0], 2) + np.power(0 - self.PrincipalRay_Tar[2], 2), 3.0 / 2.0)
        self.I_Fil_Trans = self.I_Fil_Trans * self.d_Fil / np.power(self.d_Fil * self.d_Fil + np.power(0 - self.PrincipalRay_Tar[0], 2) + np.power(self.Trans_Fil - self.PrincipalRay_Tar[2], 2), 3.0 / 2.0)

    def Patient(self):
        self.E_Fil.shape = (5050, )
        spline_ACoefficient = interpolate.InterpolatedUnivariateSpline(self.Energies, self.AbsorptionCoefficients)
        self.ACoefficient = spline_ACoefficient(self.E_Fil)
        spline_MCoefficient = interpolate.InterpolatedUnivariateSpline(self.Energies, self.MassCoefficients)
        self.MCoefficient = spline_MCoefficient(self.E_Fil)
        self.ACoefficient.shape = (50, 101)
        self.MCoefficient.shape = (50, 101)
        self.Dose_E_Rad = np.exp(-(self.d_Tank * self.Rho_Water) * self.MCoefficient) * self.I_Fil_Rad * self.ACoefficient * 60 * 100 * 1000
        self.Dose_E_Trans = np.exp(-(self.d_Tank * self.Rho_Water) * self.MCoefficient) * self.I_Fil_Trans * self.ACoefficient * 60 * 100 * 1000
        Dose_R = np.sum(self.Dose_E_Rad, 0) * (self.T_Av_Tar / ((self.iN_Points - 1) / self.Mod_Energies)) * np.power(self.d_Fil / self.d_Patient, 2)
        Dose_T = np.sum(self.Dose_E_Trans, 0) * (self.T_Av_Tar / ((self.iN_Points - 1) / self.Mod_Energies)) * np.power(self.d_Fil / self.d_Patient, 2)
        t = self.Rad_Fil[1, :] > self.Rad_Jaw * self.d_Fil / self.d_Patient
        Dose_R[np.fabs(self.Rad_Fil[1, :]) > self.Rad_Jaw * self.d_Fil / self.d_Patient] = 0.0
        Dose_T[np.fabs(self.Trans_Fil[1, :]) > self.Trans_Jaw * self.d_Fil / self.d_Patient] = 0.0
        Gauss_R = 1 / np.sqrt(2 * math.pi * self.Rad_StDev_SMag * self.Rad_StDev_SMag) * np.exp(-1.0 / 2.0 * np.power(self.Rad_Patient[np.fabs(self.Rad_Patient) <= 5.0] * self.d_Fil / (self.d_Patient - self.d_Fil) / self.Rad_StDev_SMag, 2))
        Gauss_T = 1 / np.sqrt(2 * math.pi * self.Trans_StDev_SMag * self.Trans_StDev_SMag) * np.exp(-1.0 / 2.0 * np.power(self.Trans_Patient[np.fabs(self.Trans_Patient) <= 5.0] * self.d_Fil / (self.d_Patient - self.d_Fil) / self.Trans_StDev_SMag, 2))
        Dose_R = np.convolve(Dose_R, Gauss_R, 'same') * (2 * self.Max_Patient / (self.iN_Points - 1) * self.d_Fil / (self.d_Patient - self.d_Fil))
        Dose_T = np.convolve(Dose_T, Gauss_T, 'same') * (2 * self.Max_Patient / (self.iN_Points - 1) * self.d_Fil / (self.d_Patient - self.d_Fil))
        self.dD_Ion = Dose_R[math.ceil(Dose_R.size / 2.0)]
        self.Rad_Fine = np.arange(-self.Max_Patient, self.Max_Patient + 0.001, 2 * self.Max_Patient / (self.iN_Points_Cross - 1))
        self.Trans_Fine = np.arange(-self.Max_Patient, self.Max_Patient + 0.001, 2 * self.Max_Patient / (self.iN_Points_Cross - 1))
        interpolator_Dose_Rad = interpolate.interp1d(self.Rad_Patient, Dose_R, bounds_error=False)
        self.Dose_Rad = interpolator_Dose_Rad(self.Rad_Fine)
        interpolator_Dose_Trans = interpolate.interp1d(self.Trans_Patient, Dose_T, bounds_error=False)
        self.Dose_Trans = interpolator_Dose_Trans(self.Trans_Fine)
        max_Dose_Rad = np.max(self.Dose_Rad)
        # can be == 0 which causes error indexing into index_array
        if max_Dose_Rad == 0:
            half_field_size = 0
        else:
            index_array = np.where(self.Dose_Rad > max_Dose_Rad / 2.0)
            #print(np.shape(index_array)) # added for debugging crash on next line
            left_half_index = index_array[0][0]
            right_half_index = index_array[0][-1]
            self.Half_Dose_Rad_Left = self.Rad_Fine[left_half_index]
            self.Half_Dose_Rad_Right = self.Rad_Fine[right_half_index]
            field_size = 0.8 * (right_half_index - left_half_index)
            half_field_size = int(field_size / 2)
        # added int() to fix "TypeError: slice indices must be integers or None or have an __index__ method"
        self.S_Ion_R = 100.0 * np.nansum(self.Dose_Rad[int((self.Dose_Rad.size - 1) / 2): int((self.Dose_Rad.size - 1) / 2) + half_field_size] - self.Dose_Rad[int((self.Dose_Rad.size + 1) / 2) - half_field_size: int((self.Dose_Rad.size + 1) / 2)]) / np.nansum(self.Dose_Rad[int((self.Dose_Rad.size + 1) / 2) - half_field_size:int((self.Dose_Rad.size - 1) / 2) + half_field_size])
        max_Dose_Trans = np.max(self.Dose_Trans)
        if max_Dose_Trans == 0:
            half_field_size = 0
        else:
            index_array = np.where(self.Dose_Trans > max_Dose_Trans / 2.0)
            left_half_index = index_array[0][0]
            right_half_index = index_array[0][-1]
            self.Half_Dose_Trans_Left = self.Trans_Fine[left_half_index]
            self.Half_Dose_Trans_Right = self.Trans_Fine[right_half_index]
            field_size = 0.8 * (right_half_index - left_half_index)
            half_field_size = int(field_size / 2)
        # added int() to fix "TypeError: slice indices must be integers or None or have an __index__ method"
        self.S_Ion_T = 100.0 * np.nansum(self.Dose_Trans[int((self.Dose_Trans.size - 1) / 2):int((self.Dose_Trans.size - 1) / 2) + half_field_size] - self.Dose_Trans[int((self.Dose_Trans.size + 1) / 2) - half_field_size: int((self.Dose_Trans.size + 1) / 2)]) / np.nansum(self.Dose_Trans[int((self.Dose_Trans.size + 1) / 2) - half_field_size:int((self.Dose_Trans.size - 1) / 2) + half_field_size])
        min_R = np.argmin(np.fabs(self.Rad_Fine - 0.9 * self.Rad_Jaw))
        min_T = np.argmin(np.fabs(self.Trans_Fine - 0.9 * self.Trans_Jaw))
        self.Flatness_R = 100.0 * np.fabs(self.Dose_Rad[min_R] - self.dD_Ion) / self.dD_Ion
        self.Flatness_T = 100.0 * np.fabs(self.Dose_Trans[min_T] - self.dD_Ion) / self.dD_Ion

# misspelled and not used anywhere?
    def updateSingal(self, typicalValue, signalLevel, noiseLevel, sample, dMax_Voltage, dStep_Time, dDiv_Time):
        tempVector = np.flipud(np.arange(0, sample[(0, 0)], -dStep_Time))
        tempVector2 = np.arange(dStep_Time, sample[(-1, 0)], dStep_Time)
        dPulseTimeVector = np.concatenate([tempVector, tempVector2])
        fInterpolator = interpolate.interp1d(sample[:, 0], sample[:, 1])
        Pulse = signalLevel * 1 / dMax_Voltage * fInterpolator(dPulseTimeVector)
        iNum_Pulses = math.floor(4 * dDiv_Time * self.PRF)
        if iNum_Pulses / self.PRF + sample[(-1, 0)] > 4 * dDiv_Time:
            tMax = iNum_Pulses / self.PRF + sample[(-1, 0)]
        else:
            tMax = 4 * dDiv_Time
        if -iNum_Pulses / self.PRF + sample[(0, 0)] < -4 * dDiv_Time:
            tMin = -iNum_Pulses / self.PRF + sample[(0, 0)]
        else:
            tMin = -4 * dDiv_Time
        tempVector = np.flipud(np.arange(0, tMin, -dStep_Time))
        tempVector2 = np.arange(dStep_Time, tMax, dStep_Time)
        dVector_Time = np.concatenate([tempVector, tempVector2])
        if noiseLevel == 0.0:
            dVector_Voltage = np.random.normal(typicalValue / dMax_Voltage, 1e-05 / dMax_Voltage, dVector_Time.size)
        else:
            dVector_Voltage = np.random.normal(typicalValue / dMax_Voltage, noiseLevel * 1 / dMax_Voltage, dVector_Time.size)
        for iCount in range(int(-iNum_Pulses), int(iNum_Pulses) + 1, 1):
            iIndex = np.argmin(np.abs(dVector_Time - float(iCount) / float(self.PRF) - sample[(0,
                                                                                               0)]))
            dVector_Voltage[iIndex:(iIndex + Pulse.size)] = Pulse

        return [dVector_Time, dVector_Voltage]
# okay decompiling LinacModel.pyc
