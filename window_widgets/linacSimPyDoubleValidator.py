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


# unused because config dialog doesn't work

from PyQt5.QtGui import QDoubleValidator, QValidator
#from sys import float_info  #sys already imported

class LinacSimPyDoubleValidator(QDoubleValidator):
    """
    Fix for strange behavior of default QDoubleValidator
    """

    def __init__(self, bottom=float_info.min, top=float_info.max, decimals=float_info.dig, parent=None):
        super(LinacSimPyDoubleValidator, self).__init__(bottom, top, decimals, parent)

    def validate(self, input, pos):
        state, pos = QDoubleValidator.validate(self, input, pos)
        if state == QValidator.Intermediate and input.toDouble() > bottom() and input.toDouble() < top():   # should be something.top() and .bottom()
            return (QValidator.Acceptable, pos)
        else:
            return (
             QValidator.Invalid, pos)

        return (state, pos)

