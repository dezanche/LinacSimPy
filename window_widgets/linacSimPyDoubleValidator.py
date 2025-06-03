
from PyQt5.QtGui import QDoubleValidator, QValidator
from sys import float_info

class LinacSimPyDoubleValidator(QDoubleValidator):
    """
    Fix for strange behavior of default QDoubleValidator
    """

    def __init__(self, bottom=float_info.min, top=float_info.max, decimals=float_info.dig, parent=None):
        super(LinacSimPyDoubleValidator, self).__init__(bottom, top, decimals, parent)

    def validate(self, input, pos):
        state, pos = QDoubleValidator.validate(self, input, pos)
        if state == QValidator.Intermediate and input.toDouble() > bottom() and input.toDouble() < top():
            return (QValidator.Acceptable, pos)
        else:
            return (
             QValidator.Invalid, pos)

        return (state, pos)

