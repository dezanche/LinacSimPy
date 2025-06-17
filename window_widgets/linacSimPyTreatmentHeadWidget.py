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


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8('Form'))
        Form.resize(800, 1000)   # was 640; doesn't do anything
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(800, 640))
        Form.setMaximumSize(QtCore.QSize(800, 1000)) # works; was 800,640
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        #self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        #self.gridLayout_3.setObjectName(_fromUtf8('gridLayout_3'))
        #self.gridLayout = QtWidgets.QGridLayout()
        #self.gridLayout.setObjectName(_fromUtf8('gridLayout'))
        
        # split original grid into nested horizontal and vertical layouts
        
        self.verticalStack = QtWidgets.QVBoxLayout(Form)
        self.topRow = QtWidgets.QHBoxLayout()
        self.topRow.setObjectName(_fromUtf8('topRow'))
        self.bottomRow = QtWidgets.QHBoxLayout()
        self.bottomRow.setObjectName(_fromUtf8('bottomRow'))  
        
        # top left frame
        self.frame_TL = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_TL.sizePolicy().hasHeightForWidth())
        self.frame_TL.setSizePolicy(sizePolicy)
        self.frame_TL.setMinimumSize(QtCore.QSize(300, 270))
        self.frame_TL.setMaximumSize(QtCore.QSize(600, 270))    #was 400, 270
        self.frame_TL.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TL.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_TL.setObjectName(_fromUtf8('frame_TL'))
        
        # deleted unnecessary vertical layout
        #self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_TL)
        #self.verticalLayout_2.setContentsMargins(6,6,6,6)
        #self.verticalLayout_2.setObjectName(_fromUtf8('verticalLayout_2'))
        
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_TL)
        self.gridLayout_5.setObjectName(_fromUtf8('gridLayout_5'))
        
        # Treatment Head Parameters frame
        edit_box_width = 60
        self.frame_6 = QtWidgets.QFrame(self.frame_TL)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8('frame_6'))
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_4.setContentsMargins(0,0,0,0)
        self.gridLayout_4.setObjectName(_fromUtf8('gridLayout_4'))
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName(_fromUtf8('gridLayout_2'))
        
        # Bending magnet text
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        # commented out to allow full width
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        # self.label_3.setSizePolicy(sizePolicy)
        # self.label_3.setMinimumSize(QtCore.QSize(10, 0))
        # self.label_3.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8('label_3'))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        
        # Targe current text
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        # self.label_4.setSizePolicy(sizePolicy)
        # self.label_4.setMinimumSize(QtCore.QSize(10, 0))
        # self.label_4.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8('label_4'))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        
        # In-plane beam edge number
        self.lineEdit_L_Pos_Rad = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_L_Pos_Rad.sizePolicy().hasHeightForWidth())
        self.lineEdit_L_Pos_Rad.setSizePolicy(sizePolicy)
        self.lineEdit_L_Pos_Rad.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_L_Pos_Rad.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_L_Pos_Rad.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_L_Pos_Rad.setObjectName(_fromUtf8('lineEdit_L_Pos_Rad'))
        self.gridLayout_2.addWidget(self.lineEdit_L_Pos_Rad, 5, 1, 1, 1)
        self.lineEdit_Rad_Jaw = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Rad_Jaw.sizePolicy().hasHeightForWidth())
        self.lineEdit_Rad_Jaw.setSizePolicy(sizePolicy)
        self.lineEdit_Rad_Jaw.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_Rad_Jaw.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_Rad_Jaw.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Rad_Jaw.setObjectName(_fromUtf8('lineEdit_Rad_Jaw'))
        self.gridLayout_2.addWidget(self.lineEdit_Rad_Jaw, 2, 3, 1, 1)
        
        # Radial S text
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        # self.label_12.setSizePolicy(sizePolicy)
        # self.label_12.setMinimumSize(QtCore.QSize(100, 0))
        # self.label_12.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8('label_12'))
        self.gridLayout_2.addWidget(self.label_12, 4, 2, 1, 1)
        
        # Radial symmetry number
        self.lineEdit_S_Ion_R = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_S_Ion_R.sizePolicy().hasHeightForWidth())
        self.lineEdit_S_Ion_R.setSizePolicy(sizePolicy)
        self.lineEdit_S_Ion_R.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_S_Ion_R.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_S_Ion_R.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_S_Ion_R.setObjectName(_fromUtf8('lineEdit_S_Ion_R'))
        self.gridLayout_2.addWidget(self.lineEdit_S_Ion_R, 4, 3, 1, 1)
        
        # In-plane beam edge text
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        # self.label_13.setSizePolicy(sizePolicy)
        # self.label_13.setMinimumSize(QtCore.QSize(10, 0))
        # self.label_13.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8('label_13'))
        self.gridLayout_2.addWidget(self.label_13, 5, 0, 1, 1)
        
        # Tank measurement depth text
        self.lineEdit_d_Tank = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_d_Tank.sizePolicy().hasHeightForWidth())
        self.lineEdit_d_Tank.setSizePolicy(sizePolicy)
        self.lineEdit_d_Tank.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_d_Tank.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_d_Tank.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_d_Tank.setObjectName(_fromUtf8('lineEdit_d_Tank'))
        self.gridLayout_2.addWidget(self.lineEdit_d_Tank, 10, 1, 1, 1)
        
        # Title text
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        # self.label_2.setSizePolicy(sizePolicy)
        # self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        # self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8('Helvetica'))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8('label_2'))
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 2)   # was 1, 0
        
        # Bending magnet energy number
        self.lineEdit_T_Av_Tar = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_T_Av_Tar.sizePolicy().hasHeightForWidth())
        self.lineEdit_T_Av_Tar.setSizePolicy(sizePolicy)
        self.lineEdit_T_Av_Tar.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_T_Av_Tar.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_T_Av_Tar.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_T_Av_Tar.setObjectName(_fromUtf8('lineEdit_T_Av_Tar'))
        self.gridLayout_2.addWidget(self.lineEdit_T_Av_Tar, 2, 1, 1, 1)
        
        # Radial jaw position text
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        # self.label_5.setSizePolicy(sizePolicy)
        # self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        # self.label_5.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8('label_5'))
        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)
        
        # Target current text
        self.lineEdit_i_Tar = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_i_Tar.sizePolicy().hasHeightForWidth())
        self.lineEdit_i_Tar.setSizePolicy(sizePolicy)
        self.lineEdit_i_Tar.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_i_Tar.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_i_Tar.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_i_Tar.setObjectName(_fromUtf8('lineEdit_i_Tar'))
        self.gridLayout_2.addWidget(self.lineEdit_i_Tar, 3, 1, 1, 1)
        
        # Transverse jaw position text
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        # self.label_6.setSizePolicy(sizePolicy)
        # self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        # self.label_6.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8('label_6'))
        self.gridLayout_2.addWidget(self.label_6, 3, 2, 1, 1)
        
        # Transverse jaw position number
        self.lineEdit_Trans_Jaw = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Trans_Jaw.sizePolicy().hasHeightForWidth())
        self.lineEdit_Trans_Jaw.setSizePolicy(sizePolicy)
        self.lineEdit_Trans_Jaw.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_Trans_Jaw.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_Trans_Jaw.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Trans_Jaw.setObjectName(_fromUtf8('lineEdit_Trans_Jaw'))
        self.gridLayout_2.addWidget(self.lineEdit_Trans_Jaw, 3, 3, 1, 1)
        
        # Target efficiency text
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        # self.label_11.setSizePolicy(sizePolicy)
        # self.label_11.setMinimumSize(QtCore.QSize(10, 0))
        # self.label_11.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8('label_11'))
        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)
        
        # Target efficiency number
        self.lineEdit_Eff_Tar = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Eff_Tar.sizePolicy().hasHeightForWidth())
        self.lineEdit_Eff_Tar.setSizePolicy(sizePolicy)
        self.lineEdit_Eff_Tar.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_Eff_Tar.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_Eff_Tar.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Eff_Tar.setObjectName(_fromUtf8('lineEdit_Eff_Tar'))
        self.gridLayout_2.addWidget(self.lineEdit_Eff_Tar, 4, 1, 1, 1)
        
        # Transverse symmetry text
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        # self.label_17.setSizePolicy(sizePolicy)
        # self.label_17.setMinimumSize(QtCore.QSize(100, 0))
        # self.label_17.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName(_fromUtf8('label_17'))
        self.gridLayout_2.addWidget(self.label_17, 5, 2, 1, 1)
        
        # Transverse symmetry number
        self.lineEdit_S_Ion_T = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_S_Ion_T.sizePolicy().hasHeightForWidth())
        self.lineEdit_S_Ion_T.setSizePolicy(sizePolicy)
        self.lineEdit_S_Ion_T.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_S_Ion_T.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_S_Ion_T.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_S_Ion_T.setObjectName(_fromUtf8('lineEdit_S_Ion_T'))
        self.gridLayout_2.addWidget(self.lineEdit_S_Ion_T, 5, 3, 1, 1)
        
        # In-plane beam edge text
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        # self.label_7.setSizePolicy(sizePolicy)
        # self.label_7.setMinimumSize(QtCore.QSize(10, 0))
        # self.label_7.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8('label_7'))
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        
        # In-plane beam edge number
        self.lineEdit_R_Pos_Rad = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_R_Pos_Rad.sizePolicy().hasHeightForWidth())
        self.lineEdit_R_Pos_Rad.setSizePolicy(sizePolicy)
        self.lineEdit_R_Pos_Rad.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_R_Pos_Rad.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_R_Pos_Rad.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_R_Pos_Rad.setObjectName(_fromUtf8('lineEdit_R_Pos_Rad'))
        self.gridLayout_2.addWidget(self.lineEdit_R_Pos_Rad, 6, 1, 1, 1)
        
        # Radial flatness text
        self.label_18 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        # self.label_18.setSizePolicy(sizePolicy)
        # self.label_18.setMinimumSize(QtCore.QSize(100, 0))
        # self.label_18.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName(_fromUtf8('label_18'))
        self.gridLayout_2.addWidget(self.label_18, 6, 2, 1, 1)
        
        # Radial flatness number
        self.lineEdit_Flatness_R = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Flatness_R.sizePolicy().hasHeightForWidth())
        self.lineEdit_Flatness_R.setSizePolicy(sizePolicy)
        self.lineEdit_Flatness_R.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_Flatness_R.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_Flatness_R.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Flatness_R.setObjectName(_fromUtf8('lineEdit_Flatness_R'))
        self.gridLayout_2.addWidget(self.lineEdit_Flatness_R, 6, 3, 1, 1)
        
        # Left cross-plane beam edge text
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        # self.label_8.setSizePolicy(sizePolicy)
        # self.label_8.setMinimumSize(QtCore.QSize(10, 0))
        # self.label_8.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8('label_8'))
        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)
        
        # Left cross-plane beam edge number
        self.lineEdit_L_Pos_Trans = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_L_Pos_Trans.sizePolicy().hasHeightForWidth())
        self.lineEdit_L_Pos_Trans.setSizePolicy(sizePolicy)
        self.lineEdit_L_Pos_Trans.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_L_Pos_Trans.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_L_Pos_Trans.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_L_Pos_Trans.setObjectName(_fromUtf8('lineEdit_L_Pos_Trans'))
        self.gridLayout_2.addWidget(self.lineEdit_L_Pos_Trans, 7, 1, 1, 1)
        
        # Transverse flatness text
        self.label_19 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        # self.label_19.setSizePolicy(sizePolicy)
        # self.label_19.setMinimumSize(QtCore.QSize(100, 0))
        # self.label_19.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName(_fromUtf8('label_19'))
        self.gridLayout_2.addWidget(self.label_19, 7, 2, 1, 1)
        
        # Transverse flatness number
        self.lineEdit_Flatness_T = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Flatness_T.sizePolicy().hasHeightForWidth())
        self.lineEdit_Flatness_T.setSizePolicy(sizePolicy)
        self.lineEdit_Flatness_T.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_Flatness_T.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_Flatness_T.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Flatness_T.setObjectName(_fromUtf8('lineEdit_Flatness_T'))
        self.gridLayout_2.addWidget(self.lineEdit_Flatness_T, 7, 3, 1, 1)
        
        # Right cross-plane beam edge text
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        # self.label_9.setSizePolicy(sizePolicy)
        # self.label_9.setMinimumSize(QtCore.QSize(10, 0))
        # self.label_9.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8('label_9'))
        self.gridLayout_2.addWidget(self.label_9, 9, 0, 1, 1)
        
        # Right cross-plane beam edge number
        self.lineEdit_R_Pos_Trans = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_R_Pos_Trans.sizePolicy().hasHeightForWidth())
        self.lineEdit_R_Pos_Trans.setSizePolicy(sizePolicy)
        self.lineEdit_R_Pos_Trans.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_R_Pos_Trans.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_R_Pos_Trans.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_R_Pos_Trans.setObjectName(_fromUtf8('lineEdit_R_Pos_Trans'))
        self.gridLayout_2.addWidget(self.lineEdit_R_Pos_Trans, 9, 1, 1, 1)
        
        # Dose rate text
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        # self.label_20.setSizePolicy(sizePolicy)
        # self.label_20.setMinimumSize(QtCore.QSize(100, 0))
        # self.label_20.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_20.setWordWrap(False)
        self.label_20.setObjectName(_fromUtf8('label_20'))
        self.gridLayout_2.addWidget(self.label_20, 9, 2, 1, 1)
        
        #Dose rate number
        self.lineEdit_dD_Ion = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_dD_Ion.sizePolicy().hasHeightForWidth())
        self.lineEdit_dD_Ion.setSizePolicy(sizePolicy)
        self.lineEdit_dD_Ion.setFixedSize(edit_box_width, 20)    #added to make narrower
        #self.lineEdit_dD_Ion.setMinimumSize(QtCore.QSize(10, 0))
        #self.lineEdit_dD_Ion.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_dD_Ion.setObjectName(_fromUtf8('lineEdit_dD_Ion'))
        self.gridLayout_2.addWidget(self.lineEdit_dD_Ion, 9, 3, 1, 1)
        
        # Tank measurement depth text
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        # self.label_10.setSizePolicy(sizePolicy)
        # self.label_10.setMinimumSize(QtCore.QSize(10, 0))
        # self.label_10.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8('label_10'))
        self.gridLayout_2.addWidget(self.label_10, 10, 0, 1, 1)
        
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_6, 0, 0, 1, 1)
        #self.verticalLayout_2.addLayout(self.gridLayout_5)
        
        # replaced to avoid using a grid
        #self.gridLayout.addWidget(self.frame_TL, 0, 0, 1, 1)
        self.topRow.addWidget(self.frame_TL)
        
        # top right frame
        self.frame_TR = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_TR.sizePolicy().hasHeightForWidth())
        self.frame_TR.setSizePolicy(sizePolicy)
        self.frame_TR.setMaximumSize(QtCore.QSize(200, 270))    # was 400, 270
        self.frame_TR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TR.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_TR.setObjectName(_fromUtf8('frame_TR'))
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_TR)
        self.gridLayout_8.setObjectName(_fromUtf8('gridLayout_8'))
        self.label = QtWidgets.QLabel(self.frame_TR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(_fromUtf8(''))
        #self.label.setPixmap(QtGui.QPixmap(_fromUtf8('resources/images/Medical_Linac_Treatment_Head.svg')))
        #self.label.setScaledContents(True)
        # replaced above lines with following to maintain aspect ratio
        pixmap = QtGui.QPixmap(_fromUtf8('resources/images/Medical_Linac_Treatment_Head.svg')).scaled(200, 270, QtCore.Qt.KeepAspectRatio)
        # self.label.size() in scaled size above gives very small image
        self.label.setPixmap(pixmap)
        
        self.label.setObjectName(_fromUtf8('label'))
        # added tooltip
        self.label.setToolTip('https://upload.wikimedia.org/wikipedia/commons/e/e3/Medical_Linac.svg')
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        #self.gridLayout.addWidget(self.frame_TR, 0, 1, 1, 1)
        self.topRow.addWidget(self.frame_TR)
        
        # bottom right frame
        self.frame_BR = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_BR.sizePolicy().hasHeightForWidth())
        self.frame_BR.setSizePolicy(sizePolicy)
        self.frame_BR.setMinimumSize(QtCore.QSize(0, 400))  # was 330
        self.frame_BR.setMaximumSize(QtCore.QSize(400, 800))   # was 330
        self.frame_BR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BR.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_BR.setObjectName(_fromUtf8('frame_BR'))
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_BR)
        self.gridLayout_6.setContentsMargins(0,0,0,0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8('gridLayout_6'))
        self.gridLayout_BR = QtWidgets.QGridLayout()
        self.gridLayout_BR.setSpacing(0)
        self.gridLayout_BR.setObjectName(_fromUtf8('gridLayout_BR'))
        self.gridLayout_6.addLayout(self.gridLayout_BR, 0, 0, 1, 1)
        #self.gridLayout.addWidget(self.frame_BR, 2, 1, 1, 1)
        
        # bottom left frame
        self.frame_BL = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_BL.sizePolicy().hasHeightForWidth())
        self.frame_BL.setSizePolicy(sizePolicy)
        self.frame_BL.setMinimumSize(QtCore.QSize(390, 330))
        self.frame_BL.setMaximumSize(QtCore.QSize(390, 800))    # was 390,330
        self.frame_BL.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BL.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_BL.setObjectName(_fromUtf8('frame_BL'))
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_BL)
        self.gridLayout_7.setContentsMargins(0,0,0,0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(_fromUtf8('gridLayout_7'))
        self.gridLayout_BL = QtWidgets.QGridLayout()
        self.gridLayout_BL.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_BL.setObjectName(_fromUtf8('gridLayout_BL'))
        self.gridLayout_7.addLayout(self.gridLayout_BL, 0, 0, 1, 1)
        
        # self.gridLayout.addWidget(self.frame_BL, 2, 0, 1, 1)
        # self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.bottomRow.addWidget(self.frame_BL)
        self.bottomRow.addWidget(self.frame_BR)
        self.verticalStack.addLayout(self.topRow)
        self.verticalStack.addLayout(self.bottomRow)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate('Form', 'Treatment Head', None))
        self.label_3.setText(_translate('Form', 'Bending Magnet Energy [MeV]', None))
        self.label_4.setText(_translate('Form', 'Target Current [mA]', None))
        self.lineEdit_L_Pos_Rad.setText(_translate('Form', '0', None))
        self.lineEdit_Rad_Jaw.setText(_translate('Form', '0', None))
        self.label_12.setText(_translate('Form', 'Radial Symmetry [%]', None))
        self.lineEdit_S_Ion_R.setText(_translate('Form', '0', None))
        self.label_13.setText(_translate('Form', 'Beam Edge IP (target) [cm]', None))
        self.lineEdit_d_Tank.setText(_translate('Form', '0', None))
        # call this Output parameters? Results?
        self.label_2.setText(_translate('Form', 'Treatment Head Parameters', None))
        self.lineEdit_T_Av_Tar.setText(_translate('Form', '0', None))
        self.label_5.setText(_translate('Form', 'Radial Jaw Position [cm]', None))
        self.lineEdit_i_Tar.setText(_translate('Form', '0', None))
        self.label_6.setText(_translate('Form', 'Transverse Jaw Position [cm]', None))
        self.lineEdit_Trans_Jaw.setText(_translate('Form', '0', None))
        self.label_11.setText(_translate('Form', 'Target Efficiency [%]', None))
        self.lineEdit_Eff_Tar.setText(_translate('Form', '0', None))
        self.label_17.setText(_translate('Form', 'Transverse Symmetry [%]', None))
        self.lineEdit_S_Ion_T.setText(_translate('Form', '0', None))
        self.label_7.setText(_translate('Form', 'Beam Edge IP (gun) [cm]', None))
        self.lineEdit_R_Pos_Rad.setText(_translate('Form', '0', None))
        self.label_18.setText(_translate('Form', 'Radial Flatness [%]', None))
        self.lineEdit_Flatness_R.setText(_translate('Form', '0', None))
        self.label_8.setText(_translate('Form', 'Beam Edge XP (left) [cm]', None))
        self.lineEdit_L_Pos_Trans.setText(_translate('Form', '0', None))
        self.label_19.setText(_translate('Form', 'Transverse Flatness [%]', None))
        self.lineEdit_Flatness_T.setText(_translate('Form', '0', None))
        self.label_9.setText(_translate('Form', 'Beam Edge XP (right) [cm]', None))
        self.lineEdit_R_Pos_Trans.setText(_translate('Form', '0', None))
        self.label_20.setText(_translate('Form', 'Dose Rate [cGy/Min]', None))
        self.lineEdit_dD_Ion.setText(_translate('Form', '0', None))
        self.label_10.setText(_translate('Form', 'Measurement Depth [cm]', None))
        return

